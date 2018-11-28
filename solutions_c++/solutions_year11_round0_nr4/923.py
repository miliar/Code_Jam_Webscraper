#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int t;
int n;
int a[3000];
int b[3000];
map<int,int> mp;
int used[3000];

void solve(int testcase){
	memset(used,0,sizeof(used));
	mp.clear();
	scanf("%d",&n);
	for (int i=0; i<n; i++)
		scanf("%d",&a[i]), b[i]=a[i];
	sort(b,b+n);
	for (int i=0; i<n; i++)
		mp[b[i]]=i;
	for (int i=0; i<n; i++)
		a[i]=mp[a[i]];

	double res=0;
	for (int i=0; i<n; i++){
		if (!used[i]&&a[i]!=i){
			int tek=a[i];
			used[i]=1;
			int cnt=1;
			while (!used[tek]){
				used[tek]=1;
				cnt++;
				tek=a[tek];
			}
			res+=cnt;
		}
	}

	printf("Case #%d: %.10lf\n",testcase,res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);

	for (int i=1; i<=t; i++)
		solve(i);	

	return 0;
}