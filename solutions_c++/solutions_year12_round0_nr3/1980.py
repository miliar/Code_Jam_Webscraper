#include <cstdio>

using namespace std;

bool h[2000001];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int st[10];
	st[0]=1;
	for (int i=1; i<9; i++)
		st[i]=st[i-1]*10;
	int T;
	scanf("%d",&T);
	for (int t=0; t<T; t++) {
		printf("Case #%d: ",t+1);
		int a,b;
		int ndig=1;
		scanf("%d%d",&a,&b);
		for (int i=a; i<=b; i++) h[i]=false;
		int res=0;
		while (a>=st[ndig]) ndig++;
		for (int A=a; A<=b; A++) {
			int dig[10];
			if (h[A]) continue;
			int tmp=A;
			int res1=1;
			for (int i=ndig; i>0; i--) {
				dig[i]=tmp % 10;
				tmp/=10;
			}
			for (int i=1; i<=ndig; i++) {
				tmp=0;
				int k=ndig-1;
				if (dig[i]<dig[1]) continue;
				for (int j=i; j<=ndig; j++) {
					tmp+=st[k]*dig[j];
					k--;
				}
				for (int j=1; j<i; j++) {
					tmp+=st[k]*dig[j];
					k--;
				}

				if (tmp>A && tmp<=b && !h[tmp]) {
					res1++;
					h[tmp]=true;
				}
			}
			res+=res1*(res1-1)/2;
		}
		printf("%d\n",res);
	}
	return 0;
}
