#include <iostream>
using namespace std;

const int wtg[4][2]={{-1,0},
                     {0,-1},
                     {0,1},
                     {1,0}};

    int hm[128][128];
    int h,w;
    int was[128][128];
    int colours;
    
    int s,f;
    
    int last[128*128];
    int *wpx[128*128];
    int *wpy[128*128];
    int maxalt;
    
    int gotsymb[64];
    
    void init()
    {
        memset(last,0,sizeof(last));
        memset(gotsymb,0,sizeof(gotsymb));
        memset(was,0,sizeof(was));
                
        scanf("%d%d",&h,&w);
        maxalt = 0;
        colours = 0;
        for(int i=0;i<h;i++)
            for(int j=0;j<w;j++)
            {
                scanf("%d",&hm[i][j]);                
                last[hm[i][j]]++;
                maxalt = max(maxalt, hm[i][j]);
            }
        for(int i=0;i<=maxalt;i++)
            if (last[i]!=0)
            {
                wpx[i] = new int[last[i]];
                wpy[i] = new int[last[i]];
                last[i]=0;
            }        
        for(int i=0;i<h;i++)
            for(int j=0;j<w;j++)
            {      
                wpx[ hm[i][j] ][ last[hm[i][j]] ] = i;
                wpy[ hm[i][j] ][ last[hm[i][j]]++ ] = j;
            }            
    }
    
    bool best(int ax,int ay,int bx,int by)
    {
        int minval = maxalt+1;
        for(int i=0;i<4;i++)
        {
            int nx = ax+wtg[i][0];
            int ny = ay+wtg[i][1];
            if (nx>=0 && nx<h && ny>=0 && ny<w)           
                minval = min(minval,hm[nx][ny]);
        }
        if (minval<hm[bx][by])
            return false;
        for(int i=0;i<4;i++)
        {
            int nx = ax+wtg[i][0];
            int ny = ay+wtg[i][1];            
            if (nx==bx && ny==by)
                return true;
            if (nx>=0 && nx<h && ny>=0 && ny<w && hm[nx][ny]==minval)
                return false;
        }
    }
    
    void startrec(int kx, int ky)
    {
//        cout << "At " << kx << " " << ky << " --> " << colours << endl;
        was[kx][ky] = colours; 
        for(int i=0;i<4;i++)
        {
            int nx = kx+wtg[i][0];
            int ny = ky+wtg[i][1];
            if (nx>=0 && nx<h && ny>=0 && ny<w)
            {
                if (hm[nx][ny]>hm[kx][ky] && was[nx][ny]==0 && best(nx,ny,kx,ky))
                    startrec(nx,ny);
            }
        }
    }
        
    void colourthem()
    {
        for(int i=0;i<=maxalt;i++)
            for(int j=0;j<last[i];j++)
                if (was[ wpx[i][j] ][ wpy[i][j] ] == 0)
                {
//                    cout << "New colour" << endl;
                    colours++;
                    startrec(wpx[i][j],wpy[i][j]);
                }        
    }
    
    void findbest()
    {
        int ncol = 1;
        for(int i=0;i<h;i++)
            for(int j=0;j<w;j++)
                if (gotsymb[was[i][j]]==0)                
                    gotsymb[was[i][j]] = ncol++;                    
    }
    
    void print()
    {
        for(int i=0;i<h;i++)
            for(int j=0;j<w;j++)
                printf("%c%c",(char)('a'+gotsymb[was[i][j]] - 1),(j+1==w) ? '\n' : ' ');
    }

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int nt;
    scanf("%d",&nt);
    for(int i=0;i<nt;i++)
    {
        init();
        colourthem();        
        findbest();
        printf("Case #%d:\n",i+1);
        print();
    }
    return 0;
}
