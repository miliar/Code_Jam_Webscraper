#include <list>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <iomanip>

using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;

struct lol {
	int dt,w;
	long double wr;
};

typedef struct lol loli;

bool comp(loli w1,loli w2) {
	return (w1.wr > w2.wr);
}


int main() {
	int NC;

	cin >> NC;
	
	vector<loli> ai;
	
	for(int cs=1;cs<=NC;cs++) {
			ai.clear();
			loli lul;
			int X,S,R,N;
			long double t;
			cin >> X >> S >> R >> t >> N;
			int B,E,w,wr,totd=0;
			for(int i=0;i<N;i++) {
				cin >> B >> E >> w;
				lul.dt=E-B;
				totd+=lul.dt;
				lul.w=w;
				lul.wr=(R+w)/((long double)(S+w));
				ai.push_back(lul);
			}
			lul.dt=X-totd;
			lul.w=0;
			lul.wr=R/((long double)(S));
			ai.push_back(lul);
			sort(ai.begin(),ai.end(),comp);
			long double tot=0;
			int i=0;
			while(t>1e-8 && i<ai.size()) {
				int d=ai[i].dt;
				long double rt=d/((long double)(R+ai[i].w));
				if(rt <= t) {
					tot+=rt;
					t-=rt;
				}
				else {
					long double dd=(R+ai[i].w)*t;
					tot+=t;
					t=0;
					tot+=(d-dd)/((long double)(S+ai[i].w));
				}
				i++;
			}
			while(i<ai.size()) {
					tot+=(ai[i].dt)/((long double)S+ai[i].w);
					i++;
			}
			cout << "Case #" << cs << ": " << setprecision (8) << tot << endl;
			
			
	}
	
	return 0;
}
