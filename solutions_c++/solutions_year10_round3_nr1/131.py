#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int tt,n;
struct gg
{
	int p,s;
};
gg num[10000];
int cmp(gg a,gg b)
{
	return a.p<b.p;
}
int rec[10000];
int temp[10000];
int MergeSort(int a[],int c[],int left,int right)
{
	int i,j,mid,temp,count;
	int total;
	total=0;
	if (right>=left+1) {
		mid=(left+right)/2;
		total+=MergeSort(a,c,left,mid);
		total+=MergeSort(a,c,mid+1,right);
		count=0;
		for (i=left,j=mid+1;i<=mid && j<=right;)
		{
			if (a[i]>a[j]) {
				total+=mid-i+1;
				count++;
				c[count]=a[j];
				j++;
			} 
			else {
				count++;
				c[count]=a[i];
				i++;
			}
		}
		while (i<=mid) {
			count++;
			c[count]=a[i];
			i++;
		}
		while (j<=right) {
			count++;
			c[count]=a[j];
			j++;
		}
		for (i=left;i<=right;i++)
			a[i]=c[i-left+1];
	}
	return total;
}

int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{
		cin>>n;
		for (int i=1;i<=n;++i)
		{
			cin>>num[i].p>>num[i].s;
		}
		sort(num+1,num+1+n,cmp);
		for (int i=1;i<=n;++i)
		{
			rec[i]=num[i].s;
		}
		int ans=MergeSort(rec,temp,1,n);
		printf("Case #%d: ",kk);
		cout<<ans<<endl;
	}	
	return 0;	
}