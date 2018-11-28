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
    string welcome("welcome to code jam");
    int welcome_size = welcome.size();
    forn(i, cases)
    {
        int ret = 0;
        string input;
        getline(cin, input);
        char init_c = welcome[0];
        int input_size = input.size();
        queue <node> Queue;
        forv(j, input)
            if(input[j] == init_c)
                Queue.push(node(0, j));
        while(!Queue.empty())
        {
            node t = Queue.front();
            Queue.pop();
            if(t.x == welcome_size-1)
            {
                ret++;
                if(ret > 100000000)
                    ret %= 10000;
                continue;
            }
            else
            {
                char next_c = welcome[t.x+1];
                for(int j=t.y+1; j<input_size; j++)
                    if(input[j] == next_c)
                        Queue.push(node(t.x+1, j));
            }
        }
        printf("Case #%d: %04d\n", i+1, ret % 10000);
    }

	return 0;
}
