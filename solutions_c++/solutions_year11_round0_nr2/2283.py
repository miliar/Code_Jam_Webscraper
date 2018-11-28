#include<stdio.h>
#include<string.h>
#include<math.h>
int combine[200][200],oppose[200][200];
int main()
{

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    char s[200],ans[200],c1[200],c2[200],o1[200],o2[200];
    int i,j,c,d,n,k,temp,p;
    char a,b,e,cas;

    scanf("%d",&cas);

   for(p=1;p<=cas;p++)
   {
    scanf("%d",&c);
    for(i=0;i<c;i++)
    {
        scanf(" %c%c%c",&a,&b,&e);
        c1[i]=a;
        c2[i]=b;
        combine[a][b]=combine[b][a]=e;
    }
    c1[c]=0;
    c2[c]=0;
    scanf(" %d",&d);

    for(i=0;i<d;i++)
    {
        scanf(" %c%c",&a,&b);
        o1[i]=a;
        o2[i]=b;
        oppose[a][b]=1;
        oppose[b][a]=1;
    }
    o1[d]=0;
    o2[d]=0;
    scanf("%d ",&n);
    for(i=0;i<n;i++)
     scanf("%c",&s[i]);
    s[n]=0;
    k=-1;
    for(i=0;i<n;i++)
    {

        ans[++k]=s[i];
        ans[k+1]=0;

        if(k)
        {


            temp=combine[ans[k-1]][ans[k]];
            if(temp)
            {
                ans[k-1]=temp;
                ans[k]=0;
                k=k-1;
            }
           else
                 {
                     for(j=0;j<k;j++)
                      if(oppose[ans[j]][ans[k]]==1)
                     {
                         ans[0]=0;
                         k=-1;
                         goto out;
                     }
                 }


        }

        out:;

        }

    //printf("%s",ans);

    printf("Case #%d: [",p);
    k=strlen(ans);
    for(i=0;i<k;i++)
     {
         if(i==0)
          printf("%c",ans[i]);
         else
         printf(", %c",ans[i]);

     }
    printf("]\n");

    for(i=0;i<c;i++)
     {
         combine[c1[i]][c2[i]]=combine[c2[i]][c1[i]]=0;
         }

     for(i=0;i<d;i++)
     {
         oppose[o1[i]][o2[i]]=oppose[o2[i]][o1[i]]=0;
         }

   }
    return 0;
}
