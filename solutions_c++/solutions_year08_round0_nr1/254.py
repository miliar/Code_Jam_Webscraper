#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(int bef,int pos,const vector<int> &qs,int s,vector<vector<int> > &tbl)
{
  int n=qs.size();
  if (pos==n) return 0;

  int &ret=tbl[bef][pos];
  if (ret>=0) return ret;

  ret=0x7fffffff;

  for (int i=0;i<s;i++)
    if (qs[pos]!=i)
      ret<?=solve(i,pos+1,qs,s,tbl)+(i==bef?0:1);

  return ret;
}

int main()
{
  int cases;cin>>cases;
  for (int c=1;c<=cases;c++){
    int s;cin>>s>>ws;
    vector<string> names(s);
    for (int i=0;i<s;i++)
      getline(cin,names[i]);

    int q;cin>>q>>ws;
    vector<int> qs(q);
    for (int i=0;i<q;i++){
      string line;
      getline(cin,line);

      qs[i]=find(names.begin(),names.end(),line)-names.begin();
    }

    vector<vector<int> > tbl(s,vector<int>(q,-1));

    int ans=0x7fffffff;

    if (q==0)
      ans=0;
    else{
      for (int i=0;i<s;i++){
	if (i==qs[0]) continue;
	ans<?=solve(i,1,qs,s,tbl);
      }
    }

    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
