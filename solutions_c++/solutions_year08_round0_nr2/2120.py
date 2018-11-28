#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define For(i,b) for(int i = 0; i < (int)b; ++i)
#define Fori(i,a,b) for(int i = a; i < (int)b; ++i)
#define Ford(i,a,b) for(int i = a; i >=b; --i)
#define All(t) t.begin(),t.end()
#define Sort(a) sort(All(a))
#define Fill(a,b) memset(a,b,sizeof(a))
#define Forstl(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define pb push_back
#define db(x) cout << #x << " = " << x << endl

using namespace std;

// Constants
const int INF = 1000000000;
const long double EPS = 1e-10L;
const long double PI = 3.14159265358979L;

void pr(vector<string>v)
{
 For(i,v.size())cout<<v[i]<<" ";
 cout<<endl;
}
void pr2(vector<int>v)
{
 For(i,v.size())cout<<v[i]<<" ";
 cout<<endl;
}
void print(vector<pair<int,int> >v)
{
 For(i,v.size())cout<<v[i].first<<" "<<v[i].second<<endl;
}
bool cmp(const vector<int>&a, const vector<int>&b)
{
  if(a[0]!=b[0])
    return a[0]<b[0];
  if(a[1]!=b[1])
    return a[1]<b[1];
  if(a[2]!=b[2])
    return a[2]<b[2];
  return a[3]<b[3];
}

bool cmp2(const pair<int, int>&a, const pair<int,int>&b)
{
  if(a.first!=b.first)
    return a.first<b.first;
  return a.second < b.second;
}

int main()
{
  ifstream fin("B-small-attempt0.in");
  ofstream fout("output.txt");
  //int cnt=0;
  int n;
  int t,na,nb;
  fin>>n;
  char cstr[256];
  //fin.getline(cstr,256);
  cout<<n<<endl;
  For(z,n)
  {
    db(z);
    fin>>t>>na>>nb;
   //db(t),db(na),db(nb);
    fin.getline(cstr,256);
    vector<vector<int> >v;
    int h1,m1,h2,m2;
    // 1: AB
    For(i,na)
    {
      fin.getline(cstr,256);
      //string str=cstr;
      //db(str);
      sscanf(cstr,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
      //db(h1),db(m1),db(h2),db(m2);
      //db("");
      vector<int>cur;
      cur.push_back(h1);
      cur.push_back(m1);
      cur.push_back(h2);
      cur.push_back(m2);
      cur.push_back(1);
      v.pb(cur);
    }
    For(i,nb)
    {
      fin.getline(cstr,256);
      //string str=cstr;
     // db(str);
      sscanf(cstr,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
      //db(h1),db(m1),db(h2),db(m2);
      //db("");
      vector<int>cur;
      cur.push_back(h1);
      cur.push_back(m1);
      cur.push_back(h2);
      cur.push_back(m2);
      cur.push_back(0);
      v.pb(cur);
    }
    sort(All(v),cmp);
    /*
    For(i,v.size())
    {
      pr2(v[i]);
    }
    */
    pair<int,int>res=make_pair(-1,-1);
    For(a,50) 
    {
    For(b,50)
    {
      //if(a!=2) continue;
      //if(b!=2) continue;
      vector<pair<int,int> >A,B;
      For(i,a)
      {
        A.pb(make_pair(-1,-1));
      }
      For(i,b)
      {
        B.pb(make_pair(-1,-1));
      }
      bool ok=1;
      
      Forstl(it,v)
      {
        /*
        cout<<"A"<<endl;
        print(A);
        cout<<"B"<<endl;
        print(B);
        */
        
        vector<int>cur=*it;
        pair<int,int> p = make_pair(cur[0],cur[1]);
        
        if(cur[4]) // AB
        {
          int idx=-1;
          vector<pair<int,int> >tmp;
          For(i,A.size())
          {
            if(cmp2(A[i],p) || (A[i].first==p.first && A[i].second ==p.second) )
            {
              idx=i;
              break;
            }
          }
          if(idx==-1)
          {
            ok=0;
            goto L;
          }
          else
          {
            tmp.clear();
            For(i,A.size())
            {
              if(i==idx)continue;
              tmp.pb(A[i]);
            }
            //db("tmp");
            //print(tmp);
            pair<int,int> ins = make_pair(cur[2],cur[3]);
            ins.second += t;
            if(ins.second>=60)
            {
              ins.second %= 60;
              ins.first++;
            }
            ins.first %= 24;
            B.pb(ins);
            A=tmp;
          }  // else    
        } // AB
        
        
        else // BA
        {
          int idx=-1;
          vector<pair<int,int> >tmp;
          For(i,B.size())
          {
            if(cmp2(B[i],p) || (B[i].first==p.first && B[i].second ==p.second) )
            {
              idx=i;
              break;
            }
          }
          if(idx==-1)
          {
            ok=0;
            goto L;
          }
          else
          {
            tmp.clear();
            For(i,B.size())
            {
              if(i==idx)continue;
              tmp.pb(B[i]);
            }
            //db("tmp");
            //print(tmp);
            pair<int,int> ins = make_pair(cur[2],cur[3]);
            ins.second += t;
            if(ins.second>=60)
            {
              ins.second %= 60;
              ins.first++;
            }
            ins.first %= 24;
            A.pb(ins);
            B=tmp;
          }  // else
        } // else BA
        
        
      } // Forstl
      if(ok)
        {
          pair<int,int>pi= make_pair(a,b);
          //db(pi.first),db(pi.second);
          if(res.first==-1)
          {
            res=pi;
          } else if(cmp2(pi,res))
            res=pi;   
      }
      L:continue;
    }
    } // For(a) For(b)
    //db(res.first),db(res.second);
    fout<<"Case #"<<z+1<<": "<<res.first<<" "<<res.second<<endl;
  }  // For(z,n)

    cin>>n;
   return 0;
};
