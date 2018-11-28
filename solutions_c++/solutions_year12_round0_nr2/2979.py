#include <iostream>
#include <fstream>
using namespace std;

const int MAX = 105;
typedef struct _node
{
	int max, flag;//flag_剩余可以增加数
}N;

N people[MAX];

int countMax(int can, int n, int hig)
{
	int cnt = 0;
	for(int i = 0; i < n; i++)
	{
		if(people[i].max >= hig)
			cnt++;
		else if(can > 0 && people[i].flag == 0 && people[i].max + 1 == hig)
		{
			cnt++;
			can--;
		}
	}
	return cnt;
}

int main(void)
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int cas, cas_c = 1;
	fin >> cas;
	while(cas--)
	{
		int num, sur, hig;
		fin >> num >> sur >> hig;
		for(int i = 0; i < num; i++)
		{
			int tolSor, rem;
			fin >> tolSor;
			if(tolSor == 0)
			{
				people[i].flag = 1;
				people[i].max = 0;
				continue;
			}
			rem = tolSor % 3;
			if(rem == 0)//三个相等
			{
				people[i].flag = 0;//可改
				people[i].max = tolSor / 3;
			}
			else if(rem == 1)
			{
				people[i].flag = 1;//不可改
				people[i].max = tolSor / 3 + 1;
			}
			else if(rem == 2)
			{
				people[i].flag = 0;
				people[i].max = tolSor / 3 + 1;
			}
		}
		fout << "Case #" << cas_c++ << ": ";
		fout << countMax(sur, num, hig) << endl;
	}
	return 0;
}


