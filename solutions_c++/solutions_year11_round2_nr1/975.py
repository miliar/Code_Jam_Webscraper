#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
const int mx = 210;
char a[mx][mx]={{0}};
int w[mx]={0};
int lo[mx]={0};
int tot[mx]={0};
double wp[mx]={0};
double o1[mx]={0};
double o2[mx]={0};
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,n,t,d,cnt,k;
	cin >> t;
	for (int q=1;q<=t;++q) {
		cin >> n;
		for (i=1;i<=n;++i) {
			for (j=1;j<=n;++j)
				cin >> a[i][j];
		}
		for (i=1;i<=n;++i) {
			tot[i] = w[i] = lo[i] = 0;
			for (j=1;j<=n;++j) {
				if (i==j)
					continue;
				if (a[i][j]!='.') {
					++tot[i];
					if (a[i][j]=='1')
						++w[i];
					else ++lo[i];
				}
			}
			wp[i] = w[i] / (tot[i] + .0);
		}
				if (q==2) {
			q=q;
		}

		for (i=1;i<=n;++i) {
			o1[i] = 0;
			for (j=1;j<=n;++j) {
				if (i==j || a[i][j]=='.')
					continue;
				d = cnt = 0;
				for (k=1;k<=n;++k) {
					if (k==i || k==j)
						continue;
					if (a[j][k]!='.') {
						if (a[j][k]=='1')
							++cnt;
						++d;
					}
				}
				o1[i] += cnt / (d + .0);
			}
			o1[i] /= (tot[i] + .0);
		}
		if (q==2) {
			q=q;
		}
		for (i=1;i<=n;++i) {
			o2[i] = .0;
			for (j=1;j<=n;++j) {
				if (i==j)
					continue;

				if (a[i][j]!='.') {
					o2[i] += o1[j];
				}
			}
			o2[i] /= (tot[i] + .0);
		}
		double r;
		cout << "Case #" << q << ":\n";
		for (i=1;i<=n;++i) {
			r = 0.25 * wp[i] + 0.5 * o1[i] + 0.25 * o2[i];
			printf("%.9lf\n",r);
		}
		
	}
	

	return 0;
}