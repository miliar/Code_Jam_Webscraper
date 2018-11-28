#define _CRT_SECURE_NO_DEPRECATE
#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
int main()
{
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it=1;it<=nt;it++)
	{
		int n;
		cin  >> n;
		vector<string> a(n);
		for (int i=0;i<n;++i){
			cin >> a[i];
		}
		vector<ld> res(n, 0.0);
		vector<ld> owp(n ,0.0);
		for (int i=0;i<n;++i){
			ld countt = 0.0;
			for (int j=0;j<n;++j){
				if (a[i][j] == '.') {
					continue;
				}
				countt += 1.0;
				ld br = 0.0;
				ld cnt = 0.0;
				for (int k=0;k<n;++k){
					if (k ==i || k == j){
						continue;	
					}
					if (a[j][k] == '.') {
						continue;
					}
					if (a[j][k] == '1'){
						br += 1.0;
					}
					cnt += 1.0;
				}
				owp[i] += br / cnt;
			}
			owp[i] /= countt;
		}
		for (int i=0;i<n;++i){
			ld br = 0.0;
			ld cnt = 0.0;
			for (int j=0;j<n;++j){
				if (j == i || a[i][j] == '.'){
					continue;
				}
				if (a[i][j] == '1'){
					br += 1.0;
				}
				cnt += 1.0;
			}
			ld wp = (ld)br / cnt;
			ld oowp = 0.0;
			for (int j=0;j<n;++j){
				if(j ==i || a[i][j] == '.') {
					continue;
				}
				oowp += owp[j];
			}
			oowp /= cnt;
			res[i] = 0.25 *wp + 0.50 * owp[i] + 0.25 * oowp;
		}
		cout<<"Case #"<<it<<":"<<endl;
		for (int i=0;i<n;++i){
			printf("%.9llf\n",res[i]);
		}
	}
	return 0;
}
