#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>

using namespace std;

int solve()
{
    int N;
    deque< pair<int,int> > B,O;

    cin >> N;

    for(int i = 0; i < N; ++i)
    {
        char c;
        int b;
        cin >> c >> b;
        if(c=='O')
            O.push_back(make_pair(b,i));
        else
            B.push_back(make_pair(b,i));
    }

    int orange = 1, blue = 1, ans = 0, odir = 1, bdir = 1;

    while( O.size() || B.size() )
    {
        if(O.size() && B.size())
        {
            if(orange != O.front().first && blue != B.front().first)
                orange += odir, blue += bdir;
            else if(orange == O.front().first && blue != B.front().first)
            {
                if(B.front().second > O.front().second)
                {
                    O.pop_front();

                    if(O.size()) odir = orange < O.front().first ? 1 : -1;
                }

                blue += bdir;
            }
            else if(orange != O.front().first && blue == B.front().first)
            {
                if(O.front().second > B.front().second)
                {
                    B.pop_front();

                    if(B.size()) bdir = blue < B.front().first ? 1 : -1;
                }

                orange += odir;
            } else
            {
                if(O.front().second < B.front().second)
                {
                    O.pop_front();
                    if(O.size()) odir = orange < O.front().first ? 1 : -1;
                }
                else
                {
                    B.pop_front();

                    if(B.size()) bdir = blue < B.front().first ? 1 : -1;
                }
            }

        }
        else if(O.size())
        {
            if(orange != O.front().first)
                orange += odir;
            else
            {
                O.pop_front();

                if(O.size()) odir = orange < O.front().first ? 1 : -1;
            }
        }
        else //if(B.size())
        {
            if(blue != B.front().first)
                blue += bdir;
            else
            {
                B.pop_front();

                if(B.size()) bdir = blue < B.front().first ? 1 : -1;
            }
        }
        ++ans;
    }

    return ans;
}

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    for(int cs = 1; cs <= T; ++cs) cout << "Case #" << cs << ": " << solve() << endl;

	return 0;
}
