#include<iostream>
#include<map>
#include<string>
using namespace std;
map<string,int> dict;
char se[120];
char qu[120];
int query[1200];
int q,s;
int ans,res;
int rem[120][1200];
void search(int k,int t)
{
    //cout<<k<<" "<<t<<endl;
    if(ans>=res)return;
    if(rem[k][t]<ans)
       return;
    else
       rem[k][t]=ans;
    int i,x,y,m;
    while(t<q&&query[t]!=k)
      ++t;
    if(t==q)
    {
          if(ans<res)res=ans;
          return;
    }
    ans+=1;
    for(i=0,m=0;i<s;++i)
    {
      if(query[t]!=i)
      {
          x=t;
          while(x<q&&query[x]!=i)++x;
          if(x>m)
          {
              m=x;
              y=i;
          }
      }
    }
    search(y,t);
    ans-=1;
    return;
}
int main()
{
    int i,j,k,t;
    int cases;
    string str;
    //freopen("A-large.in","r",stdin);
    //freopen("AB.out","w",stdout);
    scanf("%d",&cases);
    for(t=1;t<=cases;++t)
    {
        dict.clear();
        scanf("%d\n",&s);
        for(i=0;i<s;++i)
        {
            gets(se);
            str=se;
            dict[str]=i;
        }
        scanf("%d\n",&q);
        for(i=0;i<q;++i)
        {
            gets(qu);
            str=qu;
            if(dict.find(str)==dict.end())
               query[i]=-1;
            else
               query[i]=dict[str];
        }
        res=q;
        ans=0;
        for(i=0;i<s;++i)
            for(j=0;j<q;++j)
               rem[i][j]=12000;
        for(i=0;i<s;++i)
		{
			if(query[0]!=i)
            search(i,0);
		}
		printf("Case #%d: %d\n",t,res);
    }
   // while(1);
    return 0;
}
