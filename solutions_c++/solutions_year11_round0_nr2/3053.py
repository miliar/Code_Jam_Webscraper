#include <iostream>
using namespace std;

pair<char,char> combiners[256];
int destroyers[256][256];
int flags[256];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,tci,tc,nc,nd,n;
    cin >> tc;
    string str,res;
    for (tci = 1;tci <= tc;++tci)
    {
        memset(combiners,0,sizeof(combiners));
        memset(destroyers,0,sizeof(destroyers));
        memset(flags,0,sizeof(flags));
        res = "";
        cin >> nc;
        for (i = 0;i < nc;++i)
        {
            cin >> str;
            combiners[str[0]].first = str[1];
            combiners[str[0]].second = str[2];
            combiners[str[1]].first = str[0];
            combiners[str[1]].second = str[2];
        }
        cin >> nd;
        for (i = 0;i < nd;++i)
        {
            cin >> str;
            destroyers[str[0]][str[1]] = 1;
            destroyers[str[1]][str[0]] = 1;
        }
        cin >> n;
        cin >> str;
        flags[str[0]] = 1;res.push_back(str[0]);
        for (i = 1;i < n;++i)
        {
            if (combiners[str[i]].first == res[res.length() - 1])
            {
                --flags[res[res.length() - 1]];
                res[res.length() - 1] = combiners[str[i]].second;
                ++flags[res[res.length() - 1]];
                for (j = 'A';j <= 'Z';++j)
                    if (destroyers[res[res.length() - 1]][j] == 1 && flags[j] != 0)
                    {
                        res = "";
                        memset(flags,0,sizeof(flags));
                        break;
                    }
                continue;
            }
            ++flags[str[i]];
            res += str[i];
            for (j = 'A';j <= 'Z';++j)
                if (destroyers[str[i]][j] == 1 && flags[j] != 0)
                {
                    res = "";
                    memset(flags,0,sizeof(flags));
                    break;
                }
        }
        cout << "Case #" << tci << ": [";
        if (res != "")
        {
            cout << res[0];
            for (i = 1;i < res.length();++i) cout << ", " << res[i];
        }
        cout << ']' << endl;
    }
    //system("pause");
    fclose(stdin);
    fclose(stdout);
    return 0;
}
