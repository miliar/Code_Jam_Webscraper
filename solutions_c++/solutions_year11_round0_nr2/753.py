#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <limits>
#include <map>
#include <cmath>
#include <numeric>
#include <memory.h>
#include <stdio.h>
using namespace std;
 
#define pb push_back
#define REP(i,n) for(int i=0; i<(n); ++i)   
#define ALL(X) (X).begin(),(X).end()
#define present(c,x) ((c).find(x) != string::npos)
typedef long long ll;
template<class T>inline int sz(T& x){return (int)x.size();}
int stoi(string a){int len=sz(a);if(len==1)return a[0]-'0';return a[len-1]-'0'+10*stoi(a.substr(0,len-1));}
template<class T>inline string tostring(T& i){ostringstream oss; oss << i; return oss.str();}
template <class T> void make_unique(T& v){sort(ALL(v)); v.resize(unique(ALL(v)) - v.begin());}
inline void eraseV(vector<int>& vec,int val) {vector<int>::iterator it = find(ALL(vec),val);if(it!=vec.end()) vec.erase(it,it+1);}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests; cin>>tests;
	for(int test=1;test<=tests;++test){
		vector<string> com;
		vector<string> opp;
		string input;
		int c,d,n;
		cin>>c;
		for(int i=0;i<c;++i){
			string a; cin>>a;
			com.push_back(a);
		}
		cin>>d;
		for(int i=0;i<d;++i){
			string a; cin>>a;
			opp.push_back(a);
		}
		cin>>n>>input;
		string out;
		out += input[0];
		for(int i=1;i<n;++i){
			if(!out.empty()){
				bool f = false;
				for(int j=0;j<sz(com);++j){
					if((com[j][0] == input[i] && com[j][1] == out[sz(out)-1]) || (com[j][1] == input[i] && com[j][0] == out[sz(out)-1])){
						out[sz(out)-1] = com[j][2];
						f = true;
						break;
					}
				}
				if(f) continue;
				for(int j=0;j<sz(opp);++j){
					if((opp[j][0] == input[i] && present(out,opp[j][1])) || (opp[j][1] == input[i] && present(out,opp[j][0]))){
						out.clear();
						f = true;
						break;
					}					
				}
				if(f) continue;
			}

			out += input[i];
		}

		printf("Case #%d: ",test);
		printf("[");
		for(int i=0;i<sz(out);++i){
			printf("%c",out[i]);
			if(i != sz(out) -1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
} 
