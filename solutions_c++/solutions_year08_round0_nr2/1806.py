#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <algorithm> 

using namespace std;
typedef long long ll; 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
// abbreviation 
#define all(x) (x).begin(),(x).end() 
#define sz(x) int((x).size())
#define pb push_back
struct triple { int first, second, third; triple(int a, int b, int c) : first(a), second(b), third(c) {}; };
bool match( const triple &a, const triple &b ) { return a.third != b.third && (a.second <= b.first || a.first >= b.second ); }
bool comp(const triple &a, const triple &b) { if(a.second!=b.second) return a.second < b.second; return a.first < b.first; }
void print(const triple &x) { fprintf(stderr,"%02d:%02d %02d:%02d %c\n",x.first/60,x.first%60,x.second/60,x.second%60, x.third+'A'); }
int main() {
	int tn;
	int ret[2];
	cin >> tn;
	int NA, NB;	
	int hh, mm, a, b;
	int T;
	vector<triple> term;
	for(int cc=1;cc<=tn;++cc) {
		ret[0] = ret[1] = 0;
		cin >> T >> NA >> NB;
		REP(i,NA) {
			scanf("%d:%d",&hh,&mm); 
			a = hh * 60 + mm;
			scanf("%d:%d",&hh,&mm);
			b = hh * 60 + mm;
			term.pb(triple(a,b,0));
		}
		REP(i,NB) {
			int hh, mm;
			scanf("%d:%d",&hh,&mm); 
			a = hh * 60 + mm;
			scanf("%d:%d",&hh,&mm);
			b = hh * 60 + mm;
			term.pb(triple(a,b,1));
		}
		sort(all(term),comp);
		vector<bool> chk(sz(term), false);
		REP(i,sz(term)) {
			if(term[i].third==-1) continue;
			ret[term[i].third]++;
			chk.resize(sz(term),false);
			chk[i] = true;
			triple x = term[i]; 
			print(x);
			x.second += T;
			FOR(j,i+1,sz(term)) if(term[j].third!=-1) {
				if(match(x,term[j])) {
					x = term[j];
					print(x);
					x.second += T;
					chk[j] = true;
				}
			}
			REP(j,sz(term)) if(chk[j]) term[j].third = -1;
			cerr << endl;
		}

		printf("Case #%d: ",cc);
		printf("%d %d\n",ret[0], ret[1]);
	}	
}
