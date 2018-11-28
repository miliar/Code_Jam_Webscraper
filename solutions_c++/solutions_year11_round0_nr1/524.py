
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>

using namespace std;
#define sz(a) a.size()
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define REP(i,n) for(int i = 0 ; i < n ; i++)

int main()
{
    int t;
    cin >> t;
    int kase = 0;
    while(t--)
    {
              kase++;
              int n;
              cin >> n;
              char w[n];
              int p[n];
              REP(i,n) cin >> w[i] >> p[i];
              int freetimeO = 0,freetimeB = 0, posO=1, posB=1,jobtime=0;
              REP(i,n)
              {
                      if(w[i] == 'O')
                      {
                              if(freetimeO)
                              {
                                          int reqTime = abs(posO - p[i]);     
                                          if(freetimeO > reqTime) posO = p[i];
                                          else
                                          {
                                              if(p[i] > posO) posO += freetimeO;
                                              else posO -=freetimeO;
                                          }
                              }
                              freetimeO=0;
                              jobtime += abs(posO - p[i]) + 1;
                              freetimeB += abs(posO - p[i]) + 1;
                              posO = p[i];
                      }
                      if(w[i] == 'B')
                      {
                              if(freetimeB)
                              {
                                          int reqTime = abs(posB - p[i]);     
                                          if(freetimeB > reqTime) posB = p[i];
                                          else
                                          {
                                              if(p[i] > posB) posB += freetimeB;
                                              else posB -=freetimeB;
                                          }
                              }
                              freetimeB=0;
                              jobtime += abs(posB - p[i]) + 1;
                              freetimeO += abs(posB - p[i]) + 1;
                              posB = p[i];
                      }
                      //cout << posO << " " << posB << " " << jobtime << endl;
              }
              cout <<"Case #"<<kase<<": " << jobtime << endl;
                              
                                          
    }
    return 0;
}
