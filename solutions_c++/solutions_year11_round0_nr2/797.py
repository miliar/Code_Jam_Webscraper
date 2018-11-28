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

#define rep(i,n) for(int i = 0; i < (int)(n); ++i )

struct Problem
{
    int N,D,C;

    map< pair<char,char>, char > invokeRule;
    set< pair<char,char> > opposed;

    Problem()
    {
        invokeRule.clear();
        opposed.clear();

        cin >> C;

        rep(i,C)
        {
            string s;
            cin >> s;

            invokeRule[make_pair(s[0],s[1])] = s[2];
        }

        cin >> D;

        rep(i,D)
        {
            string s;
            cin >> s;

            opposed.insert( make_pair(s[0],s[1]) );
        }

        cin >> N;
    }

    bool canInvoke(char a, char b)
    {
        return invokeRule.count( make_pair(a,b) ) || invokeRule.count( make_pair(b,a) );
    }

    char invoke(char a, char b)
    {
        if( invokeRule.count( make_pair(a,b) ) )
            return invokeRule[ make_pair(a,b) ];

        return invokeRule[ make_pair(b,a) ];
    }

    bool isOpposed(char a, char b)
    {
        return opposed.count( make_pair(a,b) ) || opposed.count( make_pair(b,a) );
    }

    string parse()
    {
        vector<char> ans;
        char in;

        rep(i,N)
        {
            cin >> in;

            if(ans.size()==0)
            {
                ans.push_back( in );
            }
            else
            {
                ans.push_back(in);

                while(ans.size() >= 2 && canInvoke(ans[ans.size()-1], ans[ans.size()-2]))
                {
                    char invoked = invoke(ans[ans.size()-1], ans[ans.size()-2]);

                    ans.pop_back();
                    ans.pop_back();
                    ans.push_back(invoked);
                }

                bool clearMode = false;

                for(int i = 0; i < ans.size() && !clearMode; ++i)
                    for(int j = i+1; j < ans.size(); ++j)
                        if( isOpposed(ans[i], ans[j]) )
                        {
                            clearMode = true;
                            break;
                        }

                if( clearMode ) ans.clear();
            }
        }

        string res(ans.size(),' ');

        rep(i,ans.size()) res[i] = ans[i];

        return res;
    }
};

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("B-large.in","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    for(int cs = 1; cs <= T; ++cs)
    {
        string ans = Problem().parse();
        cout << "Case #" << cs << ": [" ;
        rep(i,ans.size())
        {
            if(i) cout <<", ";
            cout << ans[i];
        }
        cout << "]"<< endl;
    }

	return 0;
}
