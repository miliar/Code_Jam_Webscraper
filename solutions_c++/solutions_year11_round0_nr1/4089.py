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

using namespace std;

typedef vector<int> VI;
typedef vector<pair<int,int> > VPI;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

int searchNextPos(char c, vector<pair<char,int> > v, int& vpos){
        for(int i=0;i<v.size();++i)
                if(c==v[i].first){
                        vpos = i;
                        return v[i].second;
                }
        vpos = 0;
        return 0;
}

bool move(vector<pair<char,int> > v, char p, int& cPos, int& nPos, int& vPos, char toPress){
        if (cPos == nPos){
                if (p == toPress){
                        for(int i=vPos + 1; i<v.size(); ++i)
                                if (v[i].first == p){
                                        nPos = v[i].second;
                                        vPos = i;
                                        return true;
                                }
                        nPos = 0;
                        return true;
                }
        }
        else if (cPos < nPos)
                ++cPos;
        else
                --cPos;
        return false;
}

void solve(int testCase){
        vector<pair<char,int> > v;
        int n,i;
        cin >> n;
        for(i=0;i<n;++i){
                static int x;
                static char c;
                cin >> c >> x;
                v.push_back(make_pair(c,x));
        }

        int nextPosO, nextPosB;
        bool changePress1,changePress2;
        char nextToPress = v[0].first;
        int currentPosO = 1, currentPosB = 1;
        int currentVectorPosO, currentVectorPosB;

        if (v[0].first == 'O'){
                nextPosO = v[0].second;
                currentVectorPosO = 0;
                nextPosB = searchNextPos('B',v,currentVectorPosB);
        }else{
                nextPosB = v[0].second;
                currentVectorPosB = 0;
                nextPosO = searchNextPos('O',v,currentVectorPosO);
        }

        //cerr << "Pos B: " << nextPosB << '\n';
        //cerr << "Pos O: " << nextPosO << '\n' << '\n';

        int sol = 0, toPress = 0;
        while (nextPosO || nextPosB){
                ++ sol;
                changePress1 = changePress2 = false;

                if (nextPosB)
                        changePress1 = move(v,'B',currentPosB,nextPosB,currentVectorPosB,nextToPress);
                if (nextPosO)
                        changePress2 = move(v,'O',currentPosO,nextPosO,currentVectorPosO,nextToPress);

                if (changePress1 || changePress2){
                        nextToPress = v[++toPress].first;
                }
        }
        printf("Case #%d: %d\n",testCase,sol);
}

int main()
{
        #ifndef ONLINE_JUDGE
        freopen("google.in","r",stdin);
        freopen("google.out","w",stdout);
        #endif

        int nTests;
        cin >> nTests;
        for(int i=1;i<=nTests;++i)
                solve(i);

        return 0;
}
