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

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int testCase=1; testCase<=T; testCase++) {
        int N, M;
        cin >> N >> M;
        set<string> dirs;
        for (int i=0; i<N; i++) {
            string tmp;
            cin >> tmp;
            for (int j=1; j<tmp.size(); j++)
                if (tmp[j]=='/') 
                    dirs.insert(tmp.substr(0, j));
            dirs.insert(tmp);
        }
        set<string> need;
        for (int i=0; i<M; i++) {
            string tmp;
            cin >> tmp;
            for (int j=1; j<tmp.size(); j++)
                if (tmp[j]=='/') 
                    need.insert(tmp.substr(0, j));
            need.insert(tmp);
        }
        vector<string> res(need.size());
        vector<string>::iterator itres;
        itres = set_difference(need.begin(), need.end(), dirs.begin(), dirs.end(), res.begin());
        cout << "Case #" << testCase << ": " << int(itres - res.begin()) << endl;
    }

    return 0;
}
