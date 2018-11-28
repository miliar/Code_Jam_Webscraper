#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define S 101
#define A 10000

int t;
int a[S][S];
char res[S][S];
char dict[S*S];
int h, w;

int filled;

void read()
{
    int i,j;

    scanf("%d%d", &h, &w);
    for(i=0; i<h; i++)
    {
        for(j=0; j<w; j++)
        {
            scanf("%d", &a[i][j]);
            res[i][j]=0;
        }
    }

    for(i=0; i<50; i++)
        dict[i]=0;
}

void fillfield()
{
    int i,j, k;
    int actid=1;

    for(k=0; k<A; k++)
    {
        for(i=0; i<h; i++)
        {
            for(j=0; j<w; j++)
            {
                if(a[i][j]==k)
                {
                   if(!res[i][j])
                   {
                       res[i][j] = actid;
                       ++actid;
                   }
                   // fill sourrounding fields
                   // top
                   if(i-1>=0 && !res[i-1][j] && k<a[i-1][j])
                       res[i-1][j]=res[i][j];
                   // right
                   if(j+1<w && !res[i][j+1] && k<a[i][j+1])
                       res[i][j+1]=res[i][j];
                   // bottom
                   if(i+1<h && !res[i+1][j] && k<a[i+1][j])
                       res[i+1][j] = res[i][j];
                   // left
                   if(j-1>=0 && !res[i][j-1] && k<a[i][j-1])
                       res[i][j-1] = res[i][j];
                }
            }
        }
    }

}

void output(int c)
{
    int i,j;
    char act='a';
    printf("Case #%d:\n", c);
    for(i=0; i<h; i++)
    {
        for(j=0; j<w-1; j++)
        {
            if(!dict[res[i][j]])
            {
                dict[res[i][j]] = act;
                ++act;
            }

            printf("%c ", dict[res[i][j]]);
        }
        if(!dict[res[i][w-1]])
        {
            dict[res[i][w-1]] = act;
            ++act;
        }
        printf("%c\n", dict[res[i][w-1]]);
    }
}

int main()
{
    int i,j;

    scanf("%d", &t);

    for(i=0; i<t; i++)
    {
        read();
        fillfield();
        output(i+1);
    }
}
