
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

#define REP(i,n) for(int i=0; i<(int)(n); ++i)


class Problem
{
private:
    string R1,R2,R3,R4;

    int T;
    int CASE;
    char MAP[4][4];

public:
	Problem()
	{
        R1="X won";
        R2="O won";
        R3="Draw";
        R4="Game has not completed";
	}

    bool checkWon(char P)
    {
        bool ret=true;
        REP(i,4)
        {
            ret=true;
            REP(j,4)
            {
                if(MAP[i][j]==P || MAP[i][j]=='T');
                else
                {
                    ret=false;
                    break;
                }
            }
            if(ret) return true;
        }
        REP(i,4)
        {
            ret=true;
            REP(j,4)
            {
                if(MAP[j][i]==P || MAP[j][i]=='T');
                else
                {
                    ret=false;
                    break;
                }
            }
            if(ret) return true;
        }
        ret=true;
        REP(i,4)
        {
            if(MAP[i][i]==P || MAP[i][i]=='T');
            else
            {
                ret=false;
                break;
            }
        }
        if(ret) return true;
        ret=true;
        REP(i,4)
        {
            if(MAP[i][3-i]==P || MAP[i][3-i]=='T');
            else
            {
                ret=false;
                break;
            }
        }
        if(ret) return true;
        else return false;
    }

    bool checkComp()
    {
        REP(i,4)REP(j,4)
        {
            if(MAP[i][j]=='.')
                return false;
        }
        return true;
    }

	void solve()
	{
        cin>>T;
        CASE=0;
        while(CASE++<T)
        {
            REP(i,4)REP(j,4)
            {
                cin>>MAP[i][j];
            }
            printf("Case #%d: ",CASE);
            if(checkWon('X'))
                cout<<R1<<endl;
            else if(checkWon('O'))
                cout<<R2<<endl;
            else if(checkComp())
                cout<<R3<<endl;
            else
                cout<<R4<<endl;
        }
	}
};

int main()
{
	Problem problem=Problem();
	problem.solve();
	//system("pause");
	return 0;
}


