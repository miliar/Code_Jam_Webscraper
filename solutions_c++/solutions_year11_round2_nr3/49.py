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
int tt,n,k,cnt,kl;
int ws[10000];
int st[10000];
int en[10000];
int br[10000];
int cc[10000];
int ans[10000];
vector<int> v;
vector<int> km[10000];

void razd(vector<int> v){
	int sz,ps1,ps2;
	sz=v.size();
	cnt++;
	for (int i=0;i<sz;i++){
		ws[v[i]]=cnt;
	}
	for (int i=0;i<k;i++){
		if (ws[st[i]]==cnt && ws[en[i]]==cnt && br[i]==0){
			br[i]=1;
			vector<int> v1;
			vector<int> v2;
			ps1=0;
			ps2=0;
			for (int j=0;j<sz;j++) if (v[j]==st[i]){
				ps1=j;
				break;
			}
			for (int j=0;j<sz;j++) if (v[j]==en[i]){
				ps2=j;
				break;
			}
			if (ps1>ps2) swap(ps1,ps2);
			for (int j=ps1;j<=ps2;j++) v1.pb(v[j]);
			for (int j=0;j<=ps1;j++) v2.pb(v[j]);
			for (int j=ps2;j<sz;j++) v2.pb(v[j]);
			razd(v1);
			razd(v2);
			return;
		}
	}
	for (int i=0;i<sz;i++){
		km[kl].pb(v[i]);
	//	mk[v[i]].pb(kl);
	}
/*	cerr<<"New"<<endl;
	for (int i=0;i<sz;i++){
		cerr<<v[i]<<" ";
	}
	cerr<<endl;*/
	kl++;
}
bool bct(int v,int c){
	if (v==n+1){
		for (int i=0;i<kl;i++){
			int gg=0;
			cnt++;
			for (int j=0;j<(int)km[i].size();j++){
				if (ws[cc[km[i][j]]]!=cnt)
					gg++;
				ws[cc[km[i][j]]]=cnt;
			}
			if (gg!=c){
				return false;
			}
		}
		for (int i=1;i<=n;i++)
			ans[i]=cc[i];
		return true;
	}
	for (int i=1;i<=c;i++){
		cc[v]=i;
		if (bct(v+1,c)) return true;
	}
	return false;
}
bool can(int cl){
	return bct(1,cl);
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	scanf("%d",&tt);
	for (int ti=0;ti<tt;ti++){
	//cerr<<"test"<<endl;
		cerr<<ti<<endl;
		scanf("%d%d",&n,&k);
		for (int i=0;i<k;i++)
			scanf("%d",&st[i]);
		for (int i=0;i<k;i++)
			scanf("%d",&en[i]);
		kl=0;
		v.clear();
		for (int i=0;i<n;i++){
			v.pb(i+1);
			br[i]=0;
			km[i].clear();
			//mk[i+1].clear();
		}
		razd(v);
		for (int i=1;i<=n+1;i++){
			if (!can(i)){
				printf("Case #%d: %d\n",ti+1,i-1);
				break;
			}
		}
		for (int i=1;i<=n;i++)
			printf("%d ",ans[i]);
		printf("\n");
		//break;
	}
    return 0;
}









