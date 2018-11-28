#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<map>

using namespace std;

string i2s(long long x) { ostringstream o; o<<x; return o.str(); }
long long s2i(string s) { istringstream i(s); long long x; i>>x; return x; } 

int dx[4] = {-1,0,0,1};
int dy[4] = {0,-1,1,0};

char r[100+15][100+15];
int a[100+15][100+15], mark[100+15][100+15];
int m,n;


void initialize()
{
     int i,j;
     cin>>m>>n;
     for (i=0; i<m; i++)
       for (j=0; j<n; j++)
         cin>>a[i][j];
}

bool ok(int x,int y)
{
     if (x<0||y<0||x>=m||y>=n) return false;
     return true;
}


int go(int x, int y)
{
    if (mark[x][y]!=-1) return mark[x][y];
    
    int k,h, min = a[x][y];
    for (k=0; k<4; k++)
      if ( ok(x+dx[k],y+dy[k]) && min>a[x+dx[k]][y+dy[k]] )
      {
           min = a[x+dx[k]][y+dy[k]];
           h = k;
      }
    if (a[x][y] == min) return mark[x][y] = n*x+y; // sink

    return mark[x][y] = go(x+dx[h],y+dy[h]);
}


void dfs(int x, int y, char c)
{
     r[x][y] = c;
     for (int k=0; k<4; k++)
       if ( ok(x+dx[k],y+dy[k]) && r[x+dx[k]][y+dy[k]]=='0' 
            && mark[x][y]==mark[x+dx[k]][y+dy[k]]      )
          dfs(x+dx[k],y+dy[k],c);
}

void solve()
{
     int i,j,k;

     memset(mark,-1,sizeof(mark));
     for (i=0; i<m; i++)
       for (j=0; j<n; j++)
        if (mark[i][j]==-1)
          go(i,j);
     
     char c='a';
     memset(r,'0',sizeof(r));
     
     for (i=0; i<m; i++)
       for (j=0; j<n; j++)
         if (r[i][j]=='0')
         {
             dfs(i,j,c);
             c++;
         }
     
     for (i=0; i<m; i++)
     {
         for (j=0; j<n; j++) 
         { 
             cout<<r[i][j]; 
             if (j<n-1) cout<<" "; 
         }
         
         cout<<endl;
     }

}


#include<conio.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("t.out","w",stdout);
    
    int num,z;
    cin>>num;
    for (z=0; z<num; z++)
    {
        cout<<"Case #"<<z+1<<":"<<endl;
        initialize();
        solve();
    }
    
    
    fclose(stdin);
    fclose(stdout);    
//    getch();
    
    return 0;
}
