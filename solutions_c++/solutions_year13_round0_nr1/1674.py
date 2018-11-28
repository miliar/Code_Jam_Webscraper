#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

char mp[4][4];
int dir[4][2] = {{1,0},{0,1},{1,-1},{1,1}};
bool check(int x,int y)
{
    if(x >= 0 && x < 4 && y >= 0 && y < 4)
        return true;
    else
        return false;
}
int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    while(cin >> T)
    {
        int csT = 1;
        while(T--)
        {
            int flag = 0;
            for(int i = 0; i < 4; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    cin >> mp[i][j];
                    if(mp[i][j] == '.')
                        flag = 1;
                }
            }
            int xx,yy;
            int tmpx,tmpy;
            int finish = 0;
            char winner;
            for(int i = 0; i < 4; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    if(mp[i][j] == '.')
                        continue;
                    for(int k = 0; k < 4; k++)
                    {
                        int cnt = 0;
                        tmpx = i; tmpy = j;
                        while(1){
                            tmpx += dir[k][0];
                            tmpy += dir[k][1];
                            if(check(tmpx,tmpy)&&(mp[tmpx][tmpy] == 'T' || mp[tmpx][tmpy] == mp[i][j]))
                            {
                                cnt++;
                                continue;
                            }
                            else
                                break;
                        }
                        tmpx = i; tmpy = j;
                        while(1)
                        {
                            tmpx -= dir[k][0];
                            tmpy -= dir[k][1];
                            if(check(tmpx,tmpy)&&(mp[tmpx][tmpy] == 'T' || mp[tmpx][tmpy] == mp[i][j]))
                            {
                                cnt++;
                                continue;
                            }
                            else
                                break;
                        }
                        if(cnt == 3)
                        {
                            finish = 1;
                            winner = mp[i][j];
                            break;
                        }
                    }

                }
            }
            cout << "Case #"<<csT++<<": ";
            if(finish == 0)
            {
                if(flag == 0)
                    cout << "Draw" << endl;
                else
                    cout << "Game has not completed" << endl;
            }
            else
            {
                cout << winner << " won" << endl;
            }
        }
    }
    return 0;
}
