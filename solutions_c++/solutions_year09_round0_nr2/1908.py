#include <iostream>
using namespace std;

int ar[110][110];
int parent[110][110];
int sb_x, sb_y, h, w, ctr;
int que_x[10000], que_y[10000];
char tmp;

void cari(int x, int y)
{
    int min=ar[x][y];
    
    sb_x=x;
    sb_y=y;
    
    if (x>0 && ar[x][y]>ar[x-1][y] && parent[x-1][y]==-1)
    {
        min=ar[x-1][y];
        sb_x=x-1;
        sb_y=y;
    }
    
    if (y>0 && min>ar[x][y-1] && parent[x][y-1]==-1)
    {
        min=ar[x][y-1];
        sb_x=x;
        sb_y=y-1;
    }
    
    if (y<w-1 && min>ar[x][y+1] && parent[x][y+1]==-1)
    {
        min=ar[x][y+1];
        sb_x=x;
        sb_y=y+1;
    }
    
    if (x<h-1 && min>ar[x+1][y] && parent[x+1][y]==-1)
    {
        min=ar[x+1][y];
        sb_x=x+1;
        sb_y=y;
    }
    
    if (min!=ar[x][y])
        cari(sb_x, sb_y);
}

bool ismin(int x, int y, int patok_x, int patok_y)
{
    int min=ar[x][y]+1;
    int kor_x=x, kor_y=y;
    
    if (x>0 && min>ar[x-1][y])
    {
        min=ar[x-1][y];
        kor_x=x-1;
        kor_y=y;
    }
    
    if (y>0 && min>ar[x][y-1])
    {
        min=ar[x][y-1];
        kor_x=x;
        kor_y=y-1;
    }
    
    if (y<w-1 && min>ar[x][y+1])
    {
        min=ar[x][y+1];
        kor_x=x;
        kor_y=y+1;
    }
    
    if (x<h-1 && min>ar[x+1][y])
    {
        min=ar[x+1][y];
        kor_x=x+1;
        kor_y=y;
    }

    if (kor_x==patok_x && kor_y==patok_y)
        return true;
    else
        return false;
}

void fill(int x, int y)
{
    int s=0, f=1;
    que_x[s]=x;
    que_y[s]=y;
    
    while(s<f)
    {
        parent[que_x[s]][que_y[s]]=ctr;
        
        if (que_x[s]>0 && ar[que_x[s]-1][que_y[s]]>ar[que_x[s]][que_y[s]] && parent[que_x[s]-1][que_y[s]]==-1)
        {
            if (ismin(que_x[s]-1, que_y[s], que_x[s], que_y[s]))
            {
                que_x[f]=que_x[s]-1;
                que_y[f]=que_y[s];
                f++;
            }
        }
        
        if (que_y[s]>0 && ar[que_x[s]][que_y[s]-1]>ar[que_x[s]][que_y[s]] && parent[que_x[s]][que_y[s]-1]==-1)
        {
            if (ismin(que_x[s], que_y[s]-1, que_x[s], que_y[s]))
            {
                que_x[f]=que_x[s];
                que_y[f]=que_y[s]-1;
                f++;
            }
        }
        
        if (que_x[s]<h-1 && ar[que_x[s]+1][que_y[s]]>ar[que_x[s]][que_y[s]] && parent[que_x[s]+1][que_y[s]]==-1)
        {
            if (ismin(que_x[s]+1, que_y[s], que_x[s], que_y[s]))
            {
                que_x[f]=que_x[s]+1;
                que_y[f]=que_y[s];
                f++;
            }
        }
        
        if (que_y[s]<w-1 && ar[que_x[s]][que_y[s]+1]>ar[que_x[s]][que_y[s]] && parent[que_x[s]][que_y[s]+1]==-1)
        {
            if (ismin(que_x[s], que_y[s]+1, que_x[s], que_y[s]))
            {
                que_x[f]=que_x[s];
                que_y[f]=que_y[s]+1;
                f++;
            }
        }
        
        s++;
    }
}

int main()
{
    int n, num=1;
    
    cin >>n;
    
    while(n--)
    {
        cin >>h >>w;
        
        ctr=0;
        
        for (int i=0;i<h;i++)
            for (int j=0;j<w;j++)
            {
                cin >>ar[i][j];
                parent[i][j]=-1;
            }
        
        for (int i=0;i<h;i++)
            for (int j=0;j<w;j++)
            {
                if (parent[i][j]==-1)
                {
                    cari(i, j);
                    fill(sb_x, sb_y);
                    ctr++;
                }
            }
        
        printf("Case #%d:\n", num++);
        
        for (int i=0;i<h;i++)
        {
            for (int j=0;j<w;j++)
            {
                tmp='a';
                tmp+=parent[i][j];
                cout <<tmp;
                
                if (j<w-1)
                    cout <<" ";
            }
            cout <<endl;
        }
    }
    
    return 0;
}
