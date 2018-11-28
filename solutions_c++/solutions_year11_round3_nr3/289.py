#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;

const int MAX = 10000;

#define MAXN 10001

ifstream fin("C-small-attempt2.in");
ofstream fout("C-small-attempt2.out");

bool used[MAXN];
int n,l,h;
int num[MAXN];

int Judge()
{
	for(int i=l;i<=h;i++)
	{
		bool flag=false;
		for(int j=0;j<n;j++)
		{
			if(!(i%num[j]==0||num[j]%i==0))
			{
				flag=true;
				break;
			}
		}
		if(!flag)
			return i; 
	}
	return 0;
}
int main()
{
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		fin>>n>>l>>h;
		int tem;
		for(int j=0;j<n;j++)
		{
			fin>>num[j];
		}
		fout<<"Case #"<<i<<": ";
		tem=Judge();
		if(!tem)
			fout<<"NO";
		else
			fout<<tem;
		fout<<endl;
	}
	return 0;
}
