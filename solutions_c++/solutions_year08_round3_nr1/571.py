//operator system:windows xp
//environment:vc++6.0
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<map>
#include <algorithm>
using namespace std;
#define Pi (4*atan(1))
const double eps = 1e-9;
template<class T> T sqr(T x){return x*x;}
vector<__int64>a(2000);

int main()
{
__int64 sum;
int N;
__int64 i,j,k,m;
__int64 P,K,L;
freopen("c:\\out.txt","w",stdout);
freopen("A-large.in.txt","r",stdin);
cin>>N;
for(i=1;i<N+1;i++)
{

sum=0;
scanf("%I64d%I64d%I64d",&P,&K,&L);
for(j=0;j<L;j++)
scanf("%I64d",&a[j]);
sort(a.begin(),a.begin()+L,greater<__int64>());
int count=0;
for(k=0;k<P;k++)
{
	for(m=0;m<K;m++)
	{
	sum+=(a[count++]*(k+1));
	if(count>=L)break;
	}
	if(count>=L)break;
	
}


printf("Case #%d: ",i);
printf("%I64d\n",sum);
}
return 0;
}