//Done by Grey Matter
//Fet per Ferran Alet

#include<iostream>
#include<cmath>
#include<iomanip>
#include<vector>
#include<map>
#include<queue>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<numeric>
#include<set>
#include<sstream>

#define INF 2147483647
#define LINF 1000000000000000000LL
#define EPS 1e-9
#define debug(x) cerr << #x << " = " << x << endl
#define FORN(x,y) for(int x=0;x<y;x++)
#define FORU(x,y) for(int x=1;x<=y;x++)
using namespace std;


typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef map<int,int> MII;
typedef MII::iterator iMII;
typedef long long ll;


int main() {
	ifstream fin("A.in");
	ofstream fout("A.out");
	int t;
	fin>>t;
	for(int cas=1;cas<=t;cas++){
		int n;
		fin>>n;
		VI w(n);
		string s;
		for(int i=0;i<n;i++){
			fin>>s;
			int maxim=-1;
			FORN(j,s.size()) if(s[j]=='1') maxim=j;
			w[i]=maxim;
		}
		queue<pair<VI,int> > q;
		q.push(make_pair(w,0));
		set<VI> S;
		while(1){
			if(!S.count(q.front().first)){
				S.insert(q.front().first);
				bool b=true;
				FORN(i,n) if(q.front().first[i]>i) {
					b=false;
					break;
				}
				if(b) {
					fout<<"Case #"<<cas<<": "<<q.front().second<<endl;
					cout<<"Case #"<<cas<<": "<<q.front().second<<endl;
					break;
				}
				for(int i=0;i<n-1;i++) {
					/*bool bb=true;
					for(int j=0;j<i;j++){
						if(q.front().first[j]>q.front().first[i]) {
							bb=false;
							break;
						}
					}
					for(int j=i+2;j<n;j++) {
						if(q.front().first[j]<q.front().first[i+1]) {
							bb=false;
							break;
						}
					}*/
					if(q.front().first[i]>q.front().first[i+1]){
						swap(q.front().first[i],q.front().first[i+1]);
						q.push(make_pair(q.front().first,q.front().second+1));
						swap(q.front().first[i],q.front().first[i+1]);
					}
				}
			}
			q.pop();
		}
	}
}
