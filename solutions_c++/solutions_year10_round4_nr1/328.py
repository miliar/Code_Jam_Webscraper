#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;
int k, tab[200][200];
int tmp[200][200];

bool is_ok(int rozmiar){
//	cerr << "## rozmiar: " << rozmiar << endl;
//	fu(a,rozmiar){ fu(b,rozmiar) cerr << tmp[a][b] << " "; cerr << endl; }
//	cerr << "##### " << endl;
	fu(a,rozmiar){
		for(int b=1; b<=a; b++){
//cerr << "#1 " << a+b << " : " << a-b << " | " << a-b << " : " << a+b << " # " << tmp[a+b][a-b] << " : " << tmp[a-b][a+b] << endl;
			if( tmp[a+b][a-b] != -1 && tmp[a-b][a+b] != -1 && tmp[a+b][a-b] != tmp[a-b][a+b] ) return false;
//cerr << "#2 " << a+b-1 << " : " << a-b << " | " << a-b << " : " << a+b-1 << " # " << tmp[a+b-1][a-b] << " : " << tmp[a-b][a+b-1] << endl;
			if( tmp[a+b-1][a-b] != -1 && tmp[a-b][a+b-1] != -1 && tmp[a+b-1][a-b] != tmp[a-b][a+b-1] ){
//					cerr << tmp[a+b-1][a-b] << " " << tmp[a-b][a+b-1]  << endl;
					 return false;
					 }
		}
		int a2 = rozmiar - 1 - a;
		for(int b=1; b<=a; b++){
//cerr << "#12 " << a-b << " : " << a2-b << " | " << a+b << " : " << a2+b << " # " << tmp[a-b][a2-b] << " : " << tmp[a+b][a2+b] << endl;
			if( tmp[a-b][a2-b] != -1 && tmp[a+b][a2+b] != -1 && tmp[a-b][a2-b] != tmp[a+b][a2+b] ) return false;
//cerr << "#22 " << a-b << " : " << a2-b+1 << " | " << a+b-1 << " : " << a2+b << " # " << tmp[a-b][a2-b+1] << " : " << tmp[a+b-1][a2+b] << endl;
			if( tmp[a-b][a2-b+1] != -1 && tmp[a+b-1][a2+b] != -1 && tmp[a-b][a2-b+1] != tmp[a+b-1][a2+b] ) return false;
		}
	}

//	fu(a,rozmiar){ fu(b,rozmiar) cerr << tmp[a][b] << " "; cerr << endl; }

	return true;
}

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
//	cerr << "####" << endl;
		
		memset(tab,-1,sizeof tab);
		
		scanf("%d",&k);

		fu(a,2*k-1){
			if( a < k ){
				fu(b,a+1) scanf("%d",&tab[b][k-a-1+b]);			
			} else {
				fu(b,2*k-a-1) scanf("%d",&tab[b+a-k+1][b]);			
			}
		}
		
		fu(a,2*k){
//			fu(b,2*k) cerr << tab[a][b] << " "; cerr << endl;
//			cerr << endl;
		}

		for(int a=k; a <= k*k ; a++){
			fu(b,a-k+1) fu(c,a-k+1){
				memset(tmp,-1,sizeof tmp);
				fu(d,k) fu(e,k){
					tmp[b+d][c+e] = tab[d][e];
				}
				if( is_ok(a) ){
					printf("%d\n",(a*a) - (k*k));
					goto hell;
				}
			}
		}
		hell:
		
		continue;
	}

	return 0;
}
