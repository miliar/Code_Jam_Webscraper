# include <iostream>
# include <vector>
# include <fstream>
# include <algorithm>
# include <map>
# include <queue>

using namespace std;

ifstream in("B-small-attempt9.in");
ofstream out("out.txt");

bool visited[100][10001]={{0}};

int H,W;
int grid[101][10001]={{0}};
char res[101][10001]={{0}};

bool done()
{
    for(int i = 0;i<H;i++)
        for(int j = 0;j<W;j++)
            if(visited[i][j] == false)  return false;
            
    return true;   
}

bool valid(int x,int y, int alt)
{
	int flag = 0;
       if(x+1 < H) 
       if(alt > grid[x+1][y])
       {
	flag = 1;
       }

       if(x-1>=0 )
       if(alt > grid[x-1][y] )	flag = 1;
       
       if(y+1<W)
       if(alt > grid[x][y+1] )	flag = 1;

       if(y-1>=0 )
       if(alt > grid[x][y-1])	flag = 1;

       if(flag)
        return false;
        
    return true;
}

char dfs(char x, int xc, int yc)
{
    visited[xc][yc]=true;
    
    int tx,ty,f=0;
    tx=xc;
    ty=yc;
    
    if(xc-1 >= 0 && grid[xc-1][yc] < grid[tx][ty])
        tx=xc-1,ty = yc,f=1;
    if(yc-1 >= 0 && grid[xc][yc-1] < grid[tx][ty])
        ty=yc-1,tx = xc,f=1;
    if(yc+1 < W && grid[xc][yc+1] < grid[tx][ty])
        ty = yc+1,tx = xc,f=1;
    if(xc+1<H && grid[xc+1][yc] < grid[tx][ty])
        tx=xc+1,ty = yc,f=1;
    
    if(f && visited[tx][ty])
    {
	x = res[tx][ty];
	res[xc][yc]=x;
	return x;
    }
    if(f){
    x = dfs(x,tx,ty);
    }
    res[xc][yc]=x;
    
    return x;
}

int main()
{
    int T,cas=0;
    in>>T;
        
    while(T--){
        
    //    int H,W;
        in>>H>>W;
        
        for(int i = 0;i<H;i++){
            //vector<int> t;
            //int x;
            for(int j = 0;j<W;j++){
              //in>>x;
              //t.push_back(x);
              in>>grid[i][j];
            }
            //grid.push_back(t);
        }
     
    memset(visited,0,sizeof(visited));
                   
    int c = 'a'-1;     
        for(int i = 0;i<H;i++)
            for(int j = 0;j<W;j++)
            if(!visited[i][j]) 
                c = dfs(c+1,i,j);   
    
    out<<"Case #"<<++cas<<": "<<endl;
    
    for(int i = 0;i<H;i++){
        for(int j = 0;j<W;j++)
            out<<res[i][j]<<' ';
        out<<'\n';
    }
            
        
    }
    
    return 0;
}
 
