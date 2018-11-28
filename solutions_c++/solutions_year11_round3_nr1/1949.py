#include<iostream>
#include<cstdio>
#include<cmath>
#include <fstream>
using namespace std;
ifstream fin("D:\\acm\\a\\A-large.in");
ofstream fout("D:\\acm\\a\\A-large.out");
 
#define cin fin
#define cout fout

int main()
{
	int t,r,c,i,j,out;
	int i1,j1;
	int b[51][51];
	int temp;
	char a[51][51];
	cin>>t;
	temp=1;
	while(t--)
	{
		out=1;
	   cin>>r>>c;
		for(i=0;i<r;i++){
			cin>>a[i];
			
		}
		memset(b,0,sizeof(b));

		for(i=0;i<r-1;i++){
			for(j=0;j<c/2*2;j++){
				if(a[i][j]=='#' && b[i][j]==0){
					if(a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#'){
						i1=i+1;j1=j+1;
						a[i][j]='/';
						a[i][j1]='\\';
						a[i1][j]='\\';
						a[i1][j1]='/';
						b[i][j]=b[i][j+1]=b[i+1][j]=b[i+1][j+1]=1;
						j=j+1;
					}
				}
			}
		}
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				if(a[i][j]=='#'){
					out=0;
					break;
				}
			}
		}
		cout<<"Case #"<<temp++<<":"<<endl;

		if(out==0)
			cout<<"Impossible"<<endl;
		else
		{
			for(i=0;i<r;i++){
				for(j=0;j<c;j++){
					cout<<a[i][j];			
				}
			cout<<endl;
			}
			cout<<endl;
		}
	}
	return 0;
}