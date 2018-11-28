#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<ctime>
#include<cassert>
using namespace std;
#define y1 fndjifhwdn
#define ws vfsdkofsjd
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
int n;
int a[100000];
int can(){
	vector<pi> d1;
	for (int i=0;i<n;i++){
		bool in=false;
		sort(d1.begin(),d1.end());
		for (int j=0;j<(int)d1.size();j++){
			if (a[i]==d1[j].fs+d1[j].sc){
				in=true;
				d1[j].fs++;
				break;
			}
		}
		if (!in){
			d1.pb(mp(1,a[i]));
		}
	}
	int ans=n;
	for (int j=0;j<(int)d1.size();j++){
		ans=min(ans,d1[j].fs);
	}
	return ans;
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt;
	scanf("%d",&tt);
	for (int ti=0;ti<tt;ti++){
		printf("Case #%d: ",ti+1);
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		sort(a,a+n);		
		printf("%d",can());
		printf("\n");
	}
    return 0;
}









