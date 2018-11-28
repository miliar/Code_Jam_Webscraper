#include <cstdlib>
#include <iostream>
#include <string>
#include <map>


using namespace std;

int main(int argc, char *argv[])
{
    int c, n=0;
    cin >> c;
    string sa[10005];
    bool   s_used[10005];
    map<string, bool> sflag;
    for(;c;--c)
    {
               ++n;
               int sn;
               cin >> sn;
               sflag.clear();
               char name[2001];
               cin.getline(name, 2000);
               for(int i=0;i<sn;++i)
               {
                       string tem;
                       cin.getline(name, 2000);
                       //cin.get >> tem;
                       tem = name;
                       sflag[tem] = false;
 //                      cout << tem << endl;
               }
               int cn, left = sn;
               cin >> cn;
               int stimes = 0;
               cin.getline(name, 2000);
               for(int i=0;i<cn;++i)
               {
                       string temp;
                       cin.getline(name, 2000);
                       temp = name;
                       if(!sflag[temp])
                       {
                                       if(left == 1)
                                       {
                                               ++stimes;
                                               map<string, bool>::iterator itr;
                                               for(itr = sflag.begin(); itr != sflag.end(); ++itr)
                                               {
                                                       itr->second = false;
                                               }
                                               left = sn;
                                       }
                                       --left;
                                       sflag[temp] = true;
                       }
               }
               cout << "Case #" << n << ": " << stimes << endl;
    }


    return EXIT_SUCCESS;
}
