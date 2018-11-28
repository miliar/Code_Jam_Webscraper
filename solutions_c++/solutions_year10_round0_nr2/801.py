#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int factor(int a,int b)//a,b>=0;
{
	if(a==0)
		return b;
	else if(b==0)
		return a;
	else if(a>=b)
		return factor(a%b,b);
	else return factor(a,b%a);
}

int main()
{
	int C;
	int i;
	int N;
	int t1;
	int t2;
	int t3;
	int T;
	int temp;
	ifstream fin("B-small-attempt1.in");
	ofstream fout("small-ans.txt");
	fin>>C;
	for(i=1;i<=C;i++)
	{
		fin>>N;
		fout<<"Case #"<<i<<": ";
		if(N==2)
		{
			fin>>t1;
			fin>>t2; 
			T=abs(t2-t1);
			if(T==0)
				fout<<0<<"\n";
				else
				{
					temp=t1%T;
					if(temp==0)
						fout<<0<<"\n";
					else
						fout<<(T-temp)<<"\n";
				}
		}
		else if(N==3)
		{
			fin>>t1;
			fin>>t2;
			fin>>t3;
			T=factor(abs(t2-t1),abs(t3-t1));
			if(T==0)
				fout<<0<<"\n";
				else
				{
					temp=t1%T;
					if(temp==0)
						fout<<0<<"\n";
					else
						fout<<(T-temp)<<"\n";
				}
		}
	}
	return 0;
}