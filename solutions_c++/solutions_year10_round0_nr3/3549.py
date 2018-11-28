#include <Windows.h>
#include <iostream>
#include <fstream>
#define IN_FILE "C-small-attempt0.in"
#define OUT_FILE "C-small-attempt0.out"

using namespace std;

void ReQueue(int * queue,int num,int N)
{
	for (int i=0;i<num;i++)
	{
		int t = queue[0];
		for (int j=0;j<N-1;j++)
		{
			queue[j] = queue[j+1];
		}
		queue[N-1] = t;
	}
}

int main()
{
	int caseNum;
	int R,K,N;
	ifstream in(IN_FILE);
	ofstream out(OUT_FILE);
	in >> caseNum;
	for (int n=0;n<caseNum;n++)
	{
		in >>R;
		in >>K;
		in >>N;
		int * group_queue = new int [N];
		for (int i=0;i<N;i++)
		{
			in >> group_queue[i];
		}
		int * money = new int [R];
		for (int i=0;i<R;i++)
		{
			int premoney = 0;
			int j = 0;
			do 
			{
				premoney += group_queue[j];
				j++;
			} while (j < N && premoney < K);
			if (premoney > K)
			{
				money[i] = premoney - group_queue[j-1];
				ReQueue(group_queue,j-1,N);
			}else
			{
				money[i] = premoney;
				if (j != N)
				{
					ReQueue(group_queue,j,N);
				}
			}
		}
		int sum_money = 0;
		for (int i=0;i<R;i++)
		{
			sum_money += money[i];
		}
		out << "Case #" << n+1 << ":"<< ' ' <<sum_money <<"\n";

		delete [] money;
		delete [] group_queue;
	}
	return 0;
}