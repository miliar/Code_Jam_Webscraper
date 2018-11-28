#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    char a[4][4];
    char c[2];
    int k,aa=1,n;
    scanf("%d",&k);
    int i,stat=0,j;
    //printf("x=%d\n",x);
    aa=k;
    for(n=0;n<k;n++)
    {
       // printf("%d %d %d\n",aa,k,k-aa);
        stat=0;

        int count=0;
        for(i=0;i<4;i++)
        scanf("%s",a[i]);
        gets(c);
        printf("Case #");
        cout<<n+1<<": ";
        for(i=0;i<4;i++)
        {
            count=0;
            if(a[i][0]=='T')
            count++;
            if(a[i][1]=='T')
            count++;
            if(a[i][2]=='T')
            count++;
            if(a[i][3]=='T')
            count++;
            if(count<=1)
            {
                int count1=0;
                if(a[i][0]=='X')
                count1++;
                if(a[i][1]=='X')
                count1++;
                if(a[i][2]=='X')
                count1++;
                if(a[i][3]=='X')
                count1++;
                if(count+count1==4)
                stat=1;
                //printf("count1=%d\ncount=%d\n",count1,count);
            }
        }
        if(stat==1)
        {
            printf("X won\n");
            //p++;
            continue;
        }
        for(i=0;i<4;i++)
        {
            count=0;
            if(a[i][0]=='T')
            count++;
            if(a[i][1]=='T')
            count++;
            if(a[i][2]=='T')
            count++;
            if(a[i][3]=='T')
            count++;
            if(count<=1)
            {
                int count1=0;
                if(a[i][0]=='O')
                count1++;
                if(a[i][1]=='O')
                count1++;
                if(a[i][2]=='O')
                count1++;
                if(a[i][3]=='O')
                count1++;
                if(count+count1==4)
                stat=2;
                //printf("count1=%d\ncount=%d\n",count1,count);
            }
        }
        if(stat==2)
        {
            printf("O won\n");
            //p++;
            continue;
        }

        for(i=0;i<4;i++)
        {
            count=0;
            if(a[0][i]=='T')
            count++;
            if(a[1][i]=='T')
            count++;
            if(a[2][i]=='T')
            count++;
            if(a[3][i]=='T')
            count++;
            if(count<=1)
            {
                int count1=0;
                if(a[0][i]=='O')
                count1++;
                if(a[1][i]=='O')
                count1++;
                if(a[2][i]=='O')
                count1++;
                if(a[3][i]=='O')
                count1++;
                if(count+count1==4)
                stat=3;
                //printf("count1=%d\ncount=%d\n",count1,count);
            }
        }
        if(stat==3)
        {
            printf("O won\n");
            //p++;
            continue;
        }

        for(i=0;i<4;i++)
        {
            count=0;
            if(a[0][i]=='T')
            count++;
            if(a[1][i]=='T')
            count++;
            if(a[2][i]=='T')
            count++;
            if(a[3][i]=='T')
            count++;
            if(count<=1)
            {
                int count1=0;
                if(a[0][i]=='X')
                count1++;
                if(a[1][i]=='X')
                count1++;
                if(a[2][i]=='X')
                count1++;
                if(a[3][i]=='X')
                count1++;
                if(count+count1==4)
                stat=4;
                //printf("count1=%d\ncount=%d\n",count1,count);
            }
        }
        if(stat==4)
        {
            printf("X won\n");
            //p++;
            continue;
        }
        count=0;
        if(a[0][0]=='T')
        count++;
        if(a[1][1]=='T')
        count++;
        if(a[2][2]=='T')
        count++;
        if(a[3][3]=='T')
        count++;
        if(count<=1)
        {
            int count1=0;
            if(a[0][0]=='O')
            count1++;
            if(a[1][1]=='O')
            count1++;
            if(a[2][2]=='O')
            count1++;
            if(a[3][3]=='O')
            count1++;
            if(count+count1==4)
            stat=5;
            //printf("count1=%d\ncount=%d\n",count1,count);
        }
        if(stat==5)
        {
            printf("O won\n");
            //p++;
            continue;
        }
        count=0;
        if(a[0][0]=='T')
        count++;
        if(a[1][1]=='T')
        count++;
        if(a[2][2]=='T')
        count++;
        if(a[3][3]=='T')
        count++;
        if(count<=1)
        {
            int count1=0;
            if(a[0][0]=='X')
            count1++;
            if(a[1][1]=='X')
            count1++;
            if(a[2][2]=='X')
            count1++;
            if(a[3][3]=='X')
            count1++;
            if(count+count1==4)
            stat=6;
            //printf("count1=%d\ncount=%d\n",count1,count);
        }
        if(stat==6)
        {
            printf("X won\n");
            //p++;
            continue;
        }
        count=0;
        if(a[0][3]=='T')
        count++;
        if(a[1][2]=='T')
        count++;
        if(a[2][1]=='T')
        count++;
        if(a[3][0]=='T')
        count++;
        if(count<=1)
        {
            int count1=0;
            if(a[0][3]=='X')
            count1++;
            if(a[1][2]=='X')
            count1++;
            if(a[2][1]=='X')
            count1++;
            if(a[3][0]=='X')
            count1++;
            if(count+count1==4)
            stat=7;
            //printf("count1=%d\ncount=%d\n",count1,count);
        }
        if(stat==7)
        {
            printf("X won\n");
            continue;
        }
        count=0;
        if(a[0][3]=='T')
        count++;
        if(a[1][2]=='T')
        count++;
        if(a[2][1]=='T')
        count++;
        if(a[3][0]=='T')
        count++;
        if(count<=1)
        {
            int count1=0;
            if(a[0][3]=='O')
            count1++;
            if(a[1][2]=='O')
            count1++;
            if(a[2][1]=='O')
            count1++;
            if(a[3][0]=='O')
            count1++;
            if(count+count1==4)
            stat=8;
            //printf("count1=%d\ncount=%d\n",count1,count);
        }
        if(stat==8)
        {
            printf("O won\n");
            continue;
        }
        count=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i][j]!='.')
                count++;
            }
        }
        if(count==16)
        {
            printf("Draw\n");
        }
        else
        {
            printf("Game has not completed\n");
        }
    }
    return 0;
}
