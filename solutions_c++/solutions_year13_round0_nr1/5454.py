#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int n,m,tc;
    scanf("%d",&tc);
    for(int t=1; t<=tc; t++)
    {
        bool dotFound=false;
        char a[4][4];
        char d;
       scanf("%c",&d);
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
                scanf("%c",&a[i][j]);
            scanf("%c",&d);
        }
        //check row
        bool xwon=false;
        bool owon=false;
        for(int i=0; i<4 && !xwon && !owon; i++)
        {
            int numx=0;
            int numo=0;
            if(a[i][0]=='X' || a[i][0]=='T')
            {
                numx++;
                for(int j=1; j<4; j++) //scan colwise
                {
                    if(a[i][j]=='X' || a[i][j]=='T')
                        numx++;
                    else if(a[i][j]=='.')
                        dotFound=true;
                }
                if(numx==4)
                {
                    xwon=true;
                }
            }
            else if(a[i][0]=='O' || a[i][0]=='T')
            {
                numo++;
                for(int j=1; j<4; j++)
                {
                    if(a[i][j]=='O' || a[i][j]=='T')
                        numo++;
                    else if(a[i][j]=='.')
                        dotFound=true;
                }
                if(numo==4)
                    owon=true;
            }
             else
                dotFound=true;
        }

        //check col
        if(!xwon && !owon)
        {
            for(int j=0; j<4 && !xwon && !owon; j++)
            {
                int numx=0;
                int numo=0;
                if(a[0][j]=='X' || a[0][j]=='T')
                {
                    numx++;
                    for(int i=1; i<4; i++) //scan col
                    {
                        if(a[i][j]=='X' || a[i][j]=='T')
                            numx++;
                        else if(a[i][j]=='.')
                            dotFound=true;

                    }
                    if(numx==4)
                    {
                        xwon=true;
                    }

                }
                else if(a[0][j]=='O' || a[0][j]=='T')
                {
                    numo++;
                    for(int i=1; i<4; i++)
                    {
                        if(a[i][j]=='O' || a[i][j]=='T')
                            numo++;
                        else if(a[i][j]=='.')
                            dotFound=true;
                    }
                    if(numo==4)
                        owon=true;
                }
                 else
                dotFound=true;
            }
        }

        if(!xwon && !owon)
        {
            //diagonal
            int numx=0;
            int numo=0;
            int i=0;
            if(a[0][0]=='X' || a[0][0]=='T')
            {
                numx++;
                for(int i=1; i<4; i++) //scan col
                {
                    if(a[i][i]=='X' || a[i][i]=='T')
                        numx++;
                    else if(a[i][i]=='.')
                        dotFound=true;
                }
                if(numx==4)
                    xwon=true;
            }
            else if(a[0][0]=='O' || a[0][0]=='T')
            {
                numo++;
                for(int i=1; i<4; i++)
                {
                    if(a[i][i]=='O' || a[i][i]=='T')
                        numo++;
                    else if(a[i][i]=='.')
                        dotFound=true;
                }
                if(numo==4)
                    owon=true;
            }
             else
                dotFound=true;


            if(!xwon && !owon)
            {
                //other diagonal
                int numx=0;
                int numo=0;
                int i=0;
                if(a[0][3]=='X' || a[0][3]=='T')
                {
                    numx++;
                    for(int i=1; i<4; i++) //scan col
                    {
                        if(a[i][3-i]=='X' || a[i][3-i]=='T')
                            numx++;
                        else if(a[i][3-i]=='.')
                            dotFound=true;
                    }
                    if(numx==4)
                        xwon=true;
                }
                else if(a[0][3]=='O' || a[0][3]=='T')
                {
                    numo++;
                    for(int i=1; i<4; i++)
                    {
                        if(a[i][3-i]=='O' || a[i][3-i]=='T')
                            numo++;
                        else if(a[i][3-i]=='.')
                            dotFound=true;
                    }
                    if(numo==4)
                        owon=true;
                }
                 else
                dotFound=true;
            }
        }
        if(xwon)
            printf("Case #%d: X won\n",t);
        else if(owon)
            printf("Case #%d: O won\n",t);
        else if(!xwon && !owon && dotFound)
            printf("Case #%d: Game has not completed\n",t);
        else if(!xwon && !owon && !dotFound)
            printf("Case #%d: Draw\n",t);
    }

    return 0;
}
