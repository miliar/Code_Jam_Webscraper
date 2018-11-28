/*
TASK: water
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#define INF 1000000

FILE *fin,*fout;
int t;
int h,w;
int a[105][105];
char b[105][105];
int st[10100],top;

int clearall()
{
    int i,j;
    for(i=0;i<105;i++) for(j=0;j<105;j++) {a[i][j] = INF; b[i][j] = 0;}
}

int main()
{
    
    fin = fopen("B-large.in","r");
    fout = fopen("water.out","w");
    
    fscanf(fin,"%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        char naw = 'a';
        fscanf(fin,"%d %d",&h,&w);
        clearall();
        int i,j,in,jn;
        for(i=1;i<=h;i++) for(j=1;j<=w;j++)
        {
            fscanf(fin,"%d",&a[i][j]);
        }
        for(int zi=1;zi<=h;zi++) for(int zj=1;zj<=w;zj++)
        {
            i = zi; j = zj;
            if(b[i][j] == 0)
            {
                top = 0;
                while(1)
                {
                    in = i-1; jn = j;
                    if(a[i][j-1] < a[in][jn]) {in = i; jn = j-1;}
                    if(a[i][j+1] < a[in][jn]) {in = i; jn = j+1;}
                    if(a[i+1][j] < a[in][jn]) {in = i+1; jn = j;}
                    //printf("%d %d\n",in,jn);
                    //system("PAUSE");
                    if(a[in][jn] >= a[i][j])
                    //back up
                    {
                        b[i][j] = naw;
                        while(top>0)
                        {
                            top--;
                            b[st[top]/1000][st[top]%1000] = naw;
                        }
                        naw++;
                        break;
                    }
                    if(b[in][jn] != 0)
                    {
                        b[i][j] = b[in][jn];
                        while(top>0)
                        {
                            top--;
                            b[st[top]/1000][st[top]%1000] = b[in][jn];
                        }
                        break;
                    }
                    st[top] = i*1000+j;
                    top++;
                    i = in; j = jn;
                }
            }
            /*
            printf("d\n");
            for(int iii=1;iii<=h;iii++) for(int jjj=1;jjj<=w;jjj++)
            {
                printf("%c",b[iii][jjj]);
                if(jjj!=w) printf(" ");
                else printf("\n");
            }   
            system("PAUSE");
            */
        }
        fprintf(fout,"Case #%d:\n",tt);
        for(i=1;i<=h;i++) for(j=1;j<=w;j++)
        {
            fprintf(fout,"%c",b[i][j]);
            if(j!=w) fprintf(fout," ");
            else fprintf(fout,"\n");
        }
    }
    
    return 0;
}
