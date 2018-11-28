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

int seq[2000];
bool rob[2000];
int next[2][2000];
char buf[2000];
int main(){
	int T,N;
	scanf("%d",&T);
	FOR(tc,1,T+1){
		scanf("%d",&N);
		FOR(i,0,N){
			scanf("%s%d",buf,seq+i);
			rob[i]=(buf[0]=='B');
		}
		next[0][N]=next[1][N]=-1;
		FORD(i,0,N){
			next[0][i]=next[0][i+1];
			next[1][i]=next[1][i+1];
			if(rob[i]){
				next[0][i]=seq[i];
			} else {
				next[1][i]=seq[i];
			}
		}
		int p1 = 1, p2 = 1;
		int steps = 0;
		FOR(i,0,N){
			if(rob[i]){
				int dis = abs(p1-seq[i])+1;
				p1 = seq[i];
				steps+=dis;
				if(abs(p2-next[1][i])<=dis){
					p2=next[1][i];
				} else {
					if(p2<next[1][i])p2+=dis;
					else p2-=dis;
				}
			} else {
				int dis = abs(p2-seq[i])+1;
				p2=seq[i];
				steps+=dis;
				if(abs(p1-next[0][i])<=dis){
					p1=next[0][i];
				} else {
					if(p1<next[0][i])p1+=dis;
					else p1-=dis;
				}
			}
		}
		cout << "Case #"<< tc<<": "<<steps<<endl;
	}
	return 0;
}
