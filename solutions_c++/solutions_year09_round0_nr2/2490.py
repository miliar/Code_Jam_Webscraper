#include <iostream>

using namespace std;

int t,h,w,i,j,hi[105][105],k;
int num[105][105];
int now;

void advance(int tmpi,int tmpj)
{
    if(k==1)
    {
        printf("%d %d\n",tmpi,tmpj);
    }
    if(num[tmpi][tmpj]!=0)
    {
        return ;
    }
    int minn=1000000;
    //int tmpi=tmpii,tmpj=tmpjj;
    if(tmpi>0&&hi[tmpi-1][tmpj]<minn)
    {
        minn=hi[tmpi-1][tmpj];
    }
    if(tmpj>0&&hi[tmpi][tmpj-1]<minn)
    {
        minn=hi[tmpi][tmpj-1];
    }
    if(tmpj+1<w&&hi[tmpi][tmpj+1]<minn)
    {
        minn=hi[tmpi][tmpj+1];
    }
    if(tmpi+1<h&&hi[tmpi+1][tmpj]<minn)
    {
        minn=hi[tmpi+1][tmpj];
    }
    if(hi[tmpi][tmpj]<=minn)
    {
        num[tmpi][tmpj]=now;
        now++;
        return ;
    }
    if(k==1)
    {
        printf("%d %d\n",minn,hi[tmpi][tmpj-1]);
    }
    if(tmpi>0&&hi[tmpi-1][tmpj]==minn)
    {
        advance(tmpi-1,tmpj);
        num[tmpi][tmpj]=num[tmpi-1][tmpj];
    }
    else if(tmpj>0&&hi[tmpi][tmpj-1]==minn)
    {
        advance(tmpi,tmpj-1);
        num[tmpi][tmpj]=num[tmpi][tmpj-1];
    }
    else if(tmpj+1<w&&hi[tmpi][tmpj+1]==minn)
    {
        advance(tmpi,tmpj+1);
        num[tmpi][tmpj]=num[tmpi][tmpj+1];
    }
    else
    {
        advance(tmpi+1,tmpj);
        num[tmpi][tmpj]=num[tmpi+1][tmpj];
    }
    return ;
}

int main()
{
    FILE *fin=fopen("B-small-attempt1.in","r");
    FILE *fout=fopen("B-small.out","w");
    fscanf(fin,"%d",&t);
    for(k=1;k<=t;k++)
    {
        fscanf(fin,"%d %d",&h,&w);
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                fscanf(fin,"%d",&hi[i][j]);
                num[i][j]=0;
            }
        }
        now=1;
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                if(num[i][j]==0)
                {
                    advance(i,j);
                    printf("%d %d %d %d %d\n",k,i,j,num[i][j],now);
                    fflush(stdout);
                }
            }
        }
        fprintf(fout,"Case #%d:\n",k);
        printf("Case %d:\n",k);
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                fprintf(fout,"%c ",'a'+num[i][j]-1);
            }
            fprintf(fout,"\n");
        }
        for(i=0;i<h;i++)
        {
            for(j=0;j<w;j++)
            {
                printf("%c ",'a'+num[i][j]-1);
            }
            printf("\n");
        }
    }
    return 0;
}
