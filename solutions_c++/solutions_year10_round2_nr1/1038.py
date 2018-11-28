#include <vector>
#include <list>
#include <map>
#include <set>
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

#define sz size()
#define PB push_back
#define clr(x) memset(x, 0, sizeof(x))
#define forn(i,n) for(__typeof(n) i = 0; i < (n); i++)
#define ford(i,n) for(int i = (n) - 1; i >= 0; i--)
#define forv(i,v) forn(i, v.sz)
#define For(i, st, en) for(__typeof(en) i = (st); i < (en); i++)

using namespace std;
typedef long long ll;

map <string, bool> drive;

void parse_path_existed(string path)
{
    stringstream ss(path);
    string tmp, upto("");
    while(getline(ss, tmp, '/'))
    {
        if(tmp != "")
        {
            upto = upto + "/" + tmp;
            drive[upto] = true;
            //printf("%s\n", upto.c_str());
        }
    }
}

int main()
{
	int cases = 0;
	cin >> cases;
	forn(i, cases)
	{
        long long ret = 0;
        drive.clear();
		int N, M;
		cin >> N >> M;
        string existed;
        getline(cin, existed);

        forn(j, N)
        {
            getline(cin, existed);
            parse_path_existed(existed);
        }

        string create;
        forn(j, M)
        {
            getline(cin, create);

            stringstream ss(create);
            string tmp, upto("");
            while(getline(ss, tmp, '/'))
            {
                if(tmp != "")
                {
                    upto = upto + "/" + tmp;
                    if(!drive[upto])
                    {
                        drive[upto] = true;
                        ret++;
                    }
                }
            }
        }

        printf("Case #%d: %lld\n", i+1, ret);
	}
	return 0;
}
