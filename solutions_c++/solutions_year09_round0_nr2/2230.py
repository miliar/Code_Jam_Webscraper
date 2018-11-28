#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <fstream>
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

#define RET return
#define FOR(i,n) for(int i=0;i<(int)n;++i)
#define SZ(n) ((int)n.size())

#define FORN(i,start,end) for(int i=start;i<end;++i)
#define FORD(i,n) for(int i=(int)n;i>=0;--i)
#define SET(a,n) memset(a,n,sizeof(a))
#define foreach(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back

typedef vector<string> VS;
typedef vector<int> VI;
typedef stringstream SS;

#define MAX 101

int test,row,col,val,num_test=1;
int grid[MAX][MAX];
bool visited[MAX][MAX];
char out_grid[MAX][MAX],cur_char;
ifstream fin("B-large.in");
ofstream fout("output.txt");


struct NODE
{
       int x,y;
       NODE(){}
       NODE(int a,int b)
       {
                x=a;
                y=b;
       }
};

void print_out_grid(void )
{
         FOR(i,row)
         {
                   FOR(j,col)
                   {
                             fout<<out_grid[i][j]<<" ";
                   }
                   fout<<endl;
         }

}

const int DIR=4;
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

bool validate(int r,int c)
{
     if((r>=0)&&(r<row)&&(c>=0)&&(c<col))
            RET 1;
     RET 0;
}

void bfs_grid(int r,int c)
{
     int my_val=grid[r][c];
     int choosed_x=r,choosed_y=c;
     queue<NODE> Q, save;
     NODE add(r,c);
     Q.push(add);
     save.push(add);
     while(!Q.empty())
     {
         bool flag=0;
         NODE cur=Q.front();            
         Q.pop();
         my_val=grid[cur.x][cur.y];
         FOR(dir,DIR)
         {
                int cur_r=cur.x+dx[dir],cur_c=cur.y+dy[dir];
                if( (validate(cur_r,cur_c)) && (grid[cur_r][cur_c]<my_val) )
                {
                    my_val=grid[cur_r][cur_c];
                    choosed_x=cur_r;
                    flag=1;
                    choosed_y=cur_c;
                }
         }
         if(flag)
         {
                 if((visited[choosed_x][choosed_y])&&(out_grid[choosed_x][choosed_y]!='Z'))
                 {
                         while(!save.empty())
                         {
                                 NODE top=save.front();
                                 save.pop();
                                 out_grid[top.x][top.y]=out_grid[choosed_x][choosed_y];
                                 visited[top.x][top.y]=1;
                         }                         
                 }
                 else
                 {
                     NODE add(choosed_x,choosed_y);
                     visited[choosed_x][choosed_y]=1;
                     Q.push(add);
                     save.push(add);
                 }
         }
         else
         {
             while(!save.empty())
             {
                   NODE top=save.front();
                   save.pop();
                   out_grid[top.x][top.y]=cur_char;
                   visited[top.x][top.y]=1;
             }
             cur_char++;
         }      
     }
}

int main()
{
      fin>>test;
      while(test)
      {
             fin>>row>>col;
             cur_char='a';
             SET(visited,0);
             SET(out_grid,'Z');
             FOR(i,row)
             {
                       FOR(j,col)
                       {
                                 fin>>val;
                                 grid[i][j]=val;
                       }
             }
             FOR(i,row)
                       FOR(j,col)
                                 if(!visited[i][j])
                                       bfs_grid(i,j);
             fout<<"Case #"<<num_test<<":\n";
             print_out_grid(); 
             test--;
             num_test++;
      }
      return 0;
}
