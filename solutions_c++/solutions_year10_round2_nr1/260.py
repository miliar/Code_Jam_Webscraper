#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream dat ("a.in");
ofstream sol ("a.out");

string a[1001][1001];
int c[1001];
int b[1001][1001];

int n,m,k;

int ok(char ch)
{
	if((ch>='a' && ch<='z')||(ch>='0' && ch<='9')) return 1;
	return 0;
}
int Find(string s,int r)
{
	int i;
	for(i=0;i<c[r];i++)
		if (a[r][i]==s) return b[r][i];
	return 0;
}
int main()
{
	int p,t,i,j,l;
	dat >> t;
	string s,st="";
	k=0;
	int tt,pos=0,pop=0;
	for(p=1;p<=t;p++)
	{
		dat >> n >>m;
		k=0;
		for(j=0;j<1000;j++) c[j]=0;
		for(i=0;i<n;i++)
		{			
			dat >> s;
			s=s+'/';
			l=s.length();
			j=0;	
			pop=0;
			while (j<l-1)
			{
				j++; st="";
				while (ok(s[j])) { st=st+s[j]; j++; }
				pos=Find(st,pop);				
				if (pos==0)
				{
					a[pop][c[pop]]=st;
					k++;
					b[pop][c[pop]]=k;
					c[pop]++;	
					pop=k;
				}else pop=pos;				
			}
		}
		int res=0;
		for(i=0;i<m;i++)
		{
			dat >> s;
			s=s+'/';
			l=s.length();
			j=0; pop=0;
			while (j<l-1)
			{
				j++; st="";
				while (ok(s[j])) { st=st+s[j]; j++; }
				pos=Find(st,pop);				
				if (pos==0)
				{
					a[pop][c[pop]]=st;
					k++;
					b[pop][c[pop]]=k;
					c[pop]++;					
					res++;
					pop=k;
				} else	pop=pos;
			}

		}
		sol << "Case #" << p << ": ";
		sol << res;
		sol << endl;
	}
	return 0;
}