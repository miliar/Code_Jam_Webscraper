/*
 * A.cpp
 *
 *  Created on: 22 mai 2010
 *      Author: Rafael
 */
#include<iostream>
#include<fstream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include <set>
#define FOR(i,n) for(int (i) = 0; i < (n); (i)++)
using namespace std;
#define DEBUG(x) cout << #x" = " << x << "\n"


int toint(char c){
	int n = 0;
	if(c>='A'&&c<='Z')
		n=c-'A'+10;
	else
		n=c-'0';
	return n;
}

int N,M;

int tab[512][512];

void trab(string s, int r){

for(int i=0;i<s.size();i++)
{
	int a = toint(s[i]);
	for(int k = 0; k<4;k++)
		if(a&(1<<(3-k)))
			tab[r][4*i+k]=1;
		else
			tab[r][4*i+k]=0;
}
}



int msq[512][512];

void calc(int a, int b){

	for(int i = a; i>=0; i--)
		for(int j = b; j>=0; j--)
			if(tab[i][j]==1-tab[i+1][j] && tab[i][j]==1-tab[i][j+1] && tab[i][j]==tab[i+1][j+1])
		{
				int m = min(msq[i][j+1],msq[i+1][j+1]);
				m = min(m,msq[i+1][j]);
				msq[i][j] = m+1;
		}else
			msq[i][j]=1;
}

void ini(){
	for(int i = 0;i<M;i++)
		for(int j = 0;j<N;j++)
			msq[i][j]=1;
}

int used[516];

void clean(int a, int b, int l){
	for(int i=a; i< a+l; i++)
		for(int j=b; j< b+l; j++)
			{
			tab[i][j]=-1000;
	//		msq[i][j]=0;
			}
}


void doit(){

int m = min(M,N);
for(int t = m; t >=1; t--)
  used[t]=0;

for(int t = m; t >=1; t--)
	for(int i = 0; i < M-t+1; i++)
		for(int j = 0; j < N-t+1; j++)
			if(msq[i][j]==t&&tab[i][j]!=-1000){
				clean(i,j,t);
				used[t]++;
				calc(i,j+t);
				calc(i+t,j);
			}
}



int main(){
	int T;
	cin>>T;
	for(int t =1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		cin>>M>>N;
		string s;
		for(int i =0; i < M;i++)
		{
			cin>>s;
			trab(s,i);
		}
		ini();

		calc(M-1,N-1);
		doit();

	//	cout<<endl;

/*		FOR(i,M){
		 FOR(j,N)
			cout<<msq[i][j]<<" ";
		 cout<<"\n";
		}
		cout<<endl;
/*		cout<<endl;

		FOR(i,M){
		 FOR(j,N)
			cout<<msq[i][j]<<" ";
		 cout<<"\n";
		}
		cout<<endl;
*/
		int m = min(M,N);
		int ret=0;
		for(int t = m; t >=1; t--)
		  if(used[t])
			  ret++;
		cout<<ret<<endl;

		for(int t = m; t >=1; t--)
		  if(used[t])
			  cout<<t<<" "<<used[t]<<"\n";

		//int ret=0;
//		cout<<"\n";
	}
	return 0;
}
