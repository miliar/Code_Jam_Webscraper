#include<stdio.h>
char a[110];
char com[50][5],op[50][4];
int end;
main()
{
    FILE *fin=fopen("B-large.in","r");
    FILE *fout=fopen("magicka.txt","w");
    int t,l,i,j,n,c,d,sum=0,k;
    char temp;
    fscanf(fin,"%d",&t);
    for(l=0;l<t;l++)
    {
        end=0;
        sum=0;
        fscanf(fin,"%d",&c);
        for(i=0;i<c;i++)
        {
            fscanf(fin," %c%c%c",&com[i][0],&com[i][1],&com[i][2]);
        }
        fscanf(fin,"%d",&d);
        for(i=0;i<d;i++)
        {
            fscanf(fin," %c%c",&op[i][0],&op[i][1]);
        }
        fscanf(fin,"%d ",&n);
        for(i=0;i<n;i++)
        {
            sum=0;
            if(end==0)
            {
                fscanf(fin,"%c",&a[end]);
                end++;
            }
            else
            {
                fscanf(fin,"%c",&a[end]);
                for(j=0;j<c;j++)
                {
                    if((a[end]==com[j][0]&&a[end-1]==com[j][1])||(a[end]==com[j][1]&&a[end-1]==com[j][0]))
                    {
                        end--;
                        a[end]=com[j][2];
                        end++;
                        sum=1;
                        break;
                    }
                }
                if(sum==0)
                {
                    for(j=0;j<d;j++)
                    {
                        for(k=0;k<end;k++)
                        {
                            if((a[k]==op[j][0]&&a[end]==op[j][1])||(a[k]==op[j][1]&&a[end]==op[j][0]))
                            {
                                end=0;
                                sum=1;
                            }
                        }
                    }
                }
                if(sum==0) end++;
            }
        }
        fprintf(fout,"Case #%d: [",l+1);
        if(end>0)
        {
            fprintf(fout,"%c",a[0]);
            for(i=1;i<end;i++) fprintf(fout,", %c",a[i]);
        }
        fprintf(fout,"]\n");
    }
    //scanf(" ");
}
