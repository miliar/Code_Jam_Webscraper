#include<iostream>
#include<stdio.h>
using namespace std;


int main()
{
    FILE *fp;
    FILE *ip;
    fp=fopen("output.txt","w");
    ip=fopen("input.dat","r");
    int i=0;
    int t;
    char c;
    scanf("%d",&t);

    cout<<t;
    while(t--)
    {

        i++;
        char a[5][5];int n=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf(" %c",&a[i][j]);
                if(a[i][j]=='.')
                    n++;
            }

        }


        char w;
        w=a[0][0];
        for(int i=0;i<4;i++)
        {
            w=a[i][0];
            if(w=='.')
                continue;
            for(int j=1;j<4;j++)
            {
                if(a[i][j]!=w)
                {

                    if(w=='T')
                    {
                        w=a[i][j];
                        continue;
                    }
                    else if(a[i][j]=='T')
                    {
                        continue;
                    }
                    else
                    {
                        w='D';
                        break;
                    }

                }


            }
            if(w=='O'||w=='X')
            {
                break;
            }
        }

        if(w=='O'||w=='X')
        {

            fprintf(fp,"Case #%d: %c won\n",i,w);
            continue;
        }

        for(int i=0;i<4;i++)
        {
            w=a[0][i];
            if(w=='.')
                continue;
            for(int j=1;j<4;j++)
            {


                if(a[j][i]!=w)
                {
                    if(w=='T')
                    {
                        w=a[j][i];
                        continue;
                    }
                    else if(a[j][i]=='T')
                    {
                        continue;
                    }
                    else
                    {
                        w='D';
                        break;
                    }
                }


            }
            if(w=='O'||w=='X')
                {
                    break;
                }


        }

        if(w=='O'||w=='X')
        {
            fprintf(fp,"Case #%d: %c won\n",i,w);
            continue;
        }
        w=a[0][0];
        for(int i=1;i<4;i++)
        {

            if(a[i][i]!=w)
                {
                    if(w=='T')
                    {
                        w=a[i][i];
                        continue;
                    }
                    else if(a[i][i]=='T')
                    {
                        continue;
                    }
                    else
                    {
                        w='D';
                        break;
                    }
                }
        }

        if(w=='O'||w=='X')
        {
            fprintf(fp,"Case #%d: %c won\n",i,w);
            continue;
        }

        w=a[0][3];
        for(int i=1;i<4;i++)
        {
            if(a[i][3-i]!=w)
                {
                    if(w=='T')
                    {
                        w=a[i][3-i];
                        continue;
                    }
                    else if(a[i][3-i]=='T')
                    {
                        continue;
                    }
                    else
                    {
                        w='D';
                        break;
                    }
                }
        }
        if(w=='O'||w=='X')
        {
            fprintf(fp,"Case #%d: %c won\n",i,w);
            continue;
        }

        if(n>0)
        {
            fprintf(fp,"Case #%d: Game has not completed\n",i);
        }
        else
            fprintf(fp,"Case #%d: Draw\n",i);

    }
    fclose(fp);
    fclose(ip);
    return 0;
}

