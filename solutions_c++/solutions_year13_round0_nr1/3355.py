#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;
int map[4][4];
int main()
{
    ifstream in("input1.txt");
    ofstream out("output1.txt");
    int po=0;
    in>>po;
    for(int co=0;co<po;co++)
    {
        char test[5];
        int flag=0;
        int flag1=0;
        for(int y=0;y<=3;y++)
        {
            in>>test;
            for(int h=0;h<=3;h++)
            {
                if(test[h]=='.')
                {
                    map[y][h]=-1;
                    flag++;
                }
                if(test[h]=='X') map[y][h]=2;
                if(test[h]=='O') map[y][h]=1;
                if(test[h]=='T') map[y][h]=0;
            }
        }
        for(int h=0;h<=3;h++)
        {
            if((map[h][0]==2 || map[h][0]==0) && (map[h][1]==2 || map[h][1]==0) && (map[h][2]==2 || map[h][2]==0) && (map[h][3]==2 || map[h][3]==0))
            {
                out<<"Case #"<<co+1<<": X won"<<endl;
                flag1=1;
                break;
            }
            if((map[h][0]==1 || map[h][0]==0) && (map[h][1]==1 || map[h][1]==0) && (map[h][2]==1 || map[h][2]==0) && (map[h][3]==1 || map[h][3]==0))
            {
                out<<"Case #"<<co+1<<": O won"<<endl;
                flag1=1;
                break;
            }
            if((map[0][h]==2 || map[0][h]==0) && (map[1][h]==2 || map[1][h]==0) && (map[2][h]==2 || map[2][h]==0) && (map[3][h]==2 || map[3][h]==0))
            {
                out<<"Case #"<<co+1<<": X won"<<endl;
                flag1=1;
                break;
            }
            if((map[0][h]==1 || map[0][h]==0) && (map[1][h]==1 || map[1][h]==0) && (map[2][h]==1 || map[2][h]==0) && (map[3][h]==1 || map[3][h]==0))
            {
                out<<"Case #"<<co+1<<": O won"<<endl;
                flag1=1;
                break;
            }
        }
        if(flag1==1) continue;
        if((map[0][0]==2 || map[0][0]==0) && (map[1][1]==2 || map[1][1]==0) && (map[2][2]==2 || map[2][2]==0) && (map[3][3]==2 || map[3][3]==0))
        {
            out<<"Case #"<<co+1<<": X won"<<endl;
            flag1=1;
        }
        else if((map[0][0]==1 || map[0][0]==0) && (map[1][1]==1 || map[1][1]==0) && (map[2][2]==1 || map[2][2]==0) && (map[3][3]==1 || map[3][3]==0))
        {
            out<<"Case #"<<co+1<<": O won"<<endl;
            flag1=1;
        }
        else if((map[0][3]==2 || map[0][3]==0) && (map[1][2]==2 || map[1][2]==0) && (map[2][1]==2 || map[2][1]==0) && (map[3][0]==2 || map[3][0]==0))
        {
            out<<"Case #"<<co+1<<": X won"<<endl;
            flag1=1;
        }
        else if((map[0][3]==1 || map[0][3]==0) && (map[1][2]==1 || map[1][2]==0) && (map[2][1]==1 || map[2][1]==0) && (map[3][0]==1 || map[3][0]==0))
        {
            out<<"Case #"<<co+1<<": O won"<<endl;
            flag1=1;
        }
        if(flag1==1) continue;
        if(flag==0) out<<"Case #"<<co+1<<": Draw"<<endl;
        else if(flag>0) out<<"Case #"<<co+1<<": Game has not completed"<<endl;
    }
    return 0;
}
        
        
        
                
        
    
