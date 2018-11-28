#include <stdio.h>
#include <algorithm>
using namespace std;

int dist[1000010],prof[1000010];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntc;
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		int l,n,c;
		long long t,tsum=0,res=0;
		scanf("%d %lld %d %d",&l,&t,&n,&c);
		for (int i=0;i<c;i++) scanf("%d",&dist[i]);
		for (int i=c;i<n;i++) dist[i]=dist[i%c];
		for (int i=0;i<n;i++){
			prof[i]=dist[i];
			dist[i]*=2;
		}
		for (int i=0;i<n;i++){
			tsum+=dist[i];
			if (tsum>t){
				prof[i]=(tsum-t)/2;
				break;
			}
			else prof[i]=0;
		}
		sort(prof,prof+n);
		for (int i=0;i<n;i++) res+=dist[i];
		for (int i=0;i<l;i++) res-=prof[n-1-i];
		printf("Case #%d: %lld\n",tc,res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}