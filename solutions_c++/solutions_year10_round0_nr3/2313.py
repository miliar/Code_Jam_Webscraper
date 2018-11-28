#include<iostream>
#include<cstdio>
using namespace std;

int main(void)
{
	int r,k;
	int n;
	int t;
	int sum;
	int a[100];
	int count=0;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		count++;
		scanf("%d %d %d",&r,&k,&n);
		for(int i=0; i<n; i++)
			scanf("%d",&a[i]);
		sum=0;
		while(r--){
			int temp=0;
			int l=n;
			int j;
			for(j=0; j<n && temp+a[j]<=k; j++){
				temp+=a[j];
				a[l++]=a[j];
			}
			sum+=temp;
			temp=j;
			for(; j<l; j++)
				a[j-temp]=a[j];

		}
		printf("Case #%d: %d\n",count,sum);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
			


