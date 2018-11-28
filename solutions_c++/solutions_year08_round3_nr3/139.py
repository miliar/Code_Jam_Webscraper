#include <iostream>

using namespace std;

int main()
{
        int t, test, n, m, i, tmp, j;
	long long x, y, z, A[500000], B[500000], DP[500000], ret;
        cin>>t;
        for(test=1; test<=t; test++)
        {
		cin>>n>>m>>x>>y>>z;
		for(i=0; i<m; i++)
			cin>>A[i];
		for(i=0; i<n; i++)
		{
			B[i]=A[i%m];
			A[i%m]=(x*A[i%m]+y*(i+1))%z;
		}
		ret=1;
		DP[0]=1;
		for(i=1; i<n; i++)
		{
			DP[i]=1;
			for(j=0; j<i; j++)
				if(B[j]<B[i])
				{
					DP[i]+=DP[j];
					DP[i]=DP[i]%1000000007;
				}
			ret+=DP[i];
			ret=ret%1000000007;
		}
                cout<<"Case #"<<test<<": "<<ret%1000000007<<endl;
        }
        return 0;
}

