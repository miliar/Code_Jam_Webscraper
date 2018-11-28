#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
using namespace std;

#define make(n) int n;scanf("%d",&n)
#define FOR(i,j,k) for(int i=j;i<k;i++)
#define FORD(i,j,k) for(int i=j-1;i>=k;i--)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define ret return
#define ll long long
#define INF 2000000001
#define N 1000001
#define INFLL INF*INF
#define vi vector<int>
#define pii pair<int,int>

//stale

//struktury

//funckje
char tab[4][4];
bool kropka;
string slowo[10];
bool O, X;

bool wygra(int i,char c){
	int wyn=0;

	FOR(j,0,4){
		if(slowo[i][j]=='.')kropka=1;
		if(slowo[i][j]==c||slowo[i][j]=='T')wyn++;
	}

	if(wyn==4)ret 1;
}

int main(){
	ios_base::sync_with_stdio(0);

	int Z;
	cin>>Z;

	FOR(dupa,1,Z+1){
		FOR(i,0,10)slowo[i]="";
		O=X=kropka=0;

		FOR(i,0,4)
			FOR(j,0,4)
				cin>>tab[i][j];

		FOR(i,0,4)
			FOR(j,0,4)slowo[i]+=tab[i][j];

		FOR(j,0,4)
			FOR(i,0,4)slowo[j+4]+=tab[i][j];

		FOR(j,0,4)slowo[8]+=tab[j][j];

		FOR(j,0,4)slowo[9]+=tab[j][3-j];

		FOR(i,0,10){
			if(wygra(i,'O'))O=1;
			if(wygra(i,'X'))X=1;
		}

		cout<<"Case #"<<dupa<<": ";

		if(O&&X)cout<<"Draw"<<endl;
		else if(O)cout<<"O won"<<endl;
		else if(X)cout<<"X won"<<endl;
		else if(kropka)cout<<"Game has not completed"<<endl;
		else cout<<"Draw"<<endl;

	}

  ret 0;
}
