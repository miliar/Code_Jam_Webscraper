
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>

using namespace std;
#define sz(a) a.size()
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair

int main()
{
    int t;
    cin >> t;
    int kase=0;
    while(t--)
    {
              kase++;
              //freopen("a.in","r",stdin);
              int n1,n2,n3;
              cin >>n1;
              string x[n1];
              for(int i=0; i < n1 ; i++)
              {
                      
                      cin >> x[i];
              }
              cin >> n2;
              vector<string> y;
              for(int i=0; i < n2 ; i++)
              {
                      string tmp;
                      cin >> tmp;
                      y.pb(tmp);
                      reverse(all(tmp));
                      y.pb(tmp);
              }
              cin >> n3;
              string s;
              cin >> s;
              vector<char> list;
              //fclose(stdin);
              //freopen("a.out","w",stdout);
              for(int i=0; i < s.size() ; i++)
              {
                      char a = s[i];
                      int kkk = 0;
                      int flag = 0;
                      
                      if(flag==0 && sz(list) > 0)//not cleared ...then do other job
                      {
                      
                          char b = list[list.size()-1];
                          string c;
                          c.pb(a); c.pb(b);
                          for(int j=0;j < n1 ;j++)
                          {
                                  string xx;
                                  xx.pb(x[j][0]);xx.pb(x[j][1]);
                                  char q = x[j][2];
                                  if((xx.compare(c) == 0))
                                  {
                                                    kkk = 1;
                                      list.pop_back();
                                      list.pb(q);break;
                                  }
                                  reverse(all(c));
                                  if((xx.compare(c) == 0))
                                  {
                                                    kkk = 1;
                                      list.pop_back();
                                      list.pb(q);break;
                                  }
                                  
                          }
                          
                      }
                      if(flag==0 && kkk == 0)
                        list.pb(s[i]);
                      if(kkk==0)
                      for(int j = 0; j<list.size();j++)//claering loop
                      {
                              if(flag == 1) break;
                              char b = list[j];
                              string c;
                              c.pb(a);c.pb(b);
                              for(int p = 0 ; p < sz(y) ; p++)
                              {
                                  if(y[p].compare(c) == 0)
                                  {
                                            list.clear();
                                            flag = 1;break;
                                  }
                              }
                      }
                  /*    cout << "=======================\n";
              for(int i = 0 ; i < list.size() ; i++)
              {
                      cout << list[i] << " " ;
              }
              cout << "\n";
              cout <<"===================\n";*/
                      
              }              
              //cout << sz(list) << endl;  
              cout << "Case #"<<kase<<": ";
              if(sz(list) == 0) cout << "[]\n";
              else
              {
              cout << "[";    
              for(int i = 0 ; i < list.size()-1 ; i++)
              {
                      cout << list[i] << ", " ;
              }
              
              cout << list[list.size()-1] << "]";
              cout << "\n";
              }
    }
    return 0;
}                              
                            
