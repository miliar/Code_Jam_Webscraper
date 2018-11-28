#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <stdio.h>
#include <queue>



using namespace std;
__int64 res;
int T,test,N,i,j,A[1005],B[1005],k,l,f;
double p[1005][1005],o;
int main()
{
	

	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		res=0;
		cin>>N;
		for(i=0;i<N;i++)
			cin>>A[i]>>B[i];
		for(i=0;i<N;i++)
		{
			
			for(j=0;j<N;j++)
				if(i!=j)
				{
					if(A[i]<A[j]&&B[i]>B[j]||A[i]>A[j]&&B[i]<B[j])
					{
						f=1;
						o=(double)(A[j]-A[i])/(B[i]-B[j]);
						for(l=0;p[i][l]&&f;l++)
							if(p[i][l]==o)
								f=0;
						if(f)
						{
							p[i][l]=o;
							res++;
						}
						f=1;
						for(l=0;p[j][l]&&f;l++)
							if(p[j][l]==o)
								f=0;
						if(f)
						{
							p[j][l]=o;
						}
					}
				};
		}
		cout<<"Case #"<<test<<": "<<res<<"\n";

	}
	return 0;
}