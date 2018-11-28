#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<cmath>
using namespace std;

int main()
{
    int t,count = 0;
    ifstream fin("A-large.in");
    ofstream fout("output1.in");
    vector <int> a;
    vector <int> b;
    vector <int> c;
    fin>>t;
    while(t--)
    {
              int n;
              fin>>n;
              a.clear();b.clear();c.clear();
              for(int i=0;i<n;i++)
              {
                      char ch;
                      int tmp;
                      fin>>ch;
                      if(ch == 'O')
                      {
                            fin>>tmp;
                            a.push_back(tmp);
                            c.push_back(1);
                      }
                      else
                      {
                            fin>>tmp;
                            b.push_back(tmp);
                            c.push_back(0);
                      }
              }
              
              for(int i=0;i<a.size();i++)
              cout<<a[i]<<" ";
              cout<<endl;
              for(int i=0;i<b.size();i++)
              cout<<b[i]<<" ";
              cout<<endl;
              for(int i=0;i<c.size();i++)
              cout<<c[i]<<" ";
              cout<<endl;
              
              int ans = 0;
              int apos = 1;
              int bpos = 1;
              int ai = 0,bi = 0;
              for(int i=0;i<n;i++)
              if(c[i] == 1)
              {
                  int dist = a[ai] - apos;
                  if(dist < 0)dist = -dist;
                  cout<<"dist "<<dist<<endl;
                  apos = a[ai];
                  int steps = dist + 1;
                  int dist2 = b[bi] - bpos;
                  if(dist2 < 0)dist2 = -dist2;
                  if(dist2 > dist)
                  {if(b[bi] > bpos)bpos += steps;
                  else bpos -= steps;}
                  else bpos = b[bi];
                  ans += steps;
                  ai++;
                  cout<<"apos "<<apos<<endl;
                  cout<<"bpos "<<bpos<<endl;
                  cout<<"ans "<<ans<<endl;
              }
              else
              {
                  int dist = b[bi] - bpos;
                  if(dist < 0)dist = -dist;
                  cout<<"dist "<<dist<<endl;
                  bpos = b[bi];
                  int steps = dist + 1;
                  int dist2 = a[ai] - apos;
                  if(dist2 < 0)dist2 = -dist2;
                  if(dist2 > dist)
                  {if(a[ai] > apos)apos += steps;
                  else apos -= steps;}
                  else apos = a[ai];
                  ans += steps;
                  bi++;
                  cout<<"apos "<<apos<<endl;
                  cout<<"bpos "<<bpos<<endl;
                  cout<<"ans "<<ans<<endl;
                  
              }
              count++;
              fout<<"Case #"<<count<<": "<<ans<<endl;
    }
    //system("pause");
    return 0;
}
