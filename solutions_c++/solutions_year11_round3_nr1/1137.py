#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int t,ti,m,n;
char map[52][52];
int i,j;
bool bo;

int main()
{
    fin>>t;
    for(ti=1;ti<=t;ti++)
    {
        bo=true;
        fin>>m>>n;
        //fout<<m<<n<<endl;
        for(i=1;i<=m;i++)
            for(j=1;j<=n;j++)
            fin>>map[i][j];
            
        if(m==1) for(j=1;j<=n;j++) if(map[1][j]=='#') bo=false;
        if(n==1) for(j=1;j<=m;j++) if(map[j][1]=='#') bo=false;
        
        
        if(m>1 && n>1)
        {    
        for(i=1;i<=m-1;i++)
        {
            
            for(j=1;j<=n-1;j++)
            {
                if(map[i][j]=='#')
                {
                    if(map[i][j+1]=='#' && map[i+1][j]=='#' && map[i+1][j+1]=='#')
                    {
                        map[i][j]='/'; map[i][j+1]='\\';
                        map[i+1][j]='\\'; map[i+1][j+1]='/';
                    }
                    else { /*fout<<"=======2"<<i<<' '<<j<<endl;*/ bo=false;  }
                }
                if(!bo) break;
            }
            if(map[i][n]=='#' && map[i][n-1]!='#') { /*fout<<"=======1"<<i<<' '<<n<<endl;*/ bo=false; break;  }
            if(!bo) break;     
        }       
        for(j=1;j<=n;j++) if(map[m][j]=='#' && map[m-1][j]!='#') { /*fout<<"=======3"<<i<<' '<<j<<endl;*/ bo=false; break; }
        }
        fout<<"Case #"<<ti<<":"<<endl;
        if(!bo) fout<<"Impossible"<<endl;
        else
        {
            for(i=1;i<=m;i++)
            {
                for(j=1;j<=n;j++)
                    fout<<map[i][j];
                fout<<endl;
            }
        }
    }
    return 0;
}
