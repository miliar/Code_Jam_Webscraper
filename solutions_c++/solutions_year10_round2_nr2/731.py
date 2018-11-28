#include <iostream>
using namespace std;

#define INP_FILE "B-large.in"
#define OUT_FILE "output.txt"


int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	for(int tst=1;tst<=tstCnt;tst++)
	{	
		int n,k,b,t;
		cin>>n>>k>>b>>t;
		int x[100],v[100],bad=0,rez=0;
		for(int i=0; i<n; i++)
			cin>>x[i];
		for(int i=0; i<n; i++)
			cin>>v[i];
		for(int i=n-1; i>=0 && k>0; i--)
			if( b-x[i] <= v[i]*t )
			{
				rez+=bad;
				--k;
			}
			else
			{
				++bad;
			}
		if(k>0)
			printf("Case #%d: IMPOSSIBLE\n",tst);
		else
			printf("Case #%d: %d\n",tst,rez);
	}
	return 0;
}