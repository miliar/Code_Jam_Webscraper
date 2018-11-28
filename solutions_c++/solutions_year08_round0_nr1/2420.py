#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

map<string,int> nametonum;
map<string,int>::iterator it;
vector<int> q;
const int INF = 9999999;
int totaleng;
int m[1002][102];

int findmin(int curqpos,int cureng)
{
  if(cureng!=-1) if(m[curqpos][cureng]!=-1) return m[curqpos][cureng];
  if(curqpos>=q.size()) {if(cureng!=-1) m[curqpos][cureng]=0;return 0;}
  if(cureng!=-1 && q[curqpos]!=cureng) return m[curqpos][cureng]=findmin(curqpos+1,cureng);
  int min = INF;
  int temp = 0;
  for(int i=0;i<totaleng;i++)
  {
    if(i==cureng) continue;
    temp = findmin(curqpos,i);
    if(temp<min) min = temp;
  }
  if(cureng!=-1) min++;
  return m[curqpos][cureng]=min;  
}  

int main()
{
  int N,S,Q;
  cin>>N;
  string s;
  for(int iter=1;iter<=N;iter++)
  {
    nametonum.clear();
    cin>>S;
    totaleng = S;
    cin.ignore();
    for(int i=0;i<S;i++)
    {
      getline(cin,s);
      nametonum[s] = i;
    }
    cin>>Q;
    q.clear();
    cin.ignore();
    for(int i=0;i<Q;i++)
    {
      getline(cin,s);
      q.push_back(nametonum[s]);
    }
    memset(m,-1,sizeof(m));
    cout<<"Case #"<<iter<<": "<<findmin(0,-1)<<endl;
  }
  return 0;
}
    