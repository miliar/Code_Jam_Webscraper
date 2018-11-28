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
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
string inp[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string out[] = {"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
int main()
{
	int mp[27];
    bool us[27];
    memset(mp, -1, sizeof(mp));
    memset(us, 0, sizeof(us));
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < out[i].size(); j++)
        {
            if (out[i][j] != ' ') {
                if (mp[out[i][j] - 'a'] != -1)
                    assert(mp[out[i][j] - 'a'] == inp[i][j] - 'a');
                mp[out[i][j] - 'a'] = inp[i][j] - 'a';
                us[inp[i][j] - 'a'] = 1;
            }
        }
    }
    mp['z'-'a'] = 'q' - 'a';
    mp['q'-'a'] = 'z' - 'a';
    //for(int i = 0 ; i < 26; i++)
      //  cout<<(char)(i+'a')<<" "<<(char)(mp[i]+'a')<<endl;
    
    int tc;
    cin>>tc;
    string s;
    getline(cin, s);
    int tot = tc;
    while(tc--) {
        getline(cin, s);
        for(int i = 0 ; i < s.size(); i++) {
            if (s[i] == ' ') continue;
            for(int j = 0 ; j < 26; j++)
                if (mp[j] + 'a' == s[i])
                {s[i] = j + 'a';break;}
        }
        cout<<"Case #"<<(tot - tc)<<": "<<s<<endl;
    }
}