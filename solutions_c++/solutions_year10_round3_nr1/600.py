#include<iostream>
using namespace std;
const int MAXN=1100;
int A[MAXN],B[MAXN];
int ans(int n)
{
	int cnt=0,i,j;
	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
			if(A[i]>A[j] && B[i] <B[j]  ||  A[i] < A[j] && B[i] > B[j]  )
			{
			  cnt++;
			}
  return cnt;
}
int main()
{
	 freopen("A-large.in","r",stdin);
	 freopen("ans.txt","w",stdout);

   int T,N,i;
   cin>>T;
   for(int t=1;t<=T;t++)
   {cin>>N;
	    for(i=0;i<N;i++)
		  cin>>A[i]>>B[i];

       cout<<"Case #"<<t<<": "<<ans(N)<<endl;

	 


   }


return 0;
}