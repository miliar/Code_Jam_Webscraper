#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <algorithm>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>


using namespace std;

string getString(){char c[1024]=""; scanf("%s",c); return c;}
long long getLong(){long long x= 0; scanf("%lld",&x); return x;}
int getInt() { int x=0; scanf("%d",&x); return x;}
void filer(){freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);}


int main(int argc, char** argv)
{
    filer();
    int cases=getInt();

    vector<char> bot;
    vector<int> but;
    string s;
    int buttons,opos,bpos,tm,otm,btm;
    for(int i=0;i<cases;i++){
        buttons=getInt();
        bot.erase(bot.begin(),bot.end());
        but.erase(but.begin(),but.end());
        cout<<"Case #"<<i+1<<": ";

        for(int j=0;j<buttons;j++){
                s=getString();
                bot.push_back(s[0]);
                but.push_back(getInt());

            }
         bot.push_back(bot[bot.size()-1]);
        but.push_back(but[but.size()-1]);
        /*
        for(int j=0;j<buttons;j++)
            {
                cout<<bot[j]<<" ";
                cout<<but[j]<<" ";

            }*/
        opos=1;
        bpos=1;
        otm=0;
        btm=0;
        for(int j=0;j<bot.size()-1;j++){
                    if(bot[j]=='O')
                        {
                            otm+=abs(but[j]-opos) + 1;
                            opos=but[j];
                            if(bot[j+1]=='O')
                                    continue;
                            else {
                                if(but[j+1]>bpos)
                                    {
                                        bpos=bpos+(otm-btm);
                                        bpos= (bpos>but[j+1])?but[j+1]:bpos;
                                    }
                                else {
                                        bpos=bpos-(otm-btm);
                                        bpos= (bpos<but[j+1])?but[j+1]:bpos;

                                    }
                                btm=otm;
                            }
                        }

                    if(bot[j]=='B')
                        {
                            btm+=abs(but[j]-bpos) + 1;

                            bpos=but[j];
                            if(bot[j+1]=='B')
                                    continue;
                            else {
                                if(but[j+1]>opos)
                                    {
                                        opos=opos+(btm-otm);
                                        opos= (opos>but[j+1])?but[j+1]:opos;
                                    }
                                else {
                                        opos=opos-(btm-otm);
                                        opos= (opos<but[j+1])?but[j+1]:opos;

                                    }
                                otm=btm;
                            }
                        }

        }

    if(btm>otm)
    cout<<btm<<endl;
else cout<<otm<<endl;

    }

    return 0;
}
