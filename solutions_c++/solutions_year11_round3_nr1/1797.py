#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;
int main()
{
	int x;
	int y,z,e,f,g;
	double a[100],c[100];
	double b[100],d[100],pri;
	char str[100][100];
	scanf("%d",&x);
	for(int i=1;i<=x;i++)
	{
		g=0;
		cin>>y>>z;
		for(int j=0;j<y;j++)
		{
			cin>>str[j];
		}
		for(int p=0;p<y;p++){
			for(int q=0;q<z;q++)
				if(str[p][q]=='#' &&str[p+1][q]=='#' &&str[p][q+1]=='#' &&str[p+1][q+1]=='#')
				{str[p][q]='/';str[p+1][q]='\\';str[p][q+1]='\\';str[p+1][q+1]='/';}
				else if(str[p][q]=='#') 
					{cout<<"Case #"<<i<<":\nImpossible\n";g=1; break; }
				if(g==1) break;
				}
		if(g!=1){cout<<"Case #"<<i<<":\n";
		for(int p=0;p<y;p++){
			cout<<str[p]<<"\n";}}


		
	}
		
}
