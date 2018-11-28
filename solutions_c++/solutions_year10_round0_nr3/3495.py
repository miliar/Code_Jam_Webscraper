#include <iostream>
#include <queue>
#include <fstream>
using namespace std;

int main()
{
	int case_num=1;
	int cnt;
	int total;

	int R,K,N;
	queue<int> q1,q2;
	int temp;

	ifstream in("C-small-attempt1.in");
	ofstream out("C-small-attempt1.out");

	in >> cnt; ///////////////
	while(cnt>0)
	{	
		cnt--;
		in >> R >> K >> N; ///////////////
		while(N>0)
		{
			in >> temp;/////////////
			q1.push(temp);
			N--;
		}
		//��ʼ���㣬�����
		total=0;
		out << "Case #" << case_num++ << ": ";//////////////
		while(R>0)
		{
			R--;
			temp=0;
			while(!q1.empty())
			{
				if(temp+q1.front()<=K) //�����ϳ�
				{
					temp+=q1.front();
					q2.push(q1.front());
					q1.pop();
				}
				else
					break;
			}
			//����һ�Σ��������Ŷӣ���������
			while(!q2.empty())
			{
				q1.push(q2.front());
				total+=q2.front();
				q2.pop();
			}
		}
		out << total << endl;////////////////
		//���q1
		while(!q1.empty())
			q1.pop();
	}
	return 0;
}