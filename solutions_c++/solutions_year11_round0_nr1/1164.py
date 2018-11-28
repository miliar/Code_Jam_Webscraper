#include<cstdio>

int ab[105],ao[105],a[105][2],t,n;
int nb,no;

int main(){
    char str[5];
    int in;

    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        nb=0;
        no=0;
        scanf("%d",&n);
        for(int j=0;j<n;j++)
        {
            scanf("%s",str);
            scanf("%d",&in);
            if(str[0]=='B')
            {
                a[j][0]=0;
                ab[nb++]=in;
            }
            else
            {
                a[j][0]=1;
                ao[no++]=in;
            }
            a[j][1]=in;
        }
        /*
        for(int ii=0;ii<n;ii++)
            printf("%d %d, ",a[ii][0],a[ii][1]);
        printf("\n");
        for(int ii=0;ii<nb;ii++)
            printf("%d ",ab[ii]);
        printf("\n");
        for(int ii=0;ii<no;ii++)
            printf("%d ",ao[ii]);
        printf("\n");
        */
        int sol=0,p=0,pb=1,po=1,ib=0,io=0;
        while(p<n)
        {
            sol++;
            int cb=0,co=0;
            if(ib<nb&&pb!=ab[ib])
            {
                if(pb<ab[ib])
                    pb++;
                else
                    pb--;
                cb=1;
            }
            if(io<no&&po!=ao[io])
            {
                if(po<ao[io])
                    po++;
                else
                    po--;
                co=1;
            }
            if(a[p][0]==0)
            {
                if(cb)
                    continue;
                if(pb==ab[ib])
                {
                    ib++;
                    p++;
                }
            }else if(a[p][0]==1)
            {
                if(co)
                    continue;
                if(po==ao[io])
                {
                    io++;
                    p++;
                }
            }
        }
        printf("Case #%d: %d\n",i+1,sol);
    }
    return 0;
}
