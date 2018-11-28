//Jakub Sygnowski
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
//#include<gmp.h> // http://gmplib.org/
//#include<gmpxx.h>
using namespace std;
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define F first
#define S second
#define INF 1000000007
#define PB push_back
#define MP make_pair
typedef pair<int,int> PII;
typedef long long LL;

int t,n;
vector<string> klej;
char kloca(char a,char b){
	REP(i,klej.size()){
		if ((a==klej[i][0] && b==klej[i][1])|| ( a==klej[i][1] && b==klej[i][0]))
			return klej[i][2];
	}
	return 0;
}
vector<string> zabij;
bool bardzo(char a,char b){
	REP(i,zabij.size()){
		if ((a==zabij[i][0] && b==zabij[i][1]) || (a==zabij[i][1] && b==zabij[i][0])){
			return true;
		}
	}
	return false;
}
string res;
void wrzuc(char x){
	res.PB(x);
	while(res.size()>1 && kloca(res[res.size()-1],res[res.size()-2])){
		res[res.size()-2]=kloca(res[res.size()-1],res[res.size()-2]);
		res.erase(res.begin()+(res.size()-1));
	}
	REP(i,res.size()){
		if (res.size()>1 && bardzo(res[i],res[res.size()-1]))
			res.clear();
	}
}
void wypisz(){
	printf("[");
	REP(i,(int)(res.size())-1){
		printf("%c, ",res[i]);
	}
	if (res.size())
		printf("%c",res[res.size()-1]);
	printf("]\n");
}
string lista;
char tb[107];
int main(){
	scanf("%d",&t);
	REP(nr,t){
		printf("Case #%d: ",nr+1);
		klej.clear(); zabij.clear(); res.clear(); lista.clear();
		scanf("%d",&n);
		while(n--){ scanf("%s",tb); klej.PB((string)(tb)); }
		scanf("%d",&n);
		while(n--){
			scanf("%s",tb); zabij.PB((string)(tb));
		}
		scanf("%d",&n); scanf("%s",tb); lista=tb;
		REP(i,n) wrzuc(lista[i]);
		wypisz();
	}
}
