#pragma warning(disable:4018)  // signed/unsigned mistatch
#pragma warning(disable:4244)  // w64 to int cast
#pragma warning(disable:4267)  // big to small -- possible loss of data
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4800)  // forcing int to bool
#pragma warning(disable:4996)  // deprecations
#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}
using namespace std;

char buffer[110];
struct team{
	int wins, games;
	double wp, owp, oowp;
};

int main(){
	freopen("A-large-0.in","r",stdin);
	freopen("A-large-0.out", "w", stdout);
	int T; scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		int n; scanf("%d\n", &n);
		vector <string> v(n);
		for(int i=0; i<n; ++i){
			scanf("%s", buffer);
			v[i] = buffer;
		}
		vector < vector <int> > oponents(n);
		vector < team > teams(n);
		for(int i=0; i<n; ++i){
			teams[i].games = teams[i].wins = 0;
			for(int j=0; j<n; ++j){
				if(v[i][j] == '0'){
					teams[i].games++;
					oponents[i].push_back(j);
				}else if(v[i][j] == '1'){
					teams[i].wins++;
					teams[i].games++;
					oponents[i].push_back(j);
				}
			}
			teams[i].wp = (double)(teams[i].wins)/(double)(teams[i].games);
		}
		
		//owp
		for(int i=0; i<n; ++i){
			double avg = 0.0;
			teams[i].owp = avg;
			for(int j=0, m=oponents[i].size(); j<m; ++j){
				int x = oponents[i][j];
				if(v[i][x] == '1'){
					avg += (double)(teams[x].wins)/(double)(teams[x].games - 1);
				}else if(v[i][x] == '0'){
					avg += (double)(teams[x].wins-1)/(double)(teams[x].games - 1);
				}
			}
			if(oponents[i].size() > 0)
				teams[i].owp = avg / (double)(oponents[i].size());
		}

		//oowp
		for(int i=0; i<n; ++i){
			double avg = 0.0;
			teams[i].oowp = avg;
			for(int j=0, m=oponents[i].size(); j<m; ++j){
				int x = oponents[i][j];
				avg += teams[x].owp;
			}
			if(oponents[i].size() > 0)
				teams[i].oowp = avg / (double)(oponents[i].size());
		}
		printf("Case #%d:\n", t);
		for(int i=0; i<n; ++i){
			double x = (0.25*teams[i].wp) + (0.5 * teams[i].owp) + (0.25 * teams[i].oowp);
			printf("%lf\n", x);
		}
	}
	return 0;
}