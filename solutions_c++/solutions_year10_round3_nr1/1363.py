#include<vector>
#include<fstream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<functional>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
int t;
freopen("A-large.in.txt","r",stdin);
freopen("A-small-attempt0.in.out","w",stdout);
     
cin>>t;
for(int tt=1;tt<=t;tt++)
{
	int ret=0;
	int N;
	cin>>N;
	int A[1000],B[1000];
	for(int q=0;q<N;q++)
	{
		cin>>A[q]>>B[q];
	}
	for(int q=0;q<N;q++)
	for(int qq=q+1;qq<N;qq++)
	{	
		if(A[qq]<A[q] && B[qq]>B[q])
		{
			ret++;
		}
		if(A[qq]>A[q] && B[qq]<B[q])
		{
			ret++;
		}
	}
	cout<<"Case #"<<tt<<": "<<ret<<endl;
}
return 0;
};
