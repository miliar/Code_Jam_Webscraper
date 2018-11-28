# include<iostream>
# include<stdio.h>
using namespace std;
int main()
{
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
    int t=0,a,n;
    char map[10][10];
    scanf("%d",&n);
    while(n--)
    {
        printf("Case #%d: ",++t);
        int i,j,s1,s2,s0,f=0;
        getchar();
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            scanf("%c",&map[i][j]);
            getchar();
        }
		/*for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				printf("%c",map[i][j]);*/
        for(i=0;i<4;i++)
        {
            s1=0,s2=0;s0=0;
            for(j=0;j<4;j++)
            {
                if(map[i][j]=='T')
                {
                    s0++;
                }
                if(map[i][j]=='X')
                {
                    s1++;
                }
                if(map[i][j]=='O')
                {
                    s2++;
                }
            }
		    //printf("%d%d%d",s0,s1,s2);
            if(s1==4||s1+s0==4)
            {
                f=1;
                printf("X won\n");
                break;
            }
            if(s2==4||s2+s0==4)
            {
                f=1;
                printf("O won\n");
                break;
            }
        }
		if(f==1)
			continue;
        if(f==0)
        {
            for(i=0;i<4;i++)
            {
                s1=0,s2=0;s0=0;
                for(j=0;j<4;j++)
                {
                    if(map[j][i]=='T')
                    {
                        s0++;
                    }
                    if(map[j][i]=='X')
                    {
                        s1++;
                    }
                    if(map[j][i]=='O')
                    {
                        s2++;
                    }
                }
                if(s1==4||s1+s0==4)
                {
                    f=1;
                    printf("X won\n");
                    break;
                }
                if(s2==4||s2+s0==4)
                {
                    f=1;
                    printf("O won\n");
                    break;
                }
            }
        }
		if(f==1)
			continue;
        if(f==0)
        {
            s1=0,s2=0;s0=0;
            for(i=0;i<4;i++)
            {
                if(map[i][i]=='T')
                {
                    s0++;
                }
                if(map[i][i]=='X')
                {
                    s1++;
                }
                if(map[i][i]=='O')
                {
                    s2++;
                }
            }
            if(s1==4||s1+s0==4)
            {
                f=1;
                printf("X won\n");
            }
            if(s2==4||s2+s0==4)
            {
                f=1;
                printf("O won\n");
            }
        }
		if(f==1)
			continue;
        if(f==0)
        {
            s1=0,s2=0;s0=0;
            for(i=0;i<4;i++)
            {
                if(map[i][3-i]=='T')
                {
                    s0++;
                }
                if(map[i][3-i]=='X')
                {
                    s1++;
                }
                if(map[i][3-i]=='O')
                {
                    s2++;
                }
            }
            if(s1==4||s1+s0==4)
            {
                f=1;
                printf("X won\n");
            }
            if(s2==4||s2+s0==4)
            {
                f=1;
                printf("O won\n");
            }
        }
		if(f==1)
			continue;
        if(f==0)
        {
            for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(map[i][j]=='.')
                {
                    f=1;
                    break;
                }

            }
        }
        if(f==1)
        {
            printf("Game has not completed\n");
        }
        else
        {
            printf("Draw\n");
        }
    }
}
