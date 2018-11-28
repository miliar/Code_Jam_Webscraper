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
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

bool isPrime(int liczba){
	if( liczba == 2 ) return true;
	if( liczba %2 == 0 ) return false;
	for(int b=3; b*b<=liczba; b+=2) if( liczba % b == 0 ) return false;
	return true;
}

int ileTestow, a, b, p;

int main(){
	
	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		scanf("%d%d%d",&a,&b,&p);

		vi prime; prime.clear();

		for(int i=p; i<=b; i++) if( isPrime(i) ) prime.pb(i);
		
		int t[10000];
		for(int i=a; i<=b; i++) t[i] = i;


		for(int i=0; i<prime.sz; i++) for(int w=a; w<=b; w++) for(int e=w+1; e<=b; e++) if( w>=prime[i]&& e>=prime[i] && w%prime[i]==0 && e%prime[i]==0 ){
			int temp=t[e];
			for(int r=a; r<=b; r++) if( t[r] == temp ) t[r] = t[w];
		}

		vi res; res.clear();
		for(int i=a; i<=b; i++){
			res.pb( t[i] );
		}
		sort(ALL(res));

		int score = 0, temp=-1;
		fu(i,res.sz) if( res[i] != temp ){
			score++;
			temp=res[i];
		}
		

		printf("Case #%d: %d\n",q,score);
	}

	return 0;
}
