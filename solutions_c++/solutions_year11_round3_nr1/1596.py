#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<iostream>
#include<memory.h>
#include<memory>
using namespace std;
char a[60][60];
int main()
{
	freopen("A-large.in","r",stdin); 
	freopen("A.txt","w",stdout);
	int cas=0;
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		int r,c;
		memset(a,sizeof(a),0);
		scanf("%d %d",&r,&c);
		for(int i=0;i<r;i++) scanf("%s",a[i]);
		for(int i=0;i<r-1;i++)
		for(int j=0;j<c-1;j++)
		{
			if(a[i][j]=='#' && a[i+1][j]=='#' 
			 &&a[i][j+1]=='#' && a[i+1][j+1]=='#')
			{
				a[i][j]='/';
				a[i+1][j]='\\';
				a[i][j+1]='\\';//= =
				a[i+1][j+1]='/';
			}
		}
		bool ok=true;
		for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
		if(a[i][j]=='#') {ok=false; break;}
		
		cout<<"Case #"<<ca<<":"<<endl;
		if(ok==false) cout<<"Impossible"<<endl;
		else 
		for(int i=0;i<r;i++) printf("%s\n",a[i]);
	}
	return 0;
}
