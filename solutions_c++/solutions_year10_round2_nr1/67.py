#include<iostream>
#include<map>
#include<string>
#include<vector>
using namespace std;
struct dir
{
  map<string,dir> child;
};

vector<string> split(const string& path)
{
  vector<string> rv;
  for(int i=0;i<path.size();++i)
    if(path[i]=='/') rv.push_back(string());
    else rv.back()+=path[i];
  return rv;
}

int makeifneeded(dir& d,const vector<string>& v,int st)
{
  if(v.size()==st) return 0;
  if(d.child.count(v[st])) return makeifneeded(d.child[v[st]],v,st+1);
  else return makeifneeded(d.child[v[st]],v,st+1)+1;
}

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { int n,m,i,res=0;
    string path;
    dir dir;
    cin>>n>>m;
    for(i=0;i<n;++i)
    { cin>>path;
      makeifneeded(dir,split(path),0);
    }
    for(i=0;i<m;++i)
    { cin>>path;
      res+=makeifneeded(dir,split(path),0);
    }
    cout<<"Case #"<<ci<<": "<<res<<endl;
  }
}
