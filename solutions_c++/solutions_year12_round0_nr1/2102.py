#pragma comment(linker,"/STACK:16777216")
#pragma warning ( disable: 4786)
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

#define pb push_back

#define vi vector<int>
#define vf vector<float>
#define vd vector<double>
#define vi64 vector<int64>
#define vs vector<string>
#define vc vector<char>

#define int64 long long

#define mii map<int,int>
#define mic map<int,char>
#define mci map<char,int>
#define mcc map<char,char>

#define msi map<string,int>
#define mis map<int,string>

mii mymap;

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,a,b,c,d,m,n;
	char ch;
	string st[6];
	st[0] = "ynficwlbkuomxsevzpdrjgthaq";
	st[1] = "abcdefghijklmnopqrstuvwxyz";

    map<char,char> lan;
    for(j = 0;j < st[0].size();j++)
        lan[st[0][j]] = st[1][j];

    lan[' '] = ' ';
    map<char,char>::iterator it;
   // showing contents:
      //cout << "lan contains:\n";
      //for ( it=lan.begin() ; it != lan.end(); it++ )
        //cout << (*it).first << " => " << (*it).second << endl;
    cin >> m;
    getchar();
    c = 0;
    while(m--)
    {
        ++c;
        printf("Case #%d: ",c);
        while((ch = getchar()) != '\n')
        {
            cout << lan[ch];
        }
        cout << endl;
    }
	return 0;
}
