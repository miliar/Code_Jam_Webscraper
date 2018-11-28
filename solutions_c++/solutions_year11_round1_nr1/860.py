#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("b.out");

    int tot, count = 1;
    long long int pd, pg, n;

    cin>>tot;
    while (tot--)
    {
        cin>>n>>pd>>pg;

        bool flag = true;
        if (n > 100)n = 100;

        if (pd == 0 && pg == 0)
            flag = false;
        else
        {
            for (int i = 1; i <= n; i++)
            {
                if (i * pd % 100 == 0)
                {
                    if ((pg < 100 && pg > 0) || (pd == 100 && pg == 100))
                    {
                        flag = false;
                        break;
                    }
                }
            }
        }

        if (!flag)cout<<"Case #"<<count++<<": Possible"<<endl;
        else cout<<"Case #"<<count++<<": Broken"<<endl;
    }
    return 0;
}
