#include <iostream>
using namespace std;

struct tmas{unsigned long long data, euro, num, pred;};

int test,r,n,k;
tmas a[1001];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%i",&test);
	for (int tt=1; tt<=test; tt++) {
		printf("Case #%i: ",tt);
		scanf("%i%i%i",&r,&k,&n);

		for (int i=0; i<n; i++) {
			scanf("%i",&a[i].data);
			a[i].euro=0;
			a[i].pred=-1;
		}

		int start=0;
		int cc=0;

		while (1) {
			int tmp=start;
			unsigned long long sum=0;

			while (sum+a[tmp].data <= (unsigned long long)k) {
				sum+=a[tmp].data;
				tmp=(tmp+1)%n;
				if (tmp==start) break;
			}
			
			a[start].euro+=sum;
			a[start].num=cc;

			cc++;
			if (cc==r) {
				cout << a[start].euro << endl;
				break;
			}

			if (a[tmp].euro>0) {
				unsigned long long dif;
				if (a[tmp].pred<0) dif = a[start].euro;
				else dif = a[start].euro-a[a[tmp].pred].euro;
				unsigned long long cdif = a[start].num-a[tmp].num+1;
				
				unsigned long long sumA=a[start].euro+(unsigned long long)(r-cc)/cdif*dif;

				r=(r-cc)%cdif;
				for (int i=0; i<r; i++) {
					start=tmp;
					sum=0;

					while (sum+a[tmp].data <= (unsigned long long)k) {
						sum+=a[tmp].data;
						tmp=(tmp+1)%n;
						if (tmp==start) break;
					}
					sumA+=sum;
				}

				cout << sumA << endl;
				break;
			}

			a[tmp].euro=a[start].euro;
			a[tmp].pred=start;
			start=tmp;
		}
	}
	
	return 0;
}