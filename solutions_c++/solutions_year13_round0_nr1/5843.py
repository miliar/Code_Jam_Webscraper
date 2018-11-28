#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

#define MAX_NUM 5
int arr[MAX_NUM][MAX_NUM];
int T;

bool success(int obj)
{
    int i;
    for(i=1; i<MAX_NUM; i++)
    {
        if (arr[i][1]==arr[i][2] && arr[i][2]==arr[i][3] && arr[i][3]==arr[i][4] && arr[i][4]==obj)
        {
            return true;
        }
        if (arr[1][i]==arr[2][i] && arr[2][i]==arr[3][i] && arr[3][i]==arr[4][i] && arr[4][i]==obj)
        {
            return true;
        }
    }
    if (arr[1][1]==arr[2][2] && arr[2][2]==arr[3][3] && arr[3][3]==arr[4][4] && arr[4][4]==obj)
    {
        return true;
    }
    if (arr[1][4]==arr[2][3] && arr[2][3]==arr[3][2] && arr[3][2]==arr[4][1] && arr[4][1]==obj)
    {
        return true;
    }
}

int main()
{
    cin>>T;
    int count = 0;
    while(T--)
    {
        count++;
        int i;
        string str;
        bool haveT = false;
        bool haveE = false;
        int ti, tj;
        for(i=1; i<MAX_NUM; i++)
        {
            cin>>str;
            int j;
            for(j=1; j<MAX_NUM; j++)
            {
                if (str[j-1] == 'X')
                {
                    arr[i][j] = 1;
                }else if (str[j-1]=='O')
                {
                    arr[i][j] = 2;
                }else if (str[j-1]=='.')
                {
                    haveE = true;
                    arr[i][j] = 0;
                }else if (str[j-1]=='T')
                {
                    haveT = true;
                    arr[i][j] = -1;
                    ti = i;
                    tj = j;
                }
            }
        }
        cout<<"Case #"<<count<<": ";
        if(haveT)
        {
            arr[ti][tj] = 1;
            if (success(1))
            {
                cout<<"X won"<<endl;
                continue;
            }
            arr[ti][tj] = 2;
            if (success(2))
            {
                cout<<"O won"<<endl;
                continue;
            }
            if (!haveE)
            {
                cout<<"Draw"<<endl;
                continue;
            }else{
                cout<<"Game has not completed"<<endl;
                continue;
            }
        }else{
            if (success(1))
            {
                cout<<"X won"<<endl;
                continue;
            }
            if (success(2))
            {
                cout<<"O won"<<endl;
                continue;
            }
            if (!haveE)
            {
                cout<<"Draw"<<endl;
                continue;
            }else{
                cout<<"Game has not completed"<<endl;
                continue;
            }
        }
    }
    system("PAUSE");
    return 0;
}

/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

*/
