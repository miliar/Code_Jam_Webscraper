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
char TIC[4][4];
char check(string str)
{
    string W[]= {"XXXT","XXTX","XTXX","TXXX","XXXX"};
    if(str.compare(W[0])==0||str.compare(W[1])==0||str.compare(W[2])==0||str.compare(W[3])==0||str.compare(W[4])==0)
        return'X';

    string Y[]= {"OOOT","OOTO","OTOO","TOOO","OOOO"};
    if(str.compare(Y[0])==0||str.compare(Y[1])==0||str.compare(Y[2])==0||str.compare(Y[3])==0||str.compare(Y[4])==0)
        return'O';

    return '0';


}
char win()
{
    for (int i=0; i<4; i++)
    {
        string str="";
        for (int j=0; j<4; j++)
            str+=(char)TIC[i][j];

        if(check(str)=='X')
            return 'X';
        if(check(str)=='O')
            return 'O';


    }
    for (int i=0; i<4; i++)
    {
        string str="";
        for (int j=0; j<4; j++)
        {
            str+=TIC[j][i];

        }
        if(check(str)=='X')
            return 'X';
        if(check(str)=='O')
            return 'O';


    }
    string D,RD;
    D+=(char)TIC[0][0];
    D+=(char)TIC[1][1];
    D+=(char)TIC[2][2];
    D+=(char)TIC[3][3];
    if(check(D)=='X')
        return 'X';
    if(check(D)=='O')
        return 'O';

    RD+=(char)TIC[0][3];
    RD+=(char)TIC[1][2];
    RD+=(char)TIC[2][1];
    RD+=(char)TIC[3][0];
    if(check(RD)=='X')
        return 'X';
    if(check(RD)=='O')
        return 'O';


    return '0';
}

int main()

{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int q=1; q<=t; q++)
    {
        char a;
        int con=0;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                cin>>a;
                TIC[i][j]=a;
                if(a!='.')
                    con++;

            }

        }


        char W='0';
        W=win();
        if(W!='0')
            printf("Case #%d: %c won\n",q,W);
        else if(W=='0'&&con==16)
            printf("Case #%d: Draw\n",q);
        else
            printf("Case #%d: Game has not completed\n",q);




    }
    return 0;
}
