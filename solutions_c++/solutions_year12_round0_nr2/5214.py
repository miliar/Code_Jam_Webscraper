#include<iostream>
#include<cstdio>
#include<map>
#include<set>
#include<vector>
#include<climits>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<stack>
#include<queue>

using namespace std;

using namespace std;

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
int t;
scanf("%d",&t);

for(int tt=0;tt<t;tt++)
{
int n,s,p;

int str=0,nstr=0;

scanf("%d %d %d",&n,&s,&p);

int a[n];
for(int i=0;i<n;i++)
scanf("%d",&a[i]);

int temp;
for(int i=0;i<n;i++)
{
temp=a[i]/3;

if((temp>=p)||(temp+1==p&&a[i]%3>0))
{nstr++;}
else if((temp+2>=p&&a[i]%3==2)||(temp+1>=p&&a[i]%3==0&&a[i]>0))
{str++;}

}

int res=nstr+min(str,s);
printf("Case #%d: %d\n",tt+1,res);

}


return 0;
}
