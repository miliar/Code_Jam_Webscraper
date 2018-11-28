#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
#define vi vector<int>
#define vs vector<string>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    
    for(int t = 0; t < T; t++)
    {
        int C;
        scanf("%d", &C);
        vector < vector <char> > comb(26, vector <char> (26, '-'));
        vector < vector <char> > opp(26, vector <char> (26, '-'));

        for(int c = 0; c < C; c++)
        {
            char temp[4];
            scanf("%s", temp);
            comb[temp[0] - 'A'][temp[1] - 'A'] = comb[temp[1] - 'A'][temp[0] - 'A'] = temp[2];
        }

        int D;
        scanf("%d", &D);
        for(int d = 0; d < D; d++)
        {
            char temp[3];
            scanf("%s", temp);
            opp[temp[0] - 'A'][temp[1] - 'A'] = opp[temp[1] - 'A'][temp[0] - 'A'] = 'Y';
        }

        int N;
        scanf("%d", &N);
        char buf[201];
        scanf("%s", buf);
        string ans = "";
        char prev = '-';

        for(int i = 0; i < N; i++)
        {
            if(prev == '-')
            {
                ans.PB(buf[i]);
                prev = buf[i];
            }
            else
            {
                if(comb[prev - 'A'][buf[i] - 'A'] != '-')
                {
                    ans.erase(ans.end() - 1);
                    ans.PB(comb[prev - 'A'][buf[i] - 'A']);
                    prev = comb[prev - 'A'][buf[i] - 'A'];
                }
                else
                {
                    bool opposed = false;
                    for(int j = 0; j < SZ(ans); j++)
                    {
                        if(opp[buf[i] - 'A'][ans[j] - 'A'] == 'Y')
                            opposed = true;
                    }

                    if(opposed)
                    {
                        ans = "";
                        prev = '-';
                    }
                    else
                    {
                        ans.PB(buf[i]);
                        prev = buf[i];
                    }
                }
            }
        }

        printf("Case #%d: [", t + 1);
        for(int i = 0; i < SZ(ans); i++)
        {
            printf("%c", ans[i]);
            if(i != SZ(ans) - 1)
                printf(", ");
        }
        printf("]\n");
        
    }
    return 0;
}
