#pragma warning(disable:4786)
#include<stdio.h>
#include<queue>
#include<algorithm>
#include<set>
#include<utility>
using namespace std;

#define MAX 10006

typedef pair<int,int> ii;
int n;
int d[MAX],l[MAX];
int s[MAX];

ii mx[MAX];

#define INT(x)	scanf("%d",&x)

inline int min(int x,int y){
	return x < y ? x : y;
}

inline int abs(int x){
	return x > 0 ? x : -x;
}

int main(){
	int T,N,tot;
	int i,j,lastl;
	int newmax,newmaxi,newmaxl;
	scanf("%d",&T);
	for(N=1;N<=T;N++){
		scanf("%d",&n);

		d[0] = 0;
		l[0] = 0;
		for(i=1;i<=n;i++){
			scanf("%d",&d[i]);
			scanf("%d",&l[i]);
			mx[i] = ii(d[i]+l[i], i);
		}
		scanf("%d",&tot);
		
		queue<int> qi,qp;
		set<ii> s;
		
		if(l[0] >= d[0]){
			qi.push(1);
			qp.push(0);
			s.insert(ii(1,0));
		}

		bool ok = 0;

		while(!qi.empty()){
			int now = qi.front();
			qi.pop();
			int pos = qp.front();
			qp.pop();

			int ll;
			if(pos == -1)
				ll = l[now];
			else
				ll = d[now] - d[pos];

			if(d[now]+ll >= tot){
				ok = 1;
				break;
			}

			for(i=1;i<=n;i++)if(i!=now){
				if(abs(d[i] - d[now]) > ll)
					continue;
				
				int x = now;
				if(abs(d[i] - d[now]) > l[i])
					x = -1;
				if(s.find(ii(i,x))==s.end()){
					qi.push(i);
					qp.push(x);
					s.insert(ii(i,x));
				}
			}
		}

/*		i = 1;
		lastl = d[1];
		while(1){
			if(d[i] + lastl >= tot){
				ok = 1;
				break;
			}
			newmaxi = -1;
			newmax = -1;
			for(j=i+1;j<=n;j++){
				int maxl = min(d[j]-d[i], l[j]);
				
				if(d[i]+lastl < d[j])
					break;

				if(d[j]+maxl > newmax){
					newmaxl = maxl;
					newmaxi = j;
					newmax = d[j] + maxl;
				}
				else if(d[j]+maxl == newmax && maxl > newmaxl){
					newmaxl = maxl;
					newmaxi = j;
					newmax = d[j] + maxl;
				}
			}
			if(newmaxi == -1)
				break;

			i = newmaxi;
			lastl = newmaxl;
		}
*/
/*		i = n;
		int need = tot - d[n];
		if(l[n] < need){
			printf("Case #%d: NO\n",N);
			continue;
		}

		while(1){
			for(j=i-1;j>=1;j--){

			}
		}
*/
		if(ok)
			printf("Case #%d: YES\n",N);
		else
			printf("Case #%d: NO\n",N);

	}
	return 0;
}