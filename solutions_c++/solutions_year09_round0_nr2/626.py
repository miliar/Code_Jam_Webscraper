#include<stdio.h>
#include<stdlib.h>
int map[105][105],h,w;
char ans[105][105],now;

void search(int i,int j)
{   int lowi,lowj,ii,jj;
    ans[i][j]=now;
    lowi=i;
    lowj=j;
    if(i>0&&map[i-1][j]<map[lowi][lowj])
    {   lowi=i-1;
        lowj=j;
    }
    if(j>0&&map[i][j-1]<map[lowi][lowj])
    {   lowi=i;
        lowj=j-1;
    }
    if(j+1<w&&map[i][j+1]<map[lowi][lowj])
    {   lowi=i;
        lowj=j+1;
    }
    if(i+1<h&&map[i+1][j]<map[lowi][lowj])
    {   lowi=i+1;
        lowj=j;
    }
    if(ans[lowi][lowj]==0) search(lowi,lowj);
    
    ii=i-1;
    jj=j;
    if(ii>=0&&ans[ii][jj]==0&&map[ii][jj]>map[i][j])
        if(ii-1<0||map[ii-1][jj]>map[i][j])
            if(jj-1<0||map[ii][jj-1]>map[i][j])
                if(jj+1>=w||map[ii][jj+1]>map[i][j])
                    search(ii,jj);
    
    ii=i;
    jj=j-1;
    if(jj>=0&&ans[ii][jj]==0&&map[ii][jj]>map[i][j])
        if(ii-1<0||map[ii-1][jj]>map[i][j])
            if(jj-1<0||map[ii][jj-1]>map[i][j])
                if(ii+1>=h||map[ii+1][jj]>=map[i][j])
                    search(ii,jj);
                    
    ii=i;
    jj=j+1;
    if(jj<w&&ans[ii][jj]==0&&map[ii][jj]>map[i][j])
        if(ii-1<0||map[ii-1][jj]>map[i][j])
            if(jj+1>=w||map[ii][jj+1]>=map[i][j])
                if(ii+1>=h||map[ii+1][jj]>=map[i][j])
                    search(ii,jj);
                    
    ii=i+1;
    jj=j;
    if(ii<h&&ans[ii][jj]==0&&map[ii][jj]>map[i][j])
        if(jj-1<0||map[ii][jj-1]>=map[i][j])
            if(jj+1>=w||map[ii][jj+1]>=map[i][j])
                if(ii+1>=h||map[ii+1][jj]>=map[i][j])
                    search(ii,jj);
}

int main()
{   int t,k,i,j;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {   scanf("%d %d",&h,&w);
        now='a';
        
        for(i=0;i<h;i++)
            for(j=0;j<w;j++)
            {   scanf("%d",&map[i][j]);
                ans[i][j]=0;
            }
                
        for(i=0;i<h;i++)
            for(j=0;j<w;j++)
                if(ans[i][j]==0) 
                {   search(i,j);
                    now++;
                }
        
        printf("Case #%d:\n",k+1);        
        for(i=0;i<h;i++)
        {   for(j=0;j<w;j++)
                printf("%c ",ans[i][j]);
            printf("\n");
        }
    }
    //system("pause");
    return 0;
}
