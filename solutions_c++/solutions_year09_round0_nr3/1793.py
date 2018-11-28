#include <iostream>
#include <cstring>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define MAX 510
#define MOD 10000
using namespace std;

int n,res,dl;
char txt[MAX];
string pat="welcome to code jam.";

void fun(int lit, int poz,int ilo){
	if(pat[lit]=='.'){
		res+=ilo;
		res%=MOD;
		return;
	} 
	int ilosc=0;
	FOR(i,poz,dl){
		if(txt[i]==pat[lit]) ilosc++;
		if(ilosc>0&&txt[i]==pat[lit+1]){
			fun(lit+1,i,(ilo*ilosc)%MOD);
			ilosc=0;
		}	
	}
}

int main(){
	scanf("%d\n",&n);
	FOR(z,1,n){
		res=0;
		fgets(txt,MAX,stdin);
		dl=strlen(txt);
		txt[dl]='.';
		fun(0,0,1);
		printf("Case #%d: %.4d\n",z,res);
	}
	return 0;
}

