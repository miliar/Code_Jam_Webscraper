#include <iostream>
#include <fstream>

using namespace std;

int T,H,W;
int data[100][100];
char ch[100][100];
int x[100][100];
int y[100][100];
char letter;

int basin[26][2];
int basin_times;
int basin_backup[26][2];

void FindMix(int j,int k)
{
     int i;
     int basin_x=x[j][k],basin_y=y[j][k],temp_x,temp_y;
     if(basin_x<0 && basin_y<0)
         return ;
     while(basin_x >=0 && basin_y>=0)
     {
         temp_x=basin_x;temp_y=basin_y;
         basin_x=x[temp_x][temp_y];basin_y=y[temp_x][temp_y];
     }
     for(i=0;i<basin_times;i++)
         if(temp_x==basin_backup[i][0] && temp_y==basin_backup[i][1])
             break;
     if(j<basin[i][0] ||(j==basin[i][0]&&k<basin[i][1]))
     {
         basin[i][0]=j;basin[i][1]=k;
     }
}

char GetChar(int j,int k)
{
     if(ch[x[j][k]][y[j][k]] !=' ')
         return ch[x[j][k]][y[j][k]];
     else
         return GetChar(x[j][k],y[j][k]);
}

int main()
{
    int i,j,k,l;
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d",&H);
        scanf("%d",&W);
        for(j=0;j<H;j++)
            for(k=0;k<W;k++)
        {
            scanf("%d",&data[j][k]);
            ch[j][k]=' ';x[j][k]=-1;y[j][k]=-1;
        }
        for(j=0;j<H;j++)
            for(k=0;k<W;k++)
        {
            if(j-1 >=0 && data[j][k]>data[j-1][k])
            {
                x[j][k]=j-1;y[j][k]=k;
            }
            if(k-1 >=0 && data[j][k]>data[j][k-1])
            {
                if(x[j][k]>=0 && y[j][k]>=0)
                {
                    if(data[j][k-1]<data[x[j][k]][y[j][k]])
                    {
                        x[j][k]=j;y[j][k]=k-1;
                    }
                }
                else
                {
                    x[j][k]=j;y[j][k]=k-1;
                }
            }
            if(k+1 <W && data[j][k]>data[j][k+1])
            {
                if(x[j][k]>=0 && y[j][k]>=0)
                {
                    if(data[j][k+1]<data[x[j][k]][y[j][k]])
                    {
                        x[j][k]=j;y[j][k]=k+1;
                    }
                }
                else
                {
                    x[j][k]=j;y[j][k]=k+1;
                }
            }
            if(j+1 <H && data[j][k]>data[j+1][k])
            {
                if(x[j][k]>=0 && y[j][k]>=0)
                {
                    if(data[j+1][k]<data[x[j][k]][y[j][k]])
                    {
                        x[j][k]=j+1;y[j][k]=k;
                    }
                }
                else
                {
                    x[j][k]=j+1;y[j][k]=k;
                }
            }
        }
        
        basin_times=0;
        for(j=0;j<H;j++)
            for(k=0;k<W;k++)
        {
            if(x[j][k]<0 && y[j][k]<0)
            {
                basin[basin_times][0]=j;
                basin[basin_times][1]=k;
                basin_backup[basin_times][0]=j;
                basin_backup[basin_times][1]=k;
                basin_times++;
            }
        }
        for(l=0;l<basin_times;l++)
        {
            for(j=0;j<H;j++)
                for(k=0;k<W;k++)
            {
                FindMix(j,k);
            }
        }
        for(j=0;j<basin_times;j++)
            for(k=j+1;k<basin_times;k++)
        {
            if(basin[j][0]>basin[k][0] ||(basin[j][0]==basin[k][0] && basin[j][1]>basin[k][1]))
            {
                int temp=basin[j][0];
                basin[j][0]=basin[k][0];
                basin[k][0]=temp;
                temp=basin[j][1];
                basin[j][1]=basin[k][1];
                basin[k][1]=temp;
            }
        }
        letter='a';
        for(j=0;j<basin_times;j++)
            ch[basin[j][0]][basin[j][1]]=letter++;
        for(j=0;j<basin_times;j++)
        {
            int basin_x=basin[j][0],basin_y=basin[j][1],temp_x,temp_y;
            while(x[basin_x][basin_y]>=0 &&y[basin_x][basin_y]>=0)
            {
                temp_x=basin_x;temp_y=basin_y;
                basin_x=x[temp_x][temp_y];basin_y=y[temp_x][temp_y];
                ch[basin_x][basin_y]=ch[basin[j][0]][basin[j][1]];
            }
        }
        for(j=0;j<H;j++)
            for(k=0;k<W;k++)
        {
            if(ch[j][k] != ' ')
                continue;
            ch[j][k]=GetChar(j,k);
        }
        printf("Case #%d:\n",i);
        for(j=0;j<H;j++)
        {
            printf("%c",ch[j][0]);
            for(k=1;k<W;k++)
                printf(" %c",ch[j][k]);
            printf("\n");
        }  
    }
    fflush(stdout);
    return 0;
}

