
/***** Author : Akshay *****/
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#include <cmath>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#include <utility>
#include <numeric>
#include <map>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <iomanip>
#include <set>
#include <fstream>

using namespace std;

#define REP(a,b) for(int a=0;a<b;a++)
#define FOR(a,b,c) for(int a=b;a<c;a++)
#define FORD(a,b,c) for(int a=b;a>=c;a--)


#define LEN(x) ((int)x.length())
#define SZ(x) ((int)x.size())
#define ALL(x) x.begin(), x.end()
#define MP(x,y) make_pair(x,y)
#define PB(x) push_back(x)
#define INF 1000000000
#define MOD 10000007
#define toString(x) #x
#define add(a,b) toString(a##b)
//#define __ONLINE__JUDGE__ 1


typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int, ii> Lii;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<string> VS;

int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};

/* Function for string split . If string starts with de-lim then call split(s.substr(1,s.length()),DELIM);
 *    else call split(s,DELIM);*/
std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


std::vector<std::string> split(const std::string &s, char delim) 
{
    std::vector<std::string> elems;
    return split(s, delim, elems);
}
int iter,t;
bool gogo(vector<string> inp)
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++) if(inp[i][j]=='.') return true;
    }
    return false;
}
bool check(vector<string> inp,char ch)
{
    //check row
    for(int i=0;i<4;i++)
    {
        int ct=0;
        for(int j=0;j<4;j++)
        {
            ct = ( (inp[i][j] =='T' || inp[i][j]==ch) ? ct+1 : ct);
        }
        if(ct == 4 ) return true;
    }
    //Check colums
    for(int i=0;i<4;i++)
    {
        int ct=0;
        for(int j=0;j<4;j++)
        {
            ct = ( (inp[j][i] =='T' || inp[j][i]==ch) ? ct+1 : ct);
        }
        if(ct == 4 ) return true;
    }
    //check diagonal
    int ct=0;
    for(int i=0;i<4;i++)
    {
        ct = ( (inp[i][i] =='T' || inp[i][i]==ch) ? ct+1 : ct);
        if(ct == 4 ) return true;
    }
    ct=0;
    for(int i=0;i<4;i++)
    {
        ct = ( (inp[i][4-i-1] =='T' || inp[i][4-i-1]==ch) ? ct+1 : ct);
        if(ct == 4 ) return true;
    }
    return false;
}
int main()
{
    scanf("%d",&t);iter=1;
    while(t--)
    {
        vector<string> inp;
        string str;
        for(int i=0;i<4;i++) { cin >> str ; inp.push_back(str);}
        bool isCellEmpty = gogo(inp);
        if(isCellEmpty)
        {
            bool XWin = check(inp,'X');
            if(!XWin)
            {
                bool OWin = check(inp,'O');
                if(!OWin)
                {
                    cout << "Case #" << iter << ":" << " " << "Game has not completed";
                }
                else
                {
                    cout << "Case #" << iter << ":" << " " << "O won";
                }
            }
            else
            {
                cout << "Case #" << iter << ":" << " " << "X won";
            }
        }
        else
        {
            bool XWin = check(inp,'X');
            if(!XWin)
            {
                bool OWin = check(inp,'O');
                if(!OWin)
                {
                    cout << "Case #" << iter << ":" << " " << "Draw";
                }
                else
                {
                    cout << "Case #" << iter << ":" << " " << "O won";
                }
            }
            else
            {
                cout << "Case #" << iter << ":" << " " << "X won";
            }
        }
        iter++;
        cout << "\n";
    }
    return 0;
}
