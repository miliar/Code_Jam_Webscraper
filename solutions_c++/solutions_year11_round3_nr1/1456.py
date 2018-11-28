#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
int dx[8]= { 0,1,1,1,0,-1,-1,-1},dy[8]={1,1,0,-1,-1,-1,0,1};
vector<string> v;

int main()
	{
	   int t,r,c,x=1;
	   string s;
	   for(cin>>t;t>0;t--)
	   {
		v.clear();
		scanf("%d %d\n",&r,&c);
		for(int i=0;i<r;i++) getline(cin,s) , v.push_back(s);	
		//for(int i=0;i<r;i++) cout<<v[i]<<endl;
		for(int i=0;i+1<r;i++)
		 for(int j=0;j+1<c;j++)
		   {	
			if(v[i][j]=='#' && v[i][j+1]=='#' && v[i+1][j]=='#' && v[i+1][j+1]=='#') 
			   v[i][j]='/',v[i][j+1]='\\',v[i+1][j]='\\',v[i+1][j+1]='/';

		   }
		printf("Case #%d:\n",x++);
		bool f=1;
		for(int i=0;i<r;i++) for(int j=0;j<c;j++) if(v[i][j]=='#') f=0;
		if(f==0) { printf("Impossible\n"); continue;}
		else
		{
			for(int i=0;i<r;i++)
			 cout<<v[i]<<endl;

		}
	   }
	}
