#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;
#define forn(i,n) for(int i=0;i<int(n);++i)
int best[105][1005];
vector<string> sites;
vector<string> qs;
const int INF = 100000;
bool can(int i, int j){
	return sites[i]!=qs[j];
}
string dummy;
int main(){
	int N; cin >> N;
	forn(c, N){
		int S; cin >> S;
		getline(cin, dummy);
		sites = vector<string>(S);
		forn(i,S)getline(cin, sites[i]);

		int Q; cin >> Q;
		getline(cin, dummy);
		int r;
		if(Q > 0){
			qs = vector<string>(Q);
			forn(i,Q)getline(cin, qs[i]);

			forn(q,Q){				
				forn(s, S){
					best[s][q]=INF;
					if(can(s,q)){
						if(q==0){
							best[s][q]=0;
						}else{
							best[s][q]=min(best[s][q],best[s][q-1]);
							forn(s2, S)if(s!=s2)best[s][q]=min(best[s][q],best[s2][q-1]+1);
						}
					}
					//cout << best[s][q] << " ";
				}
				//cout << endl;
			}
			r = INF;
			forn(s, S)r=min(r,best[s][Q-1]);
		}else{
			r = 0;
		}
		cout << "Case #" << c+1 << ": " << r << endl;
	}
	return 0;
}
