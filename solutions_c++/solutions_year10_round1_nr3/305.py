#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
double z = (1+sqrt(5.0))/2;
int N,a1,a2,b1,b2,l,u;
long long cnt;
int main(){
	scanf("%d",&N);
	for (int zz=1;zz<=N;++zz){
		cnt = 0;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		for (int x=a1;x<=a2;++x){
			l = (int)ceil(x/z);
			u = (int)floor(x*z);
			//printf("hi %d %d %d %I64d\n",l,u,min(b2,u) - max(b1,l),cnt);
			if (!((b1<l && b2<l) || (b1>u && b2>u)))
				cnt += min(b2,u) - max(b1,l) + 1;
		}
		printf("Case #%d: %I64d\n",zz,((long long)(a2-a1+1))*(b2-b1+1) - cnt);
	}
	

	return 0;
}
