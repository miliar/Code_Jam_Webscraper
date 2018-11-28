#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

char base[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    freopen("B-large.out","w",stdout);
    int T, C, D, N;
    string str,str2;

    getline(cin,str);
    sscanf(str.c_str(),"%d",&T);

    for(int TT=0; TT<T; ++TT)
    {
        vector< map<char,char> > combi(26, map<char,char>() );
        vector< set<char> > opposed(26, set<char>() );

        getline(cin,str);

        istringstream strin(str);

        strin >> C;
        if(C)
        {
            for(int i=0; i<C; ++i)
            {
                strin >> str2;
                int mini = min(str2[0]-'A', str2[1]-'A');
                int maxi = max(str2[0]-'A', str2[1]-'A');
                combi[mini][maxi] = str2[2] - 'A';
            }
        }

        strin >> D;
        if(D)
        {
            for(int i=0; i<D; ++i)
            {
                strin >> str2;
                int mini = min(str2[0]-'A', str2[1]-'A');
                int maxi = max(str2[0]-'A', str2[1]-'A');
                opposed[mini].insert(maxi);
            }
        }

        strin >> N >> str2;
        string str3;
        char last, act;
        for(int i=0; i<str2.size(); ++i)
        {
            act = str2[i] - 'A';
            if(str3.size() > 0)
            {
                last = str3[str3.size() - 1] - 'A';
                int mini = min(last, act);
                int maxi = max(last, act);
                map<char,char>::iterator it2 = combi[mini].find(maxi);
                if(it2 != combi[mini].end())
                {
                    str3 = str3.substr(0,str3.size() - 1);
                    str3 = str3 + (char)(it2->second + 'A');
                }
                else
                {
                    bool clear = false;
                    for(int j=0; j<str3.size(); ++j)
                    {
                        int mini = min((char)(str3[j]-'A'), act);
                        int maxi = max((char)(str3[j]-'A'), act);
                        if(opposed[mini].find(maxi) != opposed[mini].end())
                        {
                            clear = true;
                        }
                    }
                    if(clear)
                    {
                        str3 = "";
                    }
                    else
                    {
                        str3 += (char)(act + 'A');
                    }
                }
            }
            else
            {
                str3 = str3 + (char)(act + 'A');
            }
        }
        cout << "Case #" << (TT+1) << ": [";
        for(int i=0; i<str3.size();++i)
        {
            if(i) cout << ", ";
            cout << str3[i];
        }
        cout << "]" << endl;
    }
}
