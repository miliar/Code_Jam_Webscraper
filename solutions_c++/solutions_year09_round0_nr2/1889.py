#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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

#define sz size()
#define PB push_back
#define clr(x) memset(x, 0, sizeof(x))
#define forn(i,n) for(__typeof(n) i = 0; i < (n); i++)
#define ford(i,n) for(int i = (n) - 1; i >= 0; i--)
#define forv(i,v) forn(i, v.sz)
#define For(i, st, en) for(__typeof(en) i = (st); i < (en); i++)

using namespace std;
typedef long long ll;

class node
{
    public:
        node(int X, int Y): x(X), y(Y)
        {
        }
        int x, y;
};

int main()
{
	int cases = 0;
    scanf("%d\n", &cases);
    forn(i, cases)
    {
        int width = 0, height = 0;
        scanf("%d %d\n", &height, &width);
        vector <vector <int> > map(height, vector <int> (width, 0));
        vector <vector <bool> > visit(height, vector <bool> (width, false));
        vector <vector <char> > arrow(height, vector <char> (width, 'w'));
        vector <vector <char> > ret(height, vector <char> (width, 'a'));

        forn(j, height)
            forn(k, width)
                cin >> map[j][k];
        forv(j, map)
        {
            forv(k, map[j])
            {
                vector <int> neighbors;
                if(j-1 >= 0 && j-1 < height)
                    neighbors.PB(map[j-1][k]);
                if(k-1 >= 0 && k-1 < width)
                    neighbors.PB(map[j][k-1]);
                if(k+1 >= 0 && k+1 < width)
                    neighbors.PB(map[j][k+1]);
                if(j+1 >=0 && j+1 < height)
                    neighbors.PB(map[j+1][k]);
                int min_n = neighbors.empty() ? map[j][k] : *min_element(neighbors.begin(), neighbors.end());
                if(map[j][k] <= min_n)
                    arrow[j][k] = 'o';
                else
                {
                    if(j-1 >= 0 && j-1 < height && map[j-1][k] == min_n)
                    {
                        arrow[j][k] = 'u';
                        continue;
                    }
                    if(k-1 >= 0 && k-1 < width && map[j][k-1] == min_n)
                    {
                        arrow[j][k] = 'l';
                        continue;
                    }
                    if(k+1 >= 0 && k+1 < width && map[j][k+1] == min_n)
                    {
                        arrow[j][k] = 'r';
                        continue;
                    }
                    if(j+1 >=0 && j+1 < height && map[j+1][k] == min_n)
                    {
                        arrow[j][k] = 'd';
                        continue;
                    }
                }
            }
        }
        int label = 0;
        forv(j, visit)
        {
            forv(k, visit[j])
            {
                if(!visit[j][k])
                {
                    int ox = j, oy = k;
                    while(arrow[ox][oy] != 'o')
                    {
                        switch(arrow[ox][oy])
                        {
                            case 'u':
                                ox--;
                                break;
                            case 'l':
                                oy--;
                                break;
                            case 'r':
                                oy++;
                                break;
                            case 'd':
                                ox++;
                                break;
                        }
                    }
                    stack <node> Stack;
                    Stack.push(node(ox, oy));
                    while(!Stack.empty())
                    {
                        node t = Stack.top();
                        Stack.pop();
                        ret[t.x][t.y] = 'a'+label;
                        visit[t.x][t.y] = true;
                        if(t.x-1 >= 0 && t.x-1 < height && arrow[t.x-1][t.y] == 'd')
                            Stack.push(node(t.x-1, t.y));
                        if(t.y-1 >= 0 && t.y-1 < width && arrow[t.x][t.y-1] == 'r')
                            Stack.push(node(t.x, t.y-1));
                        if(t.y+1 >= 0 && t.y+1 < width && arrow[t.x][t.y+1] == 'l')
                            Stack.push(node(t.x, t.y+1));
                        if(t.x+1 >=0 && t.x+1 < height && arrow[t.x+1][t.y] == 'u')
                            Stack.push(node(t.x+1, t.y));
                    }
                    label++;
                }
            }
        }
        printf("Case #%d:\n", i+1);
        forv(j, ret)
        {
            forv(k, ret[j])
            {
                printf("%c", ret[j][k]);
                if(k != ret[j].size()-1)
                    printf(" ");
            }
            printf("\n");
        }
    }
	return 0;
}
