#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
using namespace std;
int main()
{
int l,d,n;
cin >>l>>d>>n;
vector<string> dic;
for(int i=0;i<d;i++)
  {
  string temp;
  cin >>temp;
  dic.push_back(temp);
  }
int now=1;
while(now<=n)
  {
  string ans;
  cin >>ans;
  vector< map<char,bool> > done;
  for(int i=0;i<ans.size();i++)
    {
    map<char,bool> temp;
    if(ans[i]!='(') temp[ans[i]]=1;
    else 
       {
       i++;
       while(ans[i]!=')')
          temp[ans[i++]]=0;
       }
    done.push_back(temp);
    }
  int ret=0;
  for(int i=0;i<dic.size();i++)
    {
    bool f=1;
    string no=dic[i];
    for(int j=0;j<l;j++)
      {
      char q=no[j];
      if(done[j].find(q)!=done[j].end()){}
      else { f=0;break;}
      }
    if(f)ret++;
    }
  cout<<"Case #"<<now<<": "<<ret<<"\n";
  now++;
  }
return 0;
}
