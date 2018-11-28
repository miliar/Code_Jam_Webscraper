#include <cstdio>

using namespace std;


int n,t;
char** a;


int main()
{
    FILE* be=fopen("A-large.in","r");
    FILE* ki=fopen("out.txt","w");
    fscanf(be,"%d",&t);
    for(int c=0; c<t; c++)
    {
        n=4;
        a=new char*[n];
        for(int i=0; i<n; i++)
        {
            a[i]=new char[n];
            for(int j=0; j<n; j++)
            {
                char tempc='\n';
                while(tempc=='\n')
                {
                    fscanf(be,"%c",&tempc);
                }
                a[i][j]=tempc;
            }
        }

        bool xwon,owon,ended;
        xwon=false;
        owon=false;
        ended=true;
        for(int i=0; i<n&&(!xwon&&!owon); i++)
        {
            bool b1=true;
            bool b2=true;
            for(int j=0; j<n; j++)
            {
                if ((a[i][j]=='T') || (a[i][j]=='X'))
                {
                }
                else
                {
                    b1=false;
                }

                if ((a[i][j]=='T') || (a[i][j]=='O'))
                {
                }
                else
                {
                    b2=false;
                }
                if (a[i][j]=='.')
                {
                    ended=false;
                }
            }

            if (!xwon&&!owon)
            {
                if (b1==true)
                {
                    xwon=true;
                }
                else if (b2==true)
                {
                    owon=true;
                }
            }
        }

        for(int i=0; i<n&&(!xwon&&!owon); i++)
        {
            bool b1=true;
            bool b2=true;
            for(int j=0; j<n; j++)
            {
                if ((a[j][i]=='T') || (a[j][i]=='X'))
                {
                }
                else
                {
                    b1=false;
                }

                if ((a[j][i]=='T') || (a[j][i]=='O'))
                {
                }
                else
                {
                    b2=false;
                }
            }

            if (!xwon&&!owon)
            {
                if (b1==true)
                {
                    xwon=true;
                }
                else if (b2==true)
                {
                    owon=true;
                }
            }
        }

        bool b1=true;
        bool b2=true;
        for(int j=0; j<n&&(!xwon&&!owon); j++)
        {
            if ((a[j][j]=='T') || (a[j][j]=='X'))
            {
            }
            else
            {
                b1=false;
            }

            if ((a[j][j]=='T') || (a[j][j]=='O'))
            {
            }
            else
            {
                b2=false;
            }
        }

        if (!xwon&&!owon)
        {
            if (b1==true)
            {
                xwon=true;
            }
            else if (b2==true)
            {
                owon=true;
            }
        }

        b1=true;
        b2=true;
        for(int j=0; j<n&&(!xwon&&!owon); j++)
        {
            if ((a[n-1-j][j]=='T') || (a[n-1-j][j]=='X'))
            {
            }
            else
            {
                b1=false;
            }

            if ((a[n-1-j][j]=='T') || (a[n-j-1][j]=='O'))
            {
            }
            else
            {
                b2=false;
            }
        }
        if (!xwon&&!owon)
        {
            if (b1==true)
            {
                xwon=true;
            }
            else if (b2==true)
            {
                owon=true;
            }
        }

        fprintf(ki,"Case #%d: ",c+1);
        if (xwon)
        {
            fprintf(ki,"X won");
        }
        else if (owon)
        {
            fprintf(ki,"O won");
        }
        else if (!ended)
        {
            fprintf(ki,"Game has not completed");
        }
        else
        {
            fprintf(ki,"Draw");
        }
        fprintf(ki,"\n");
    }


    fclose(be);
    fclose(ki);
    return 0;
}
