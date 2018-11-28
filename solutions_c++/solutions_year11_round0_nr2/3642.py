/***************************************************
 * Author: Alexandru Palcuie
 * Country: Romania
 * Contest: Google CodeJam
 * Email: alex [dot] palcuie [at] gmail [dot] com
 * Website: http://palcu.blogspot.com/
 * Year: 2011
****************************************************/

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
#include <cstring>

using namespace std;

typedef vector<int> VI;
typedef vector<pair<int,int> > VPI;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

//Constants

//Global Vars
const int NMAX = 100;
string str;
char combine[NMAX][NMAX];
bool oppose[NMAX][NMAX];

//Structs

//Solve Functions
int ltoint(char c){
        return c-'A';
}

void combineF(){
        bool hasCombined = false;
        int j;
        for (int i=1; i<str.size(); ++i){
                static int a,b;
                a = ltoint(str[i-1]);
                b = ltoint(str[i]);
                if(combine[a][b]) {
                        if (combine[a][b]){
                        //cerr<<str<<endl;
                        string tmp; tmp.push_back(combine[a][b]);
                        str.insert(i-1,tmp);
                        //cerr<<str<<endl;
                        str.erase(i,2); --i;}
                }
                else{
                        for (j=i-1; j>=0; --j)
                                if (oppose[b][ltoint(str[j])]){
                                        str.erase(0,i+1);
                                        i = 0;
                                        if (i<0) i=0;
                                        break;
                                }
                }
        }
}

void delF(){
        int i,j;
        for (i=0;i<str.size();++i)
                for(j=i+1;j<str.size();++j)
                        if(oppose[ltoint(str[i])][ltoint(str[j])]){
                                str.erase(i,j-i+1);
                                //cerr << *(str.begin()+i) << '\n' << *(str.begin()+j) << '\n';
                        }
}

void solve(int testCase){
        memset(combine,0,sizeof(combine));
        memset(oppose,0,sizeof(oppose));
        str.clear();

        int nCombine, nOppose;
        cin >> nCombine;
        for (int i=0; i<nCombine; ++i){
                static string s;
                static int a,b;
                cin >> s;
                a = ltoint(s[0]);
                b = ltoint(s[1]);
                combine[a][b] = s[2];
                combine[b][a] = s[2];
        }

        cin >> nOppose;
        for (int i=0; i<nOppose; ++i){
                static string s;
                static int a,b;
                cin >> s;
                a = ltoint(s[0]);
                b = ltoint(s[1]);
                oppose[a][b] = true;
                oppose[b][a] = true;
        }

        int sizeString; cin >> sizeString;
        cin >> str;
        //str.push_back('1'); //just a delimiter

        /*bool hasCombined = true, hasDeleted = true;
        while (hasCombined|| hasDeleted){
                hasCombined = hasDeleted = false;
                hasCombined = combine();
                hasDeleted = del();
        }*/

        combineF();
        //delF();

        printf("Case #%d: [",testCase);
        if (str.size()){
                int sizestr = str.size()-1;
                for(int i=0;i<sizestr;++i)
                        cout << str[i] << ", ";
                cout << str[sizestr] << "]\n";
        }
        else
                cout << "]\n";
}


int main()
{
        #ifndef ONLINE_JUDGE
        freopen("magic.in","r",stdin);
        freopen("magic.out","w",stdout);
        #endif

        int nTests;
        cin >> nTests;
        for(int i=1;i<=nTests;++i)
                solve(i);

        return 0;
}
