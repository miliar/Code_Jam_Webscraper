#include <iostream>
#include <algorithm>
#include <string>
#include <math.h>
#include <fstream>
using namespace std;
#define fon(i,n) for(i=0;i<n;++i)
#define re return
#define ll long long
const double EPS = 1E-9;const int INF = 1000000000;const ll INF64 = (ll)1E18;const double PI = 3.1415926535897932384626433832795;

ll x,y;
typedef struct{ll l,r,d;}tpo;

int main()
{
	#ifndef ONLINE_JUDGE
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	#endif

	ll i,j,n,m,T,t,k;
	
	string s[5]={""};bool bEmpty,bWin,iWin;
	cin>>T;
	for(t=0;t<T;++t){
		for(j=0;j<4;++j)cin>>s[j];
		bEmpty=false;bWin=false;
		for(i=0;i<4;++i){
			for(j=0,k=0;j<4;++j)if(s[i][j]=='O'||s[i][j]=='T')++k;
			if(k==4){bWin=true;iWin=0;}
			for(j=0,k=0;j<4;++j)if(s[j][i]=='O'||s[j][i]=='T')++k;
			if(k==4){bWin=true;iWin=0;}
			for(j=0,k=0;j<4;++j)if(s[i][j]=='X'||s[i][j]=='T')++k;
			if(k==4){bWin=true;iWin=1;}
			for(j=0,k=0;j<4;++j)if(s[j][i]=='X'||s[j][i]=='T')++k;
			if(k==4){bWin=true;iWin=1;}
			for(j=0,k=0;j<4;++j)if(s[i][j]=='.')bEmpty=true;
		}for(j=0,k=0;j<4;++j)if(s[j][j]=='O'||s[j][j]=='T')++k;
		if(k==4){bWin=true;iWin=0;}
		for(j=0,k=0;j<4;++j)if(s[j][3-j]=='O'||s[j][3-j]=='T')++k;
		if(k==4){bWin=true;iWin=0;}
		for(j=0,k=0;j<4;++j)if(s[j][j]=='X'||s[j][j]=='T')++k;
		if(k==4){bWin=true;iWin=1;}
		for(j=0,k=0;j<4;++j)if(s[j][3-j]=='X'||s[j][3-j]=='T')++k;
		if(k==4){bWin=true;iWin=1;}
		cout<<"Case #"<<t+1<<": ";
		if(bWin){
			if(iWin){cout<<"X won"<<endl;}
			else{cout<<"O won"<<endl;}
		}else if(bEmpty){cout<<"Game has not completed"<<endl;}
		else {cout<<"Draw"<<endl;}
	}
	re 0;
}