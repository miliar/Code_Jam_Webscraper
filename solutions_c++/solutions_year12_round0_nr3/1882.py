#include<stdio.h>
int main()
{
    int a,b,c,d,e,n,p,q,k,len,x,y,z,l,out,i;
    int ch[10],ck;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&n);
    for(a=0;a<n;a++)
    {
        out=0;
        scanf("%d%d",&p,&q);
        for(b=0,k=p;;b++,k/=10)
            if(k==0)
                break;
        len=b;
        for(b=p;b<q;b++)
            for(c=1,i=0;c<len;c++)
            {
                for(d=0,l=1;d<c;d++)
                    l*=10;
                x= b%l;
                z= b/l;
                for(d=0,y=1;d<len-c;d++)
                    y*=10;
                k= (x*y+z);
                if(k/p!=0)
                {
                    if(k>b && k<=q)
                    {
                        //printf("%d = %d\n",b,k);
                        for(e=0,ck=0;e<i;e++)
                            if(k==ch[e])
                                ck=1;
                        if(ck==0)
                        {
                            ch[i]=k;
                            i++;
                            out++;
                        }
                    }
                }
                    
            }
        printf("Case #%d: %d\n",a+1,out);
    }
    scanf(" ");
}
