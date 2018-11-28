#include <fstream>
#include <iostream>
using namespace std;

int num[1000];

int add_bin(int a, int b);

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	int cnt;
	fin >> cnt;
	int caseNum=0;
	while(cnt-- > 0)
	{
		int N;
		fin >> N;
		int sum_bin=0;
		for(int i=0;i<N;i++)
		{
			fin >> num[i];
			sum_bin=add_bin(sum_bin, num[i]);
		}
		fout << "Case #" << ++caseNum << ": ";
		if(sum_bin!=0)
			fout << "NO" << endl;
		else
		{
			int sum=0;
			int min=1000001;
			for(int i=0;i<N;i++)
			{
				sum+=num[i];
				if(min>num[i])
					min=num[i];
			}
			fout << sum-min << endl;
		}
	}
}

int add_bin(int a, int b)
{
	int base=1;
	int s1,s2,s;
	int sum_b=0;
	while(a!=0 || b!=0)
	{
		s1=a-(a>>1<<1);
		s2=b-(b>>1<<1);
		if(s1==1 && s2==1)
			s=0;
		else
			s=s1+s2;
		if(s!=0)
			sum_b+=base;
		base=base << 1;
		a=a>>1;
		b=b>>1;
	}
	return sum_b;
}