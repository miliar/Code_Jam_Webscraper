#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>
#include <string>
#include <cstring>
using namespace std;
#define sz(x) (int)x.size()
int L, D, N;
string dic[5010];
int main()  {  freopen("Abig.out", "w", stdout);
    cin >> L >> D >> N;
    for(int i = 0; i < D; i++)  {
        cin >> dic[i];
    }
    int Case = 1;
    while(N--)  {
        string s;
        cin >> s;
        vector<string> let;
        for(int i = 0; i < sz(s); i++)  {
            if(s[i] == '(')  {
                int j = i + 1;
                while(s[j] != ')')  j++;
                string tmp;
                for(int k = i + 1; k < j; k++)  tmp += s[k];
                let.push_back(tmp);
                i = j;
            }
            else  {
                string tmp;
                tmp += s[i];
                let.push_back(tmp);
            }
        }
        int ans = 0;
        //cout << sz(let) << endl;
        //for(int i = 0; i< sz(let); i++) cout << let[i] << endl;
        for(int i = 0; i < D; i++) {
            bool flag = 1;
            if(sz(let) == sz(dic[i]))  {
                for(int j = 0; j < sz(dic[i]); j++)  {
                    if(let[j].find(dic[i][j], 0) == string::npos)  {
                        flag = 0;
                        break;
                    }
                }
            }
            else flag = 0;
            ans += flag;
        }
        printf("Case #%d: %d\n", Case++, ans);
    }
    return 0;
}
                        
                
                
