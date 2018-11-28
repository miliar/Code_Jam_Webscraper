#include <string>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int e;
//char s[505];
string s;
int dp[505][20];
string w;

int f (int x,int y)
{
	if(dp[x][y]!=-1)
		return dp[x][y];
	
	if(y==w.size ())
		return dp[x][y]=1;
	if(x==e)
		return 0;
	
	dp[x][y]=f (x+1,y);
	
	if(w[y]==s[x])
	{
		dp[x][y]=(dp[x][y]+f (x+1,y+1))%10000;
	}
	return dp[x][y];
}

int main ()
{
	FILE *fin,*fout;
	fin=freopen ("Welcome to Code Jam.in","r",stdin);
	fout=freopen ("Welcome to Code Jam.out","w",stdout);
	
	int N,n;
	fscanf (fin,"%d\n",&N);
	
	w="welcome to code jam";
	
	
	for(n=1;n<=N;n++)
	{
//		fscanf (fin,"%[^\n]s",&s);
		getline (cin,s);
		e=s.size ();
		memset (dp,-1,sizeof dp);
		fprintf (fout,"Case #%d: %04d\n",n,f (0,0));
	}
	return 0;
}
