#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;
int graph[110][110];
int num[110][110];
int path[110][110];
int r,c;

int uni[110*110];
int map[110][110];
void back1(int i,int j,int v,int cnt)
{
        if(map[i][j] != v)
                return ;
        if(map[i][j] ==-1) return ;
        map[i][j] = -1;

        path[i][j] = cnt;

        back1(i+1,j,v,cnt);
        back1(i-1,j,v,cnt);
        back1(i,j+1,v,cnt);
        back1(i,j-1,v,cnt);
}



int union_find(int k)
{
        if(k==uni[k])
                return k;
        else return union_find(uni[k]);
}
int aa[5][2]={ {0,0},{+1,0},{0,+1},{0,-1},{-1,0}};

void back(int i,int j,int n,int d)
{
        int x=i,y=j,v=graph[i][j];

        if(path[x][y] == -1){
                path[x][y] = n;
                num[x][y] = n;
                uni[(x-1)*c +y] = n;
        }
        else{
                int n1 = union_find(num[x][y]);
                if(n > n1){
                        uni[(x-1+aa[d][0])*c +y+aa[d][1]] = n1;
                        path[x+aa[d][0]][y+aa[d][1]] = n1;
                        num[x+aa[d][0]][y+aa[d][1]] = n1;
                }
                else{
                        uni[(x-1)*c +y] = n;
                        path[x][y] = n;
                        num[x][y] = n;
                }
                return ;
        }

        //N
        if(v > graph[i-1][j]){
                x = i-1;
                y = j;
                v = graph[i-1][j];
                d = 1;
        }
        //W
        if(v > graph[i][j-1]){
                x = i;
                y = j-1;
                v = graph[i][j-1];
                d = 2;
        }

        //E
        if(v > graph[i][j+1]){
                x = i;
                y = j+1;
                v = graph[i][j+1];
                d = 3;
        }

        //S
        if(v > graph[i+1][j]){
                x = i+1;
                y = j;
                v = graph[i+1][j];
                d = 4;
        }

        if(x == i && y == j)
                return ;
        back(x,y,n,d);
        int n1 = union_find(num[x][y]);
        if(n > n1){
                uni[(x-1+aa[d][0])*c +y+aa[d][1]] = n1;
                path[x+aa[d][0]][y+aa[d][1]] = n1;
                num[x+aa[d][0]][y+aa[d][1]] = n1;
        }
        else{
                uni[(x-1)*c +y] = n;
                path[x][y] = n;
                num[x][y] = n;
        }

}

int main()
{

        int i,j,t;
        int kase;

        cin >> t;

        for(kase=1;kase<=t;kase++){
                cin >> r >> c;
                cout <<"Case #"<<kase<<":"<<endl;
                memset(graph,1,sizeof graph);
                memset(path,-1,sizeof path);
                for(i=1;i<=r;i++)
                        for(j=1;j<=c;j++){
                                cin >> graph[i][j];
                                num[i][j] = (i-1)*c +j;
                                uni[(i-1)*c +j] = (i-1)*c +j;
                        }

                for(i=1;i<=r;i++)
                        for(j=1;j<=c;j++)
                                if(path[i][j] == -1)
                                        back(i,j,num[i][j],0);


                for(i=1;i<=r;i++){
                        for(j=1;j<=c;j++)
                                map[i][j] = union_find(num[i][j]);
                }
                memset(path,0,sizeof path);

                int cnt = 0;
                for(i=1;i<=r;i++)
                        for(j=1;j<=c;j++)
                                if(map[i][j] != -1){
                                        back1(i,j,map[i][j],cnt);
                                        cnt++;
                                }
                for(i=1;i<=r;i++,cout<<endl){
                        cout << (char)('a' + path[i][1]);
                        for(j=2;j<=c;j++)
                                cout << " "<<(char)('a' + path[i][j]);
                }
        }

        return 0;
}
