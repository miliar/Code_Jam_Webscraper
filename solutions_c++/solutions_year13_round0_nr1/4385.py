/*
 Anton Gulikov
*/
#pragma comment(linker,"/STACK:300000000")
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <stdlib.h>

#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define foru(i,n) for (int i=0;i<(n);i++)
#define ford(i,n) for (int i=(n)-1;i>=0;i--)
#define forab(i,l,r) for (int i=(l);i<=(r);i++)
#define forabd(i,r,l) for (int i=(r);i>=(l);i--)
#define fillchar(a,b) memset((a),(b),sizeof((a)))
#define pb push_back
#define F first
#define S second
#define all(x) x.begin,x.end
#define pw2(x) (1ull<<(x))
#define mp make_pair

const long double eps=1e-20;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

map <char,int> kol;
string s[4];
char sx,so;
int t,k2;
bool was[5][5];

int main(){
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	scanf("%d",&t);
	sx='X';
	so='O';
	forab(tt,1,t){
		printf("Case #%d: ",tt);
		foru(i,4) cin>>s[i];
		k2=0;
		foru(i,4)foru(j,4) k2+=s[i][j]=='.';
		foru(i,4)foru(j,4) was[i][j]=false;
		foru(i,4)foru(j,4) was[i][j]=s[i][j]=='T';
		foru(i,4)foru(j,4) if (was[i][j]) s[i][j]='X';
		kol['X']=0; kol['O']=0;
		foru(i,4){
			if (s[i][0]==sx && s[i][1]==sx && s[i][2]==sx && s[i][3]==sx) kol['X']++;
			if (s[0][i]==sx && s[1][i]==sx && s[2][i]==sx && s[3][i]==sx) kol['X']++;
		}
		if (s[0][0]==sx && s[1][1]==sx && s[2][2]==sx && s[3][3]==sx) kol['X']++;
		if (s[0][3]==sx && s[1][2]==sx && s[2][1]==sx && s[3][0]==sx) kol['X']++;
		foru(i,4)foru(j,4) if (was[i][j]) s[i][j]='O';
		foru(i,4){
			if (s[i][0]==so && s[i][1]==so && s[i][2]==so && s[i][3]==so) kol['O']++;
			if (s[0][i]==so && s[1][i]==so && s[2][i]==so && s[3][i]==so) kol['O']++;
		}
		if (s[0][0]==so && s[1][1]==so && s[2][2]==so && s[3][3]==so) kol['O']++;
		if (s[0][3]==so && s[1][2]==so && s[2][1]==so && s[3][0]==so) kol['O']++;
		if (kol['X']>0) cout<<"X won"<<endl; else
		if (kol['O']>0) cout<<"O won"<<endl; else
		if (k2>0) cout<<"Game has not completed"<<endl; else
		cout<<"Draw"<<endl;
	}
	return 0;
}