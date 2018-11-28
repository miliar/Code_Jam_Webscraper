#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define maxSize 1000

int n,m;
set<string> s;
set<string>::iterator it;
string src[maxSize];
string look[maxSize];
int cnt = 0;
void deal(string str)
{
    it = s.find(str);
    int tmplen = str.length();
    if(it!=s.end() || str=="/" || tmplen==0)
    {
        return ; 
    }
    else
    {
        int pos = str.find_last_of('/');
        string tmpstr = str.substr(0,pos);
        deal(tmpstr);
        cnt++;
        s.insert(str);
    }
    return ;
}
void getAC()
{
    for(int i=0;i<m;i++)
    {
        deal(look[i]);
    }
    cout<<cnt<<endl;
    return ;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin >>t;
    for(int cases=1;cases<=t;cases++)
    {
        cin >> n >> m;
        s.clear();
        for(int i=0;i<n;i++)
        {
            cin >> src[i];
            //s.insert(src[i]);
            int len = src[i].length();
            string str ="/";
            for(int j=1;j<len;j++)
            {
                if(src[i][j]=='/' || j==(len-1))
                {
                    if(j==(len-1))
                        str +=src[i][j];
                    it = s.find(str);
                    if(it==s.end())
                        s.insert(str);
                    if(j!=len-1)
                        str +=src[i][j];
                }
                else 
                    str += src[i][j];
            }
        }
        for(int i=0;i<m;i++)
            cin >> look[i];
        cnt =0;
        printf("Case #%d: ",cases);
        getAC();
    }
    return 0;
}
