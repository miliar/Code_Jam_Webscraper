#include<iostream>
#include<string>
#include<vector>
using namespace std;
int mt(string st)
{ int h=(st[0]-48)*10+(st[1]-48);
  int m=(st[3]-48)*10+(st[4]-48);
  return h*60+m;
}
void count(vector<int>depA,vector<int>avB,vector<int>depB,vector<int>avA)
{ int na=0,nb=0;
  sort(depA.begin(),depA.end());
  sort(avA.begin(),avA.end());
  int i=0;
  for(i=0;i<depA.size()&&!avA.empty();++i)
  {  if(depA[i]>=avA[0])
      { avA.erase(avA.begin());
      }
      else
      ++na;
  }
  na+=depA.size()-i;
  
  sort(depB.begin(),depB.end());
  sort(avB.begin(),avB.end());
  for(i=0;i<depB.size()&&!avB.empty();++i)
  {  if(depB[i]>=avB[0])
      { avB.erase(avB.begin());
      }
      else
      ++nb;
  }
  nb+=depB.size()-i;
  cout<<na<<" "<<nb<<endl;
}
int main()
{ freopen("in.IN","r",stdin);
  freopen("output.txt","w",stdout);
  int n;
  cin>>n;
  for(int i=0;i<n;i++)
  { vector<int> depA,avB,depB,avA;
    string st1,st2;
    int td,a,b;
    cin>>td;
    cin>>a>>b;
    for(int j=0;j<a;j++)
    { cin>>st1>>st2;
      depA.push_back(mt(st1));
      avB.push_back(mt(st2)+td);
    }
    for(int j=0;j<b;j++)
    { cin>>st1>>st2;
      depB.push_back(mt(st1));
      avA.push_back(mt(st2)+td);
    }
    cout<<"Case #"<<i+1<<": ";
    count(depA,avB,depB,avA);
  }
}        
