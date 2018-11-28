#include<cstdio>
#include<cstring>
using namespace std;
FILE *fr, *fw;
int  main()
{
    fr = fopen ("A-large.in", "rt");
    fw = fopen ("op3.txt", "w+");
    int t,z;
        int i,j,k,l,m,n,b,c,d;
        fscanf(fr, "%d",&t);
        for(i=1;i<=t;i++)
        {
            char a[4][5];
            for(j=0;j<4;j++)
            {
                fscanf(fr,"%s",a[j]);
            }
            l=m=b=n=d=c=0;
            for(j=0;j<4;j++)
            {
                l=m=b=c=-1;
                for(k=0;k<4;k++)
                {
                        if(a[j][k]== 'X' || a[j][k]=='T')
                        {

                                l++;
                        }
                        if(a[k][j]== 'X' || a[k][j]=='T')
                        {m++;}
                        if(a[j][k]=='O' || a[j][k]=='T')
                        {b++;}
                        if(a[k][j]=='O' || a[k][j]=='T')
                        {c++;}
                }

                if(l==3 || m==3)
                {
                   n=1;
                }
                if(c==3 || b==3)
                {
                   d=1;
                }

            }
            k=0;
            l=b=-1;
            for(j=0;j<4;j++)
            {
                if(a[j][k]=='X' || a[j][k]=='T')
                l++;
                if(a[j][k]=='O' || a[j][k]=='T')
                b++;
                k++;

                   }
            if(l==3)
            n=2;
            if(b==3)
            d=2;

            k=0;
            l=b=-1;
            for(j=3;j>=0;j--)
            {
                if(a[k][j]=='X' || a[k][j]=='T')
                l++;
                if(a[k][j]=='O' || a[k][j]=='T')
                b++;
                k++;

                                         }
            if(l==3)
            n=3;
            if(b==3)
            d=3;
            z=0;
                for(j=0;j<4;j++)
            {
                for(k=0;k<4;k++)
                {
                        if(a[j][k]=='.')
                        {
                                z=1;
                                break;
                        }
                }
            }
            if((n==1 ||  n==2 || n==3) && d==0)
            fprintf(fw, "Case #%d: X won\n\n",i);
            else if((d==1 || d==2 || d==3) && n==0)
            fprintf(fw, "Case #%d: O won\n\n",i);
            else if(d==0 && n==0 && z==0)
            fprintf(fw, "Case #%d: Draw\n\n",i);
            else if(d==0 && n==0 && z==1)
            fprintf(fw, "Case #%d: Game has not completed\n\n",i);
        }
        return 0;
}
