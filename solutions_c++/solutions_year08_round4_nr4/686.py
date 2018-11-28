/*
	Author : Vinay Emani
	Contact : VinayEmani AT gmail DOT com
*/
#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <utility>
using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define PB push_back
#define MP make_pair
#define FORN(i,a,b) for(i=(int)(a);i<(int)(b);i++)
#define FOR(i,n) FORN(i,0,n)
#define FOREACH(it,S) for(typeof(S.begin()) it = S.begin();it != S.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define BEG(a) a.begin()
#define END(a) a.end()
#define ALL(a) BEG(a),END(a)

string s;
int K;
int main(){
	int cas,T=0;
	cin >> cas;
	while(cas--){
		T++;
		cin >> K >> s;
		int t[6],i;
		FOR(i,K)t[i]=i;
		int ans = 1<<23;
		do{
			string s2 = s;
			int j,sz = SZ(s),k;
			FOR(j,sz/K){
				FOR(k,K)
					s2[j*K+k]=s[j*K+t[k]];
			}
			int sz2=0;
			FOR(j,sz)if(j==0 || s2[j]!=s2[j-1])sz2++;
			ans=min(ans,sz2);
		}while(next_permutation(t,t+K));
		cout << "Case #" << T << ": " << ans << endl;
	}
	return 0;
}
