#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t;
    char a[4][4];
    scanf("%d\n",&t);
    for(int m=1;m<=t;m++)
    {
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            scanf("%c",&a[i][j]);
	    scanf("\n");
        }
    bool flag=0;
    bool e=0;
    int status=0;
   
    int x=0,o=0;
    for(int i=0;i<4;i++)
    {
        x=0;o=0;
        for(int j=0;j<4;j++)
        {
            if(a[i][j]=='X')
            x++;
            else if(a[i][j]=='O')
            o++;
            else if(a[i][j]=='T')
            {
            x++;
            o++;
            }
            else if(a[i][j]=='.')
            e=1;
            if(x==4)
            {
                flag=1;
                status=1;
                break;
            }
            else if(o==4)
            {
                flag=1;
                status=2;
                break;
            }
        }
        if(flag==0)
        {
        for(int j=0;j<4;j++)
        {
        x=0;o=0;
        for(int i=0;i<4;i++)
        {
            if(a[i][j]=='X')
            x++;
            else if(a[i][j]=='O')
            o++;
            else if(a[i][j]=='T')
            {
            x++;
            o++;
            }
            else if(a[i][j]=='.')
            e=1;
            if(x==4)
            {
                flag=1;
                status=1;
                break;
            }
            else if(o==4)
            {
                flag=1;
                status=2;
                break;
                }
            }
        }
    }
    if(flag==0)
    {
	x=0;o=0;
        for(int i=0;i<4;i++)
        {
            if(a[i][i]=='X')
            x++;
            else if(a[i][i]=='O')
            o++;
            else if(a[i][i]=='.')
            e=1;
            else if(a[i][i]=='T')
            {
            x++;
            o++;
            }
            if(x==4)
            {
                flag=1;
                status=1;
                break;
            }
            else if(o==4)
            {
                flag=1;
                status=2;
                break;
                }
        }
    }
    if(flag==0)
    {
	x=0;o=0;
      for(int i=0;i<4;i++)
        {
            if(a[i][3-i]=='X')
            x++;
            else if(a[i][3-i]=='O')
            o++;
            else if(a[i][3-i]=='.')
            e=1;
            else if(a[i][3-i]=='T')
            {
            x++;
            o++;
            }
            if(x==4)
            {
                flag=1;
                status=1;
                break;
            }
            else if(o==4)
            {
                flag=1;
                status=2;
                break;
                }
        }  
    }
    }
     if(flag==1)
    {
        if(status==1)
        printf("Case #%d: X won\n",m);
        else if(status==2)
        printf("Case #%d: O won\n",m);
        
    }
    else if(flag==0)
    {
        if(e==1)
        printf("Case #%d: Game has not completed\n",m);
        else
        printf("Case #%d: Draw\n",m);
    }   
}
}