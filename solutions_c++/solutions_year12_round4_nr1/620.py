#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d",&cases);
	
	for(int casenum=1;casenum<=cases;casenum++){
		printf("Case #%d: ",casenum);
		vector<int> d,l;
		int n,i,D,a,b;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d",&a,&b);
			d.push_back(a);
			l.push_back(b);
		}
		scanf("%d",&D);
		vector<int> maxswing(n);
		maxswing[0]=d[0];
		for(i=0;i<n;i++){
			int j=i+1;
			int swing=min(maxswing[i],l[i]);
			while(j<n && d[j]-d[i]<=swing){
				maxswing[j]=max(maxswing[j],d[j]-d[i]);
				j++;
			}
		}
		int ans=0;
		for(i=0;i<n;i++)if(d[i]+min(maxswing[i],l[i])>=D)ans=1;
		if(ans)puts("YES");
		else puts("NO");
	}
	return 0;
}