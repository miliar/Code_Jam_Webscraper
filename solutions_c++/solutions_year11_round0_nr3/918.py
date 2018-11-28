#include<stdio.h>
#include<stdlib.h>
int a[1100];
int sum[15];
int compare(const void *x,const void *y)
{
    return(*(int*)x-*(int*)y);
}
main()
{
    FILE *fin= fopen("C-large.in","r");
    FILE *fout= fopen("candy.txt","w");
    int t,n,i,l,total,p,c;
    fscanf(fin,"%d",&t);
    for(l=0;l<t;l++)
    {
        for(i=0;i<15;i++) sum[i]=0;
        total=0;
        fscanf(fin,"%d",&n);
        for(i=0;i<n;i++)
        {
            fscanf(fin,"%d",&a[i]);
            total+=a[i];
        }
        qsort(a,n,sizeof(int),compare);
        total-=a[0];
        for(i=0;i<n;i++)
        {
            p=0;
            while(a[i]!=0)
            {
                sum[p]+=a[i]%2;
                a[i]/=2;
                p++;
            }
        }
        c=0;
        for(i=0;i<15;i++)
        {
            //printf("%d ",sum[i]);
            if(sum[i]%2!=0) c=1;
        }
        //printf("\n");
        if(c==1) fprintf(fout,"Case #%d: NO\n",l+1);
        else fprintf(fout,"Case #%d: %d\n",l+1,total);
        //if(c==1) printf("Case #%d: NO\n",l+1);
        //else printf("Case #%d: %d\n",l+1,total);
    }
    //scanf(" ");
}
