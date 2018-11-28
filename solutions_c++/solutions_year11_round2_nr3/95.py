#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define ll long long
#define ull unsigned long long
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define pii pair<int,int>

int n,m;
int l[2011],r[2011];

int v[2011];
int ja[2011];
int qt;

int best;
int resp[10];
set< vector<int> > faces;
void resolve(int p){
	if(p==n){
		int erro=0;
		for(set< vector<int> > :: iterator it = faces.begin();it!=faces.end();it++){
				vector<int> w = *it;
				int foi[10];
				clr(foi);
				int cnt=0;
				for(int i=0;i<sz(w);i++){
					if(foi[v[w[i]]]==0)cnt++;
					foi[v[w[i]]]=1;
				}
				if(cnt!=qt){erro=1;break;}
		}
		if(erro==0){
			if(qt>best){
				best=qt;
				for(int i=0;i<n;i++)
					resp[i]=v[i]+1;
			}
		}
		return;
	}
	for(int i=0;i<n;i++){
		int era = ja[i];
		if(era==0)qt++;
		ja[i]=1;
		v[p]=i;
		resolve(p+1);
		if(era==0)qt--;	
		ja[i]=era;
	}
}



int main(){
	int casos;
	scanf("%d",&casos);
	for(int caso=1;caso<=casos;caso++){
		scanf("%d %d",&n,&m);
		for(int i=0;i<m;i++){
			scanf("%d",&l[i]);
			l[i]--;
		}
		for(int i=0;i<m;i++){
			scanf("%d",&r[i]);
			r[i]--;
		}
		faces.clear();
		vector<int> w;
		for(int i=0;i<n;i++)
			w.pb(i);
		faces.insert(w);
		for(int i=0;i<m;i++){
			if(l[i]>r[i])
				swap(l[i],r[i]);
			vector<int> w1, w2;
			for(set< vector<int> > :: iterator it = faces.begin();it!=faces.end();it++){
				w = *it;
				int j;
				for(j=0;j<sz(w);j++)
					if(w[j]==r[i])break;
				if(j==sz(w))continue;
				for(j=0;j<sz(w);j++)
					if(w[j]==l[i])break;
				if(j==sz(w))continue;
				w1.clear();
				w2.clear();
				while(1){
				//	printf("j:%d\n",j);
					w1.pb(w[j]);
					if(w[j]==r[i])break;
					j= (j+1)%sz(w);
				}
				while(1){
					w2.pb(w[j]);
					if(w[j]==l[i])break;
					j= (j+1)%sz(w);
				}
				break;
			}
			faces.erase(w);
			faces.insert(w1);
			faces.insert(w2);
		}
		qt=0;
		clr(ja);
		best=-1;
		resolve(0);
		printf("Case #%d: %d\n",caso,best);
		for(int i=0;i<n-1;i++)
			printf("%d ",resp[i]);
		printf("%d\n",resp[n-1]);
	}	
	return 0;
}

