#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

map<string,int> mymap;
map<string,int> mymap3;
map<string,int> mymap6;
map<string,int> mymap9;
map<string,int> mymap12;

void count(VS &str, string ts, int i, int &num)
{
  if(i==str.size()-1)
  {
    string ts1;
    int j;
    REP(j,str[i].length())
    {
      ts1=ts+str[i].at(j);
      if(mymap.find(ts1)->second==1)  { 
        cout<<ts1<<endl;
        num++; 
      }
    }
  }
  else if(i==3-1)
  {
    string ts1;
    int j;
    REP(j,str[i].length())
    {
      ts1=ts+str[i].at(j);
      if(mymap3.find(ts1)->second!=1) continue;
      else count(str,ts1,i+1,num);
    }
  }
  else if(i==6-1)
  {
    string ts1;
    int j;
    REP(j,str[i].length())
    {
      ts1=ts+str[i].at(j);
      if(mymap6.find(ts1)->second!=1) continue;
      else count(str,ts1,i+1,num);
    }
  }
  else if(i==9-1)
  {
    string ts1;
    int j;
    REP(j,str[i].length())
    {
      ts1=ts+str[i].at(j);
      if(mymap9.find(ts1)->second!=1) continue;
      else count(str,ts1,i+1,num);
    }
  }
  else if(i==12-1)
  {
    string ts1;
    int j;
    REP(j,str[i].length())
    {
      ts1=ts+str[i].at(j);
      if(mymap12.find(ts1)->second!=1) continue;
      else count(str,ts1,i+1,num);
    }
  }
  else {
    string ts1;
    int j;
    REP(j,str[i].length())
    {
      ts1=ts+str[i].at(j);
      count(str,ts1,i+1,num);
    }
  }
}

int main(int argc, char** argv)
{
  ifstream in(argv[1]);
  int l,d,n;
  in>>l;in>>d;in>>n;
  int i,j,k;
  VS idx;
  REP(i,d)
  {
    string s;
    in>>s;
    mymap[s]=1;
    if(l>3) mymap3[s.substr(0,3)]=1;
    if(l>6) mymap6[s.substr(0,6)]=1;
    if(l>9) mymap9[s.substr(0,9)]=1;
    if(l>12) mymap12[s.substr(0,12)]=1;
    REP(j,l) {
      if(i==0) 
      {
        string ts="";
        ts+=s[j];
        idx.PB(ts);
      }
      else idx[j].append(s,j,1);
    }
  }
  //cout<<"map over"<<endl;
  //REP(j,l) cout<<idx[j]<<endl;
  //map<string,int>::iterator it;
  //for(it=mymap6.begin();it!=mymap6.end();it++)
  //  cout << (*it).first << " => " << (*it).second << endl;


  ofstream out(argv[2]);
  REP(i,n)
  {
    cout<<i<<endl;
    VS myvs;
    string s;
    in>>s;
    string ts;
    bool inbr=false;
    bool zero=false;
    int id=0;
    REP(j,s.length())
    {
      if(s[j]=='(')
      {
        ts.clear();
        inbr=true;
      }
      else if(s[j]==')')
      {
        if(ts.length()==0) { zero=true; break; }
        myvs.PB(ts);
        id++;
        inbr=false;
      }
      else if(char(s[j])>=97 && char(s[j])<=122)
      {
        if(inbr) { 
          size_t found;
          found=idx[id].find(s[j]);
          if (found!=string::npos)
            ts+=s[j];
        }
        else {
          ts.clear();
          ts+=s[j];
          myvs.PB(ts);
          id++;
        }
      }
    }

    //REP(j,myvs.size()) cout<<myvs[j]<<" ";
    //cout<<endl;
    int num=0;
    ts.clear();
    if(!zero) count(myvs,ts,0,num);
    out<<"Case #"<<(i+1)<<": "<<num<<endl;
  }
  in.close();
  out.close();
  return 0;
}
