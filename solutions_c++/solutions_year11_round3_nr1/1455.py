#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string.h>
#include <stack>
#include <sstream>
#include <bitset>
#include <algorithm>
#include <numeric>
#define TASK "A-large"
#define Max 50
using namespace std;

int T,R,C,Grid[Max][Max];

void Init()
{
    memset(Grid, 0, sizeof(Grid));
}

int main()
{
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    
    cin>>T;
    
    for(int t=0; t<T; t++)
    {
        Init();
        cin>>R>>C;
        
        char tmp;
        int blue=0;
        
        for(int i=0; i<R; i++)
        {
            for(int j=0; j<C; j++)
            {
                cin>>tmp;
                if(tmp=='#')
                {
                    Grid[i][j]=1;
                    blue++;
                }
                else
                {
                    Grid[i][j]=0;
                }
            }
        }
        
        
        for(int i=0; i+1<R; i++)
        {
            for(int j=0; j+1<C; j++)
            {
                if(Grid[i][j]==1 && Grid[i][j+1]==1 && Grid[i+1][j]==1 && Grid[i+1][j+1]==1)
                {
                    Grid[i][j]=Grid[i+1][j+1]=2;
                    Grid[i][j+1]=Grid[i+1][j]=3;
                    blue-=4;
                }
            }
        }
        
        
        cout<<"Case #"<<t+1<<":"<<endl;
        if(blue>0)
        {
            cout<<"Impossible"<<endl;
        }
        else
        {
            for(int i=0; i<R; i++)
            {
                for(int j=0; j<C; j++)
                {
                    if(Grid[i][j]==2)
                    {
                        cout<<'/';
                    }
                    else if(Grid[i][j]==3)
                    {
                        cout<<'\\';
                    }
                    else
                    {
                        cout<<'.';
                    }
                }
                cout<<endl;
            }
        }
        
    }
    
    
    fclose(stdin);
    //fclose(stdout);
    
    return 0;
}
