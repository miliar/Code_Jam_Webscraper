//This code was writen by Alexander Dryapko (sdryapko)
#include<sstream>
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>                             	
#include<set>               
#include<string>
#include<string.h>  
#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define pw2(x) (1ll<<(x))
#define F first
#define S second
const int maxi=2000000000;              
const int maxq=1000000000;
const double eps=1e-10;       
const double pi=3.1415926535897932;
const double inf=1e+18;
const int mo=1000000007;

using namespace std;
char a[55][55];             
int tt,xp[8]={1,1,1,-1,-1,-1,0,0};
int    yp[8]={0,1,-1,0,1,-1,1,-1};
int kol(int x,int y,int k,char ch) {
        int sum=0;
	while (a[x][y]==ch) sum++,x+=xp[k],y+=yp[k];
	return sum;
}
bool win(char ch) {
	for (int i=1;i<=4;i++) for (int j=1;j<=4;j++) for (int k=0;k<8;k++) if (a[i][j]==ch&&kol(i,j,k,a[i][j])==4) return 1;
	return 0;
}
bool check(char ch) {
	vector<pair<int,int> > v;
	v.clear();
	for (int i=1;i<=4;i++) for (int j=1;j<=4;j++) if (a[i][j]=='T') {
		a[i][j]=ch;
		v.push_back(make_pair(i,j));
	}
	bool f=win(ch);
	for (int i=0;i<v.size();i++) a[v[i].F][v[i].S]='T';
	return f;
}

int main(){                 
        freopen("input.txt","r",stdin);      
        freopen("output.txt","w",stdout); 
       	cin>>tt;
       	scanf("\n");
       	for (int t=1;t<=tt;t++) {
       		printf("Case #%d: ",t);
       		for (int i=1;i<=4;i++) {
       			for (int j=1;j<=4;j++) scanf("%c",&a[i][j]);
       			scanf("\n");
       	        }
       	        scanf("\n");
       	        int kol=0;
       	        for (int i=1;i<=4;i++) for (int j=1;j<=4;j++) if (a[i][j]=='.') kol++;
       	        if (check('X')) puts("X won"); else 
       	        if (check('O')) puts("O won"); else 
       	        if (kol==0) puts("Draw"); else puts("Game has not completed");
       	}
       	return 0;
}
