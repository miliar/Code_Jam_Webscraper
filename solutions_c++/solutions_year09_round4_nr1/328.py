#include <cstdio>
#include <algorithm>
#define N 50
using namespace std;

int n,c,AC,t,p,v[N];
char s[N][N];

int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
	scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%s",s[i]);
		for (int i=0;i<n;i++){
		v[i]=0;
			for (int j=0;j<n;j++)
				if (s[i][j]=='1') v[i]=j;
		}
	AC=0;
		for (int i=0;i<n;i++){
			if (v[i]<=i) continue;
		p=0;
			for (int j=i;j<n&&!p;j++)
				if (v[j]<=i) p=j;
			for (int j=p;j>i;j--) swap(v[j],v[j-1]),AC++;
		}		
	printf("Case #%d: %d\n",tc,AC);
	}
	return 0;
}
