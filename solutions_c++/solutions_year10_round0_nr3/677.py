#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<utility>
using namespace std;
typedef long long ll;
typedef vector<int> vl;
int n,k,r,sum;

struct qq
{
vector<int> V;
int c;
qq(vector<int> a,int b)
{
   V=a;
   c=b;
}
bool operator<(const qq &a)const
{
   return V>a.V;//vector如何比较大小？？ 
}
};
vector<int> trans(vector<int> V)
{
vector<int> tmp1,tmp2;
int i,j;
for(i=0;i<V.size();i++)
{
   if(sum+V[i]>k)
        break;
   sum+=V[i];
   tmp1.push_back(V[i]);  
}
for(j=i;j<V.size();j++)
   tmp2.push_back(V[j]);
for(i=0;i<tmp1.size();i++)
   tmp2.push_back(tmp1[i]);
return tmp2;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    ll ans,tmp1,tmp2;
    int num,b;
    int cas,cas_top,in,i,j;
    scanf("%d",&cas_top);
for(cas=1;cas<=cas_top;cas++)
{
   scanf("%d %d %d",&r,&k,&n);
   ans=0;
   vector<int> V,tempV;
   vector<long long> all;
   set<qq> Setqq;
   set<qq>::iterator it;
   for(i=0;i<n;i++)
   {
        scanf("%d",&in);
        V.push_back(in);
   }
   all.push_back(0);
   for(i=1;i<=r;i++)
   {
        qq tmp(V,i);
        it=Setqq.find(tmp);
        if(it!=Setqq.end())
        {
            b=(*it).c;
            tmp1,tmp2;
            tmp1=all[i-1]-all[b-1];
            num=(r-(i-1));
            tmp2=all[b+num%(i-b)-1]-all[b-1];
            ans=ans+(ll)(num/(i-b))*tmp1+tmp2;
            break;
        }
        else
        {
            sum=0;
            V=trans(V);
            Setqq.insert(tmp);
            ans+=sum;
            all.push_back(ans);
        }
   }
   printf("Case #%d: %lld\n",cas,ans);
}
return 0;
}
