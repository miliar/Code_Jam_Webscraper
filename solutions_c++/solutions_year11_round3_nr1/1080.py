#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string>
#include<map>
using namespace std;

int r,c;

char m[51][51];
int check(int i, int j)
{
	if(i==r-1)return 0;
	if(j==c-1)return 0;
	if(m[i][j+1]!='#') return 0;
	if(m[i+1][j]!='#') return 0;
	if(m[i+1][j+1]!='#') return 0;
	return 1;
}

void solve(int t)
{
int i,j;
cin>>r>>c;
for(i=0;i<r;i++)
cin>>m[i];
int result;

int dontknow=1;
for(i=0;i<r&&dontknow;i++)
for(j=0;j<c;j++)
{
	if(m[i][j]=='#')
	{
		result = check(i,j);
		if(result)
		{
			m[i][j]='/';
			m[i][j+1]='\\';
			m[i+1][j]='\\';
			m[i+1][j+1]='/';
		}
		else
		{
			dontknow=0;
			break;
		}
	}
}
cout<<"Case #"<<t<<":"<<endl;
if(dontknow)
{
for(i=0;i<r;i++)
{
m[i][j]='\0';
printf("%s\n",m[i]);
}
}
else
cout <<"Impossible"<<endl;
}

int main()
{
int i, T;
cin >> T;
for(i=1;i<=T;i++)solve(i);
}
