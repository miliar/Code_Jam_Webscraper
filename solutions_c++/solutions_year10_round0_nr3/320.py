#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int gr[1200];
ll sum[1200];
int to[1200];
int step[1200];
ll am[1200];
ll R;
int K,N;
int inc(int id){return ((id==N-1)?0:id+1);}
int dec(int id){return ((id==0)?N-1:id-1);}
ll size(int a, int b){
	if(a>=b)return sum[b]+sum[N]-sum[a];
	else return sum[b]-sum[a];
}
int main(){
	int tcam;
	cin >> tcam;
	FOR(tnr,1,tcam+1){
		cin >> R >> K >> N;
		FOR(i,0,N)cin >> gr[i];
		sum[0]=0;
		FOR(i,0,N)sum[i+1]=sum[i]+gr[i];
		int currto = 1;
		ll amount = 0;
		if(sum[N]<=K){
			amount = R*sum[N];
		} else {
			FOR(i,0,N){
				if(currto==i)currto = inc(currto);
				while(size(i,currto)<=K){
					currto = inc(currto);
				}
				currto = dec(currto);
				to[i]=currto;
			}
			memset(step,-1,sizeof(step));
			int curr = 0;
			step[0]=0;
			am[0]=0;
			while(R!=0){
				if(step[to[curr]]!=-1){
					ll diff = am[curr]-am[to[curr]]+size(curr,to[curr]);
					int anz = step[curr]-step[to[curr]]+1;
					ll mult = R/anz;
					amount += diff*mult;
					R -= mult * anz;
					memset(step,-1,sizeof(step));
					step[curr]=0;
					am[curr]=0;
				} else {
					--R;
					step[to[curr]]=1+step[curr];
					am[to[curr]]=am[curr]+size(curr,to[curr]);
					amount += size(curr,to[curr]);
					curr = to[curr];
				}
			}
		}
			cout << "Case #" << tnr << ": " << amount << endl;
	}
	return 0;
}
