#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
int t;
scanf("%d",&t);

int A[1001], B[1001];

for(int count=0;count<t;count++)
{

int n;
scanf("%d",&n);

for(int i=0;i<n;i++)
scanf("%d %d",&A[i],&B[i]);

int intsec=0;

for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
	if(i==j) continue;
if( (A[j]>A[i] && B[j]<B[i]) || (A[j]<A[i] && B[j]>B[i]))
intsec++;

}
}

intsec=intsec/2;
printf("Case #%d: %d\n",count+1,intsec);


}

return 0;
}
