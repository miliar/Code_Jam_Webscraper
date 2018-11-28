#include <iostream>
#include <string>
using namespace std;

struct node
{
    int cc;
    int father, child[160];
    string name;
};

int N, M, T, Ti, NC, ans;
node ND[16000];

void init()
{
     cin >> N >> M;
}

int checkChild(int x, string name)
{
    int i, ret;

    for (i = 1; i <= ND[x].cc; i++)
        if (ND[ND[x].child[i]].name == name)
            return ND[x].child[i];

    NC++;
    ND[NC].name = name;
    ND[x].child[++ND[x].cc] = NC;
    ND[NC].father = x;
    
    return NC;
}

int checkChild2(int x, string name)
{
    int i, ret;

    for (i = 1; i <= ND[x].cc; i++)
        if (ND[ND[x].child[i]].name == name)
            return ND[x].child[i];

    NC++;
    ND[NC].name = name;
    ND[x].child[++ND[x].cc] = NC;
    ND[NC].father = x;
    ans++;
    return NC;
}

void work()
{
    int i, j, p, wc;
    string tmp, w[100];
    int x;

  //  memset(ND, 0, sizeof(ND));

    for (i = 0; i < 16000; i++)
    {
        ND[i].cc = 0;
        ND[i].father = 0;
        for (j = 0; j < 160; j++)
            ND[i].child[j] = 0;
    }
    
    ans = 0;
    NC = 1;
    for (i = 1; i <= N; i++)
    {
        cin >> tmp;
        p = 0;
        wc = 0;
        for (j = 1; j < tmp.length(); j++)
            if (tmp[j] == '/')
            {
                w[++wc] = tmp.substr(p + 1, j - p - 1);
                p = j;
            }
        w[++wc] = tmp.substr(p + 1, j - p - 1);

        x = 1;
        for (j = 1; j <= wc; j++)
        {
            x = checkChild(x, w[j]);
        }
    }

    for (i = 1; i <= M; i++)
    {
        cin >> tmp;
        p = 0;
        wc = 0;
        for (j = 1; j < tmp.length(); j++)
            if (tmp[j] == '/')
            {
                w[++wc] = tmp.substr(p + 1, j - p - 1);
                p = j;
            }
        w[++wc] = tmp.substr(p + 1, j - p - 1);

        x = 1;
        for (j = 1; j <= wc; j++)
        {
            x = checkChild2(x, w[j]);
        }
    }
    
    cout << "Case #" << Ti << ": " << ans << endl;
}

int main()
{
    cin >> T;
    for (Ti = 1; Ti <= T; Ti++)
    {
        init();
        work();
    }

  //  system("pause");
    return 0;
}
