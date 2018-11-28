#include <iostream>
using namespace std;

int cmp(const void * xx,const void * yy)
{
	if ((*((long *)xx))<(*((long *)yy))) return -1;
	else if ((*((long *)xx))>(*((long *)yy))) return 1;
	else return 0;
}

long n,t,i,kk;
long a[2000],b[2000];
__int64 total,aa,bb;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>t;
	for (kk=1;kk<=t;kk++)
	{
		cin>>n;
		for (i=0;i<n;i++) cin>>a[i];
		for (i=0;i<n;i++) cin>>b[i];
		qsort(a,n,sizeof(long),cmp);
		qsort(b,n,sizeof(long),cmp);
		total=0;
		for (i=0;i<n;i++)
		{
			aa=a[i];
			bb=b[n-i-1];
			total=total+aa*bb;
		}
		printf("Case #%ld: %I64d\n",kk,total);
		//cout<<"Case #"<<kk<<": "<<total<<endl;
	}
	return 0;
}

