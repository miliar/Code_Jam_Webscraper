#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<vector>
#include<list>
#include<map>
#include<string>
#include<set>
#include<algorithm>
using namespace std;

#define mm 30000
#define ll long long

int main()
{freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
 int T,vv=0;cin>>T;while(T--)
{vv++;
int n,sum=0;
int a[1010],b[1010];

printf("Case #%d: ",vv);
cin>>n;
for(int i=0;i<n;i++)
scanf("%d %d",&a[i],&b[i]);
for(int i=0;i<n;i++)
{
for(int j=i+1;j<n;j++)
{if(i==j)
continue;
if((a[j]<a[i]&&b[j]>b[i])||(a[j]>a[i]&&b[j]<b[i]))
sum++;
}}
printf("%d\n",sum);








}
//while(1);
return 0;
}
