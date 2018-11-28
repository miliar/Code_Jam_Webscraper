#include<string>
#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

const int Max = 500;
const string Str = "welcome to code jam";

ifstream fin("qualround3.in");
ofstream fout("qualround3.out");
int N;
string str;
int rec[256][10], count1[256];
int ans[Max][20];

int main()
{
	fin >>N;
	for (int i=0;i<Str.size() ;i++ )
	{
		rec[Str[i]][count1[Str[i]]++] = i;
	}
	getline(fin, str);
	for (int i=1;i<=N ;i++ )
	{
		getline(fin, str);
		memset(ans,0 ,sizeof(ans));
		for (int j=0;j<str.size();j++)
		{
			char c = str[j];
			for (int k=0;k<count1[c];k++)
			{
				int p = rec[c][k];
				if (p==0)
				{
					ans[j][p] = 1;
				}
				else
				{
					for (int q = 0;q<j ;q++ )
					{
						ans[j][p]+= ans[q][p-1];
					}
					ans[j][p]%=10000;
				}
			}
		}
		int a= 0;
		for (int j=0;j<str.size() ;j++ )
		{
			a += ans[j][18];
		}
		a%=10000;
		fout<<"Case #"<<i<<": "<<a/1000<<(a%1000)/100<<(a%100)/10<<a%10<<endl;
	}
	return 0;
}
