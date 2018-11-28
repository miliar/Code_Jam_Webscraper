#include <iostream>
using namespace std;

#define INP_FILE "A-large.in"
#define OUT_FILE "output.txt"

int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	for(int tst=1;tst<=tstCnt;tst++)
	{	
		int n,a[2000],b[2000];
		long int r=0;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i]>>b[i];
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				r+= ( a[i]>a[j] && b[i]<b[j] ) || ( a[i]<a[j] && b[i]>b[j] );

		printf("Case #%d: %ld\n",tst,r);
	}
	return 0;
}