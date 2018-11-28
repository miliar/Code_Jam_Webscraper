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
#define MINS 24*60

int d(string s){
	int i,ret=0;
	FOR(i,2)
		ret=10*ret+s[i]-'0';
	return ret;
};

int c(string s){
	int ret = 60*d(s.substr(0,2)) + d(s.substr(3));
	return ret;
};

int TA;
int NA,NB;
int ts[MINS+100][2];
int main(){
	int cases;
	cin >> cases;
	for(int it=1;it<=cases;it++){
		cin >> TA >> NA >> NB;
		SET(ts,0);
		vector<pair<int,pair<int,int> > > V;
		V.clear();int i;
		string s1,s2;
		FOR(i,NA){
			cin >> s1 >> s2;
			V.PB(MP(c(s2)+TA,MP(c(s1),0)));
		}
		FOR(i,NB){
			cin >> s1 >> s2;
			V.PB(MP(c(s2)+TA,MP(c(s1),1)));
		}
		sort(ALL(V));
		int ans[2]={0};
		FOR(i,SZ(V)){
			int arrival = V[i].first;
			int departure = V[i].second.first;
			int x = V[i].second.second;
			//cout << arrival << " " << departure << " " << x << endl;
			int j;
			for(j=departure;j>=0 && ts[j][x]==0;j--);
			if(j<0){
				//cout<<arrival<<" "<<departure<<" "<<x<<endl;
				ans[x]++;
			}
			else{
				ts[j][x]--;
			}
			ts[arrival][1-x]++;
		}
		cout << "Case #"<<it<<": "<<ans[0]<<" "<<ans[1]<<endl;
	}
	return 0;
}
