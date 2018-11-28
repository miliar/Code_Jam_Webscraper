#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int num = 0;
    while(num++<n)
    {
        string str[4];
        for(int i = 0; i < 4; i ++)
            cin>>str[i];
        int countX[10];
        int countO[10];
        memset(countX, 0, sizeof(countX));
        memset(countO, 0, sizeof(countO));
        bool draw = true;
        for(int i = 0; i < 4; i ++)
        {
            for(int j = 0; j <4 ;j ++)
            {
                if(str[i][j] =='X')
                {
                    countX[i]++;
                    countX[4+j]++;
                    if(i == j) countX[8]++;
                    if(i+j==3) countX[9]++;
                }
                else if(str[i][j] =='O')
                {
                    countO[i]++;
                    countO[4+j]++;
                    if(i == j) countO[8]++;
                    if(i+j==3) countO[9]++;
                }
                else if(str[i][j] == 'T')
                {
                    countX[i]++;
                    countX[4+j]++;
                    countO[i]++;
                    countO[4+j]++;
                    if(i == j) {countX[8]++;countO[8]++;}
                    if(i+j==3) {countX[9]++;countO[9]++;}
                }
                else
                {
                    draw = false;
                }
            }
        }
        bool flag = false;
        for(int i = 0; i < 10; i++)
        {
            if(countX[i]==4)
            {
                cout<<"Case #"<< num <<": X won"<<endl;
                flag = true;
                break;
            }
        }
        for(int i = 0; i < 10; i++)
        {
            if(countO[i]==4)
            {
                cout<<"Case #"<< num <<": O won"<<endl;;
                flag = true;
                break;
            }
        }
        if(flag == false)
        {
            if(draw)
            {
                cout<<"Case #"<< num <<": Draw"<<endl;;
            }
            else
            {
                cout<<"Case #"<< num <<": Game has not completed"<<endl;;
            }
        }
    }
    return 0;
}
