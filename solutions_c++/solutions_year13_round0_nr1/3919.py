#include<stdio.h>

#define MAX(a,b) a>b? (a):(b)


#define X "X won"
#define O "O won"
#define D "Draw"
#define NC "Game has not completed"


#define BSize 4

bool isInRange(int i,int j)
{
    return (0<=i && i<BSize && 0<=j && j<BSize) ;
}

int convertX(char c)
{
    if(c=='T' || c=='X')
        return 1;
    else
        return 0;
}

int convertO(char c)
{
    if(c=='T' || c=='O')
        return 1;
    else
        return 0;
}

int C4W(int a[4][4],int is,int js)
{
    int i,j,maxs=0,tmp;

    //R
    for(i=is,j=js,tmp=0;isInRange(i,j) && a[i][j]!=0;j++)
        tmp++;
    maxs=MAX(maxs,tmp);
    //D
    for(i=is,j=js,tmp=0;isInRange(i,j) && a[i][j]!=0;i++)
        tmp++;
    maxs=MAX(maxs,tmp);

    //RD
    for(i=is,j=js,tmp=0;isInRange(i,j) && a[i][j]!=0;i++,j++)
        tmp++;
    maxs=MAX(maxs,tmp);

    //RU
    for(i=is,j=js,tmp=0;isInRange(i,j) && a[i][j]!=0;i--,j++)
        tmp++;
    maxs=MAX(maxs,tmp);

    return maxs;
}

int main()
{
    char s[4][5],tmp;
    int T,tt,i,j,maxx,maxo;
    bool isSpace,isWin;

    scanf("%d",&T);

    for(tt=1;tt<=T;tt++)
    {
        int fx[4][4]={0},fo[4][4]={0};

        for(i=0;i<4;i++)
            scanf("%s",s[i]);

        isSpace = false;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                //X
                fx[i][j] = convertX(s[i][j]);
                //O
                fo[i][j] = convertO(s[i][j]);
                if(s[i][j]=='.')
                    isSpace = true;
            }
        }

        maxx = maxo = 0;
        isWin = false;
        for(i=0;i<4 && !isWin;i++)
        {
            for(j=0;j<4 && !isWin;j++)
            {
                //X
                maxx = MAX(maxx,C4W(fx,i,j));
                //O
                maxo = MAX(maxo,C4W(fo,i,j));

                if(maxx==4 || maxo==4)
                    isWin=true;

            }
        }
        //ANS
        printf("Case #%d: ",tt);

        if(maxx==4)
            printf("%s",X);
        else if(maxo==4)
            printf("%s",O);
        else if(isSpace)
            printf("%s",NC);
        else
            printf("%s",D);

        printf("\n");
    }

    return 0;
}
