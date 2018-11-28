#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
using namespace std;
string getPath(string path)
{
       int slash = path.rfind("/");
       return path.substr(0,slash);
}

string getName(string path)
{
       int slash = path.rfind("/");       
       return path.substr(slash + 1);
}
int main()
{
        //cout << (getName("/") == "");
       // while(1);
       int cas, cases;
       cin >> cases;
       for(cas = 1; cas <= cases; cas++)
       {
               int n, m;
               cin >> n >> m;
               int cnt = 0;
               vector <string> a(n,"");
               vector <string> p(n,"");
               int i, j;
               string temp;
               for(i = 0; i < n; i++)
               {
                     cin >> temp;      
                     a[i] = getName(temp);
                     p[i] = getPath(temp);
               }
              // for(i = 0; i < n; i++)
                //     cout << p[i] << "  /  " << a[i] << endl;
               //cout << endl << endl << endl;
               string cur;
               for(i = 0; i < m; i++)
               {
                     cin >> cur;      
                     string name = getName(cur);
                     string path = getPath(cur);
                    // cout << "i = " << i << endl;
                    //string path = cur;
                    //string name = "";
                     while(1)
                     {
                          //if(path == "/")
                            //      break;
                          bool done =  false;
                          bool parent = false;
                          for(j = 0; j < a.size(); j++)
                          {
                               if(p[j] == path && a[j] == name)      
                                      done = true;
                               else if(p[j] == path)
                                    parent = true;
                          }
                          if(done)
                                  break;
                          else if(parent)
                          {
                                    a.push_back(name);
                                    p.push_back(path);
                                    cnt++;
                                    break;
                          }
                          else
                          {
                              a.push_back(name);
                              p.push_back(path);
                              cnt++;
                              if(path == "")
                                      break;
                              //if(path.rfind("/") == 0)
                                //                 break;
                              name = getName(path);
                              path = getPath(path);


                          }
                          //if(path == "/")
                            //      break;
                     }
               }
               //for(i = 0; i < a.size(); i++)
                //     cout << p[i] << "  /  " << a[i] << endl;
               cout << "Case #" << cas << ": " << cnt << endl;
               //cout << endl << endl << endl;
             
       }
        return 0;
}
