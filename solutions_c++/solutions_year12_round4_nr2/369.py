#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>
#include <set>
#include <complex>
#include <iomanip>
#include <queue>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define show(x) cerr << "#" << #x << ": " << x << endl
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;
typedef pair<int, int> pii;
typedef complex<double> point;

const int MAX_N = 1000 + 10;

pii r[MAX_N];
double x[MAX_N];
double y[MAX_N];

vector<int> hgt;
vector<int> len;

int main(){
	int test_n;
	cin >> test_n;
	for(int test_i = 1; test_i <= test_n; test_i++){
		hgt.clear();
		len.clear();
		int n, w, l;
		cin >> n >> w >> l;
		FOR(i, n){
			cin >> r[i].F;
			r[i].S = i;
		}
		sort(r, r + n, greater<pii>());
		hgt.PB(l);
		len.PB(w);
		FOR(i, n){
			int tool = 2 * r[i].F;
			int id = r[i].S;
			int sum = 0, min_hgt = l;
			bool puted = false;
			FOR(j, SZ(hgt)){
// 				if(i == 0){
// 					show(hgt[j]);
// 					show(tool);
// 					show(len[j]);
// 				}
				min_hgt = min(min_hgt, hgt[j]);
				if((hgt[j] == l || hgt[j] >= tool) && ((sum == 0  && len[j] >= tool / 2) || len[j] >= tool)){
					if(sum == 0){
						x[id] = 0;
						len.insert(len.begin() + j, tool / 2);
						len[j + 1] -= tool / 2;
					}else{
						x[id] = sum + tool / 2;
						len.insert(len.begin() + j, tool);
						len[j + 1] -= tool;
					}
					
					if(hgt[j] == l){
						y[id] = l;
						hgt.insert(hgt.begin() + j, hgt[j] - tool / 2);
					}else{
						y[id] = hgt[j] - tool / 2;
						hgt.insert(hgt.begin() + j, hgt[j] - tool);
					}
					puted = true;
					break;
				}
				sum += len[j];
			}
			
			if(puted)
				continue;
			
			x[id] = 0;
			y[id] = min_hgt - tool / 2;
			
			if(min_hgt - tool / 2 >= 0)
				puted = true;
			
			FOR(i, SZ(hgt))
				hgt[i] = min_hgt - tool;
			
			if(!puted)
				cerr << test_i << " ERROR!\n";
			
		}
		printf("Case #%d:", test_i);
		FOR(i, n)
			printf(" %0.0lf %0.0lf", x[i], y[i]);
		printf("\n");
	}
	return 0;
}
