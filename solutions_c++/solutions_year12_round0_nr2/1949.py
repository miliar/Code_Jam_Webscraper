#include <cstdio>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int t=0; t<T; t++) {
		int n,s,p;
		int ans=0;
		printf("Case #%d: ",t+1);
		scanf("%d%d%d",&n,&s,&p);
		for (int i=0; i<n; i++) {
			int a;
			scanf("%d",&a);
			if (a<p) continue;
			if ((a-p)/2>=p-1) {
				ans++;
				continue;
			}
			if ((a-p)/2>=p-2 && s>0) {
				ans++;
				s--;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}