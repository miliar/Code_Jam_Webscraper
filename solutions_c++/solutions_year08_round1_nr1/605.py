#include <vector>
#include <fstream>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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

using namespace std;

bool cmp(long long a,long long b){
	if(a<0) a=-a;
	if(b<0) b=-b;
	return a>b;
}
int main() {
	ifstream cin("a.txt");
	ofstream cout("b.txt");
	int i,j,t,c,n,m;
	long long k;
	vector<long long> a,b;
	int f[1000];
	for(cin>>t,c=1;c<=t;c++) {
		a.resize(0);
		b.resize(0);
		memset(f,0,sizeof(f));
		cin>>n;
		for(i=0;i<n;i++) {
			cin>>j;
			a.push_back(j);
		}
		for(i=0;i<n;i++) {
			cin>>j;
			b.push_back(j);
		}
		sort(a.begin(),a.end(),cmp);
		sort(b.begin(),b.end(),cmp);
		k=0;
		for(i=0;i<n;i++) {
			m=0;
			for(j=0;j<n;j++) {
				if(f[j]==0&&(long long)a[i]*b[j]<0) {
					k+=a[i]*b[j];
					f[j]=1;
					m=1;
					break;
				}
			}
			if(m==1) continue;
			for(j=n-1;j>=0;j--) {
				if(f[j]==0&&(long long)a[i]*b[j]>=0) {
					k+=a[i]*b[j];
					f[j]=1;
					break;
				}
			}
		}
		cout<<"Case #"<<c<<": "<<k<<endl;
	}
}