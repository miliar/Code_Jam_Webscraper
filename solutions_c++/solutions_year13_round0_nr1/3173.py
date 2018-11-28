#include<stdio.h>

char table[10][10];
int checkSpace;

int check(int sx,int sy,int px,int py,char target)
{
    while(1)
    {
        if(table[sx][sy]!=target && table[sx][sy]!='T')
        {
            return 0;
        }      
        sx+=px;
        sy+=py;
        if(sx>=4 || sy>=4)
        {
            break;
        }    
    }    
    return 1;
}    

void analysis()
{
    if(check(0,0,1,0,'O')||check(0,1,1,0,'O')||check(0,2,1,0,'O')||check(0,3,1,0,'O')||
    check(0,0,0,1,'O')||check(1,0,0,1,'O')||check(2,0,0,1,'O')||check(3,0,0,1,'O')||
    check(0,0,1,1,'O')||check(0,3,1,-1,'O'))
    {
        printf("O won\n");
        return;
    }    
    if(check(0,0,1,0,'X')||check(0,1,1,0,'X')||check(0,2,1,0,'X')||check(0,3,1,0,'X')||
    check(0,0,0,1,'X')||check(1,0,0,1,'X')||check(2,0,0,1,'X')||check(3,0,0,1,'X')||
    check(0,0,1,1,'X')||check(0,3,1,-1,'X'))
    {
        printf("X won\n");
        return;
    }
    if(checkSpace==1)
    {
        printf("Game has not completed\n");
        return;
    } 
    printf("Draw\n");
}

void input()
{
    for(int i=0;i<4;i++)
    {
        scanf("%s",table[i]);
        for(int j=0;j<4;j++)
        {
            if(table[i][j]=='.')
            {
                checkSpace=1;
            }    
        }    
    }    
}    

int main()
{
    int n;
    char junk[10];
   // freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        checkSpace=0;
        input(); 
        printf("Case #%d: ",i+1);
        analysis();  
        //scanf("%s",junk);
    }    
    return 0;
}    
