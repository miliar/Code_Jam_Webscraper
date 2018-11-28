#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char name[105][105],find[105];
int have[105],sum;

int sort_function(const void *a,const void *b)
{   return strcmp((char *)a,(char *)b);
}
int search(int be,int end)
{   int mid;
    mid=(be+end)/2;
    if(strcmp(find,name[mid])==0) return mid;
    if(strcmp(find,name[mid])<0) return search(be,mid-1);
    return search(mid+1,end);
}

int main()
{   int n,s,q,i,j,k,in,ans;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {   sum=0;
        ans=0;
        scanf("%d",&s);
        for(j=0;j<s;j++)
            have[j]=0;
        gets(name[0]);
        for(j=0;j<s;j++)
            gets(name[j]);
        qsort((void *)name,s,sizeof(name[0]),sort_function);
        scanf("%d",&q);
        gets(find);
        for(j=0;j<q;j++)
        {   gets(find);
            in=search(0,s-1);
            if(have[in]==0)
            {   sum++;
                if(sum==s)
                {   ans++;
                    //printf("+\n");
                    for(k=0;k<s;k++)
                        have[k]=0;
                    sum=1;
                }
                have[in]=1;
            }
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    //system("pause");
    return 0;
}
