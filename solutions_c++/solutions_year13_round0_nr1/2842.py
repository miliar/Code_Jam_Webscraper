#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	freopen("aaa.in","r",stdin);
	freopen("aaa.txt","w",stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		char tm;
		int x[4][4],o[4][4];
		memset(x,0,sizeof(x));
		memset(o,0,sizeof(o));
		bool fin=1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>tm;
				if(tm=='X') x[i][j]=1;
				else if(tm=='O') o[i][j]=1;
				else if(tm=='T') x[i][j]=o[i][j]=1;
				else fin=false;
				}
			}
		int rowx[4],columnx[4],rdx=0,ldx=0;
		memset(rowx,0,sizeof(rowx));
		memset(columnx,0,sizeof(columnx));
		int rowo[4],columno[4],rdo=0,ldo=0;
		memset(rowo,0,sizeof(rowo));
		memset(columno,0,sizeof(columno));
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(x[i][j]==x[i][0] && x[i][j]==1) rowx[i]++;
				if(x[j][i]==x[0][i] && x[j][i]==1) columnx[i]++;
				if(o[i][j]==o[i][0] && o[i][j]==1) rowo[i]++;
				if(o[j][i]==o[0][i] && o[j][i]==1) columno[i]++;
			}
			if(x[i][i]==x[0][0] && x[0][0]==1) rdx++;
			if(x[i][3-i]==x[3][0] && x[3][0]==1) ldx++;
			if(o[i][i]==o[0][0] && o[0][0]==1) rdo++;
			if(o[i][3-i]==o[3][0] && o[3][0]==1) ldo++;
		}
		bool ok=false;;
		for(int i=0;i<4;i++)
		{
			if(rowx[i]==4) {cout<<"Case #"<<tt<<": X won"<<endl;ok=true;break;}
			else if(columnx[i]==4) {cout<<"Case #"<<tt<<": X won"<<endl;ok=true;break;}
			else if(rowo[i]==4) {cout<<"Case #"<<tt<<": O won"<<endl;ok=true;break;}
			else if(columno[i]==4) {cout<<"Case #"<<tt<<": O won"<<endl;ok=true;break;}
		}
		if(ok) continue;
		if(rdx==4) {cout<<"Case #"<<tt<<": X won"<<endl;continue;}
		else if(ldx==4) {cout<<"Case #"<<tt<<": X won"<<endl;continue;}
		else if(rdo==4) {cout<<"Case #"<<tt<<": O won"<<endl;continue;}
		else if(ldo==4) {cout<<"Case #"<<tt<<": O won"<<endl;continue;}
		if(fin) {cout<<"Case #"<<tt<<": Draw"<<endl;}
		else 
		{cout<<"Case #"<<tt<<": Game has not completed"<<endl;}
	}
	return 0;
}
