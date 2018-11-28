#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

int main() {
	int t,n;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cin>>n;
		char mat[n][n];
		long double wp[n],owp[n],oowp[n];
		int win[n], loss[n];
		for(int r=0;r<n;r++){
			for(int c=0;c<n;c++){
				cin>>mat[r][c];
			}
		}
		for(int r=0;r<n;r++){
			int w = 0, l = 0;
			for(int c=0;c<n;c++){
				if(mat[r][c]=='1')
					w++;
				else if (mat[r][c]=='0')
					l++;
			}
			wp[r] = w*1.00/(w+l);
			win[r] = w;
			loss[r] = l;
		}
		for(int r=0;r<n;r++) {
			long double tmp=0.0;
			for(int c=0;c<n;c++) {
				if(mat[r][c]!='.') {
					if(mat[r][c]=='0') {
						tmp += (win[c]-1)*1.00/(win[c]+loss[c]-1);
					}
					else {
						tmp += win[c]*1.00/(win[c]+loss[c]-1);
					}
				}
			}
			owp[r] = tmp/(win[r]+loss[r]);
		}
		for(int r=0;r<n;r++){
			long double tmp=0.0;
			for(int c=0;c<n;c++){
				if(mat[r][c]!='.') {
					tmp +=owp[c];
				}
			}
			oowp[r] = tmp*1.00/(win[r]+loss[r]);
		}
		cout<<"Case #"<<i<<":"<<endl;
		for(int r=0;r<n;r++) {
			cout<< setiosflags(ios::fixed) << setprecision(12)<<0.25*wp[r]+0.5*owp[r]+0.25*oowp[r]<<endl;
		}		
	}
}
