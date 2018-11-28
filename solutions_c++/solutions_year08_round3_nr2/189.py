#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)

bool is_ugly(ll);
int cmp(const void *,const void *);
ll gcd(ll,ll);
void rec(char *,int,ll);

ll ans;
int n;

int main (int argc, char *argv[]){
  int ti,tn;
  ifstream fin("B-small-attempt0.in");
  ofstream fout("output.out");
  fin>>tn;
  
  char read [100];
  fin.getline(read,100);
  F1(ti,tn)
  {
    fin.getline(read,100);
    ans=0;

    n=strlen(read);
    rec(read,0,0);
    cout<<"Case #"<<ti<<": "<<ans;
    cout<<endl;
    fout<<"Case #"<<ti<<": "<<ans;
    fout<<endl;
  }
  return 0;
}

int cmp(const void *a,const void *b)
{
  return *(int*)b-*(int*)a;
}

ll gcd(ll x,ll y)
{ 
  return y ? gcd(y, x%y) : x; 
}

bool is_ugly(ll x)
{
  if(x<0)
    x=-x;
  if((x%2==0)||(x%3==0)||(x%5==0)||(x%7==0))
    return true;
  else
    return false;
}

void rec(char *str,int pos,ll sum)
{
  int i;
  ll res=0;
  if(pos==n)
  {
    if(is_ugly(sum))
    {
      ans++;
    }
  }
  for(i=pos;i<n;i++)
  {
    res=res*10+(str[i]-'0');
    
    rec(str,i+1,sum+res);
    if(pos!=0)
      rec(str,i+1,sum-res);
  }
}
