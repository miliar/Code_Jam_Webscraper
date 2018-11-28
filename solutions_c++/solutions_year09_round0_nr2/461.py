#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int T,H,W;
int land[200][200];
char mark[200][200];
int x;
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

queue<int> qx;
queue<int> qy;

int first;
int last;

int is_connect(int x1,int y1,int x2,int y2)
{
    int min = 10001;
    int d;

    for (d=0;d<4;d++)
    {
        if (min > land[x1+dir[d][0]][y1+dir[d][1]]) min = land[x1+dir[d][0]][y1+dir[d][1]];
    }

    if (min >= land[x1][y1]) return 0;

    for (d=0;d<4;d++)
    {
        if (min == land[x1+dir[d][0]][y1+dir[d][1]]) break;
    }

    if ((x2 == x1+dir[d][0]) && (y2 == y1+dir[d][1])) return 1;
    else return 0;
}

int main()
{
    cin>>T;

    for (int t=1;t<=T;t++)
    {
        cin>>H>>W;

        for (int i=1;i<=H;i++)
        {
            land[i][0] = 10001;
            land[i][W+1] = 10001;
        }
        
        for (int i=1;i<=W;i++)
        {
            land[0][i] = 10001;
            land[H+1][i] = 10001;
        }

        for (int i=1;i<=H;i++)
            for (int j=1;j<=W;j++)
            {
                cin>>land[i][j];                
            }
        
        memset(mark,0,200L*200);

        char cur_char = 'a';

        for (int i=1;i<=H;i++)
            for (int j=1;j<=W;j++)
                if (mark[i][j] == 0)
                {                
                    while( !qx.empty() ) qx.pop();
                    while( !qy.empty() ) qy.pop();

                    mark[i][j] = cur_char;
                    qx.push(i);qy.push(j);

                    while (!qx.empty())
                    {
                        int x1 = qx.front();
                        int y1 = qy.front();
                        qx.pop();qy.pop();
    
                        for (int d=0;d<4;d++)
                            if (mark[x1+dir[d][0]][y1+dir[d][1]] == 0)
                                if (is_connect(x1,y1,x1+dir[d][0],y1+dir[d][1]) || is_connect(x1+dir[d][0],y1+dir[d][1],x1,y1) )
                                {
                                    mark[x1+dir[d][0]][y1+dir[d][1]] = cur_char;
                                    qx.push(x1+dir[d][0]);
                                    qy.push(y1+dir[d][1]);
                                }
                    }

                    cur_char++;
                }
        cout<<"Case #"<<t<<": "<<endl;
        for (int i=1;i<=H;i++)
        {
            for (int j=1;j<=W;j++) cout<<mark[i][j]<<' ';
            cout<<endl;
        }
            
    }
    return 1;
}
