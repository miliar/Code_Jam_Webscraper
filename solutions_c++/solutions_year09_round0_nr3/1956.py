//Jakub Sygnowski
#include <cstdio>
#include <iostream>
#include <string>
#define REP(I,N) for(int I=0;I<(N);I++)
using namespace std;
int res[508][20];
string ciag;
char tab[508];
string wel;
int n;
int main(){
	wel="welcome to code jam";
	cin.getline(tab,1024);
	ciag=tab;
	while(ciag.size()){
		n*=10;
		n+=ciag[0]-'0';
		ciag.erase(ciag.begin());
		//printf("a");
	}
	REP(nr,n){
		cin.getline(tab,1024);
		ciag=tab;
		REP(i,ciag.size()+1)
			REP(k,wel.size()+1)
				res[i][k]=0;
		REP(i,ciag.size()) res[i][0]=1;
	//	REP(k,wel.size()+1){ REP(i,ciag.size()+1) printf("%d ",res[i][k]); printf("\n");}
	//	return 0;
		REP(i,ciag.size()){
			REP(k,wel.size()){
				if (ciag[i]==wel[k]){
					res[i+1][k+1]+=res[i][k];
					res[i+1][k+1]%=1000;
				}
				res[i+1][k+1]+=res[i][k+1];
			}
		}
	//	REP(k,wel.size()+1){ REP(i,ciag.size()+1) printf("%d ",res[i][k]); printf("\n");}
		printf("Case #%d: ",nr+1);
		if (res[ciag.size()][wel.size()]<1000) printf("0");
		if (res[ciag.size()][wel.size()]<100) printf("0");
		if (res[ciag.size()][wel.size()]<10) printf("0");
		printf("%d\n",res[ciag.size()][wel.size()]);
	}
}
