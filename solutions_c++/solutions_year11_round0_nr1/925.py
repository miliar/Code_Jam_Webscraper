#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int freeo,freeb;
int poso=1,posb=1;
int time=0;
main()
{
    FILE *fin= fopen("A-large.in","r");
    FILE *fout= fopen("bottrust.txt","w");
    int t,n,i,j,l,x;
    char y;
    fscanf(fin,"%d",&t);
    for(l=0;l<t;l++)
    {
        fscanf(fin,"%d",&n);
        freeo=0;freeb=0;poso=1;posb=1;time=0;
        for(i=0;i<n;i++)
        {
            fscanf(fin," %c %d",&y,&x);
            if(y=='O')
            {
                if(fabs((double)(poso-x))<freeo)
                {
                    freeo=0;
                    time++;
                    freeb++;
                }
                else
                {
                    time+=(int)fabs((double)(poso-x))-freeo+1;
                    freeb+=(int)fabs((double)(poso-x))-freeo+1;
                    freeo=0;
                }
                poso=x;
            }
            else if(y=='B')
            {
                if(fabs((double)(posb-x))<freeb)
                {
                    time++;
                    freeb=0;
                    freeo++;
                }
                else
                {
                    time+=(int)fabs((double)(posb-x))-freeb+1;
                    freeo+=(int)fabs((double)(posb-x))-freeb+1;
                    freeb=0;
                }
                posb=x;
            }
        }
        fprintf(fout,"Case #%d: %d\n",l+1,time);
        printf("Case #%d: %d\n",l+1,time);
    }
}
