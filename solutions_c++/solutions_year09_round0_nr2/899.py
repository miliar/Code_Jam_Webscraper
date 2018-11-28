#include<iostream>

using namespace std;
const int maxr = 100;
const int maxc = 100;

int row, col;
int map[maxr+5][maxc+5];
char label[maxr + 5][maxc+ 5];
int graph[maxr*maxc][4];
int n;



int direction[4][2] = {{-1,0}, {0,-1}, {0,1}, {1,0}};
void Init()
{
     cin >> row >> col;
     for(int i = 0; i < row; ++i)
             for(int j =0; j < col; ++j)
             {
                     cin >> map[i][j];
                     label[i][j] = '*';
             }
}
char DFS(int r, int c, char l)
{
     label[r][c] = l;
     for(int i  = 0; i < 4; ++i)
     {
             if(graph[col*r + c][i])
             {
                            int nr = r + direction[i][0];
                            int nc = c + direction[i][1];
                            
                            if(label[nr][nc] == '*')
                                             DFS(nr, nc, l);
             }
     }
     
  
}
void ConstructGraph()
{
     memset(graph, 0, sizeof(graph));
     for(int r = 0; r < row; ++r)
             for(int c = 0; c < col; ++c)
             {
                        int nr, nc;
                        int min = map[r][c];
                        int pos = -1;
                        int posr = -1;
                        int posc = -1;
                        for(int i = 0; i < 4; ++i)
                        {
                             nr = r + direction[i][0];
                             nc = c + direction[i][1];
             
                             if(nc < 0 || nc >= col)
                                   continue;
                             if(nr < 0 || nr >= row)
                                   continue;
             
                             if(map[nr][nc] < min)
                             {
                                            min = map[nr][nc];
                                            posr = nr;
                                            posc = nc;
                                            pos = i;
                             }
                         }
                         if(pos != -1)
                         {
                                 graph[r*col + c][pos] = 1;
                                 graph[posr*col + posc][ 3 - pos ] = 1;
                         }
             }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b_out.txt","w",stdout);
    cin >> n;
    for(int i = 1; i <= n; ++i)
    {
            Init();
            ConstructGraph();
            char l = 'a';
            for(int r = 0; r < row; ++r)
                    for(int c = 0 ; c < col; ++c)
                    {
                            if(label[r][c] == '*')
                            {
                                           DFS(r,c,l);
                                           l++;
                            }
                    }
            
            printf("Case #%d:\n",i);
            for(int r = 0; r < row; ++r)
                    for(int c = 0; c < col; ++c)
                    {
                            printf("%c", label[r][c]);
                            if( c!= col -1)
                                printf(" ");
                            else
                                printf("\n");
                    }
            
    }
    return 0;
}
