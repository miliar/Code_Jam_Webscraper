//Code Jam 2011
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <complex>
#include <iostream>
#include <cmath>
#include <utility>
#include <ctype.h>
#include <cstring>
#include <string>
#include <cassert>
#include <queue>
#include <map>
#include <set>
#include <complex>
using namespace std;

#define REP(_i, _N) for(_i=0;_i<_N;_i++)
#define REC(_i, _N) for(_i=1;_i<=_N;_i++)
#define PF printf
#define SF scanf
#define LIMPIA(_a) memset((_a), 0, sizeof(_a))
#define ANULA(_a) memset((_a), -1, sizeof(_a))

typedef long long ll;
const double EPS=1e-9;
const int INF=1000000000;

int T, N;
int LibreO, LibreB;
int PO, PB;

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h;
	int caso;
	int r=0;
	int dist;
	int aumento;
	SF("%d", &T);
	REC(caso, T){
		LibreO=0;
		LibreB=0;
		PO=1;
		PB=1;
		r=0;
		SF("%d", &N);
		char Robot[5];
		REP(i, N){
			SF("%s %d", Robot, &k);
			if(Robot[0]=='O'){
				dist=abs(k-PO);
				if(dist<=LibreO){
					aumento=1;
				}else{
					aumento=dist-LibreO+1;
				}
				LibreO=0;
				LibreB+=aumento;
				PO=k;
			}else if(Robot[0]=='B'){
				dist=abs(k-PB);
				if(dist<=LibreB){
					aumento=1;
				}else{
					aumento=dist-LibreB+1;
				}
				LibreB=0;
				LibreO+=aumento;
				PB=k;
			}
			r+=aumento;
		}
		printf("Case #%d: %d\n", caso, r);
	}
	return 0;
}
