/*
TASK: D
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>

FILE *fin,*fout;
int h,w,r;
int map[106][106]={0};

int main()
{
    int i,j;
    int ss,sss;
    fin = fopen("D-small-attempt0.in","r");
    fout = fopen("D-small.out","w");
    fscanf(fin,"%d",&sss);
    for(ss=1;ss<=sss;ss++)
    {
        printf("----- %d -----\n",ss);
        fprintf(fout,"Case #%d: ",ss);
        fscanf(fin,"%d %d %d",&h,&w,&r);
        for(i=0;i<106;i++) for(j=0;j<106;j++) map[i][j] = 0;
        int a,b;
        for(i=0;i<r;i++)
        {
            fscanf(fin,"%d %d",&a,&b);
            map[a][b] = -1;
        }
        if(!map[1][1]) map[1][1] = 1;
        int s;
        for(s=2;s<=h+w;s++)
        {
            for(i=1;i<=h;i++)
            {
                j = s-i;
                if(j<1 || j>w) continue;
                if(map[i][j] == -1) continue;
                if(i-2>0 && j-1>0 && map[i-2][j-1]!=-1) map[i][j] += map[i-2][j-1];
                if(i-1>0 && j-2>0 && map[i-1][j-2]!=-1) map[i][j] += map[i-1][j-2];
                map[i][j] = (map[i][j]%10007);
            }
        }
        fprintf(fout,"%d\n",map[h][w]);
        
    }
    system("PAUSE");
    return 0;
}
