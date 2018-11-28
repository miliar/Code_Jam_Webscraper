
#include <iostream>
using namespace std;

const int N =1003;

int a[2*N],b[N];
__int64 sum[N];
int R,K,n;
int main()
{
	freopen("F://Google Code Jam//C-large.in","r",stdin);
	freopen("F://Google Code Jam//write.txt","w",stdout);
	int cas,t=1;
	scanf("%d",&cas);
	while(t<=cas)
	{
		printf("Case #%d: ",t);
		t++;
		scanf("%d %d %d",&R,&K,&n);
		int i;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

		for(i=n;i<2*n;i++)
			a[i] =a[i-n];


		__int64 sumi= 0,sumj =a[0];
		int j=0;
		for(i=0;i<n;i++)
		{
			while(j < i+n && sumj -sumi <=K)
				sumj += a[++j];
			sum[i] = sumj-sumi -a[j];
			b[i] =j%n;
			sumi += a[i];
		}
		__int64 cost =0;
		j =0;
		for(i=0;i<R;i++)
		{
			cost += sum[j];
			j = b[j];
		}
		cout<<cost<<endl;
	}
	return 0;
}