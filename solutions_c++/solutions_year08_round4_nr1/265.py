#include<iostream>
#include<algorithm>
using namespace std;

const int imax=1000000000;
bool isand[10001];
bool value[10001];    // true for int nodes if cheatable
int cost[10001][2];
int sz;

int calc(int val)
{ int i,j;
  for(i=(sz+1)/2;i<=sz;++i) { cost[i][value[i]]=0; cost[i][!value[i]]=imax; }
  for(i=(sz-1)/2;i>0;--i)
  { cost[i][0]=cost[i][1]=imax;
    int a=2*i,b=2*i+1;
    if(isand[i]||value[i])
    { cost[i][0]=min(cost[a][0],cost[b][0])+!isand[i];
      cost[i][1]=cost[a][1]+cost[b][1]+!isand[i];
    }
    if(!isand[i]||value[i])
    { cost[i][0]=min(cost[i][0],cost[a][0]+cost[b][0]+isand[i]);
      cost[i][1]=min(cost[i][1],min(cost[a][1],cost[b][1])+isand[i]);
    }
  }
  return cost[1][val];
}

int main()
{
  int ci,cn,val,i;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>sz>>val;
    for(i=1;i<=(sz-1)/2;++i)
      cin>>isand[i]>>value[i];
    for(;i<=sz;++i) cin>>value[i];
    cout<<"Case #"<<ci<<": ";
    int rv=calc(val);
    if(rv>=imax) cout<<"IMPOSSIBLE"<<endl;
    else cout<<rv<<endl;
  }
}
