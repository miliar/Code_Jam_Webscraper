//SORU
//PROGRAM C++

/*
	ID: semihbasrik
	LANG: C++
	TASK:
*/
#include<iostream>
#include<fstream>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<list>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<climits>
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define wait system("pause");
#define lint long long int
#define ABS(a)	 ( (a)>0 ? (a) : -(a) )
#define KARE(a)	 ( (a)*(a) )
#define MAX(a,b) ( (a)>(b) ? (a) : (b) )
#define MIN(a,b) ( (a)<(b) ? (a) : (b) )
#define INF		 INT_MAX
#define MX		 2000005
#define cin fin
#define cout fout
using namespace std;
ifstream fin("C-large.in");
ofstream fout("C-large.out");

map< pair<int,int> , bool >MP;
lint BAS[MX],T,A,B;
string str;

void bas(){
	lint i,j,s=0;
	for(j=1;j<=7;j++){
		for(i=s+1,s=s*10+9;i<MX && i<=s;i++)
			BAS[i]=j;
	}
}

string str_cevir(lint x){
	string temp="";
	while(x){
		temp=(char)( '0' + x%10 ) + temp;
		x/=10;
	}
	return temp;
}

lint sayi_cevir(lint b,lint s){
	lint res=0;
	for(;b<=s;b++){
		res*=10;
		res+=str[b]-'0';
	}
	return res;
}

void solve(lint k){
	MP.clear();
	lint i,j,t,res=0;
	for(i=A;i<=B;i++){
		str=str_cevir(i);
		str+=str;
		for(j=0;j<str.size()/2;j++){
			t=sayi_cevir( j,j+BAS[i]-1 );
			if( t<i && t>=A && MP[ mp(t,i) ]==0){
				MP[ mp(t,i) ]=1;
				res++;
			}
		}
	}
	cout<<"Case #"<<k<<": "<<res<<endl;
}

void read(){
	lint i;
	cin>>T;
	for(i=1;i<=T;i++)
		cin>>A>>B,solve(i);
//	wait;
}

int main(){
	bas();
	read();
}
