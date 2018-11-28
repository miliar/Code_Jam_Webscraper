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
int dig(string &s, int i){
	return int(s[i]-'0');
}
int read(){
	string s;
	cin >> s;
	return dig(s, 0)*600+dig(s,1)*60+
		dig(s,3)*10 + dig(s,4);
}
void go(vector<pair<int,int> > &a, vector<bool> &ua, vector<pair<int,int> > &b, vector<bool> &ub, int t, int s){
	ua[s]=true;
	int start = a[s].second+t;
	//cout << "**"<<s << endl;
	forn(i, b.size())if(!ub[i] && b[i].first>=start){
		go(b,ub,a,ua,t,i);
		return;
	}
}
int main(){
	int N; cin >> N;
	forn(c, N){
		int t; cin >> t;
		int NA, NB; cin >> NA >> NB;
		vector<pair<int,int> >   fa(NA), fb(NB);
		vector<bool> ua(NA, false), ub(NB, false);
		forn(i, NA){
			fa[i].first = read();
			fa[i].second = read();
		}
		forn(i, NB){
			fb[i].first = read();
			fb[i].second = read();
		}
		sort(fa.begin(), fa.end());
		sort(fb.begin(), fb.end());
		
		int nexta = 0;
		int nextb = 0;
		int ra = 0, rb=0;
		while(nexta < fa.size() && nextb < fb.size()){
			if(ua[nexta]){nexta++;continue;}
			if(ub[nextb]){nextb++;continue;}
			//cout << ">>"<<nexta << " " << nextb << endl;
			if(fa[nexta].first < fb[nextb].first){
				//cout << "a" << endl;
				go(fa,ua,fb,ub,t,nexta);
				ra++;
			}else{
				//cout << "b" << endl;
				go(fb,ub,fa,ua,t,nextb);
				rb++;
			}
		}
		forn(i, fa.size())if(!ua[i])ra++;
		forn(i, fb.size())if(!ub[i])rb++;
		cout << "Case #" << c+1 << ": " << ra << " " << rb << endl;
	}
	return 0;
}
