#include<stdio.h>
#include<stdlib.h>
char word[5005][20],q[500],poss[20];
int l,d,n,ans,jump[20];
int be_t,end_t;

int sort_function(const void *a,const void *b)
{   int i=0;
    while( ((char *)a)[i] == ((char *)b)[i] ) i++;
    return ((char *)a)[i]-((char *)b)[i];
}

int bi(int be,int end,int length)
{   int mid,i=0;
    if(be>end) return 0;
    mid=(be+end)/2;
    while(i<length&&word[mid][i]==poss[i]) i++;
    be_t=be;
    end_t=end;
    if(i==length) return 1;
    if(poss[i]<word[mid][i]) return bi(be,mid-1,length);
    return bi(mid+1,end,length);
}

void search(int i,int be,int end)
{   int mid,j,re,p;
    p=jump[i];
    
    /*printf("%d: ",i);
    for(j=0;j<i;j++)
        printf("%c",poss[j]);
    printf("%c",q[p]);
    printf("\n");*/
    
    if(i==l) ans++;
    else if( q[p]!='(' ) 
    {   poss[i]=q[p];
        re=bi(be,end,i+1);
        if(re) search(i+1,be_t,end_t);
    }
    else
    {   p++;
        while( q[p]!=')' )
        {   poss[i]=q[p];
            re=bi(be,end,i+1);
            if(re) search(i+1,be_t,end_t);
            p++;
        }
    }
}

int main()
{   int i,j,k,inout;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d %d %d",&l,&d,&n);
    for(i=0;i<d;i++)
        scanf("%s",word[i]);
    qsort((void *)word,d,sizeof(word[0]),sort_function);
        
    for(k=0;k<n;k++)
    {   scanf("%s",q);
        if(q[0]=='(') inout=1;
        else inout=0;
        jump[0]=0;
        i=j=1;
        while(q[i]!='\0')
        {   if(inout==0) //out
            {   jump[j]=i;
                if(q[i]=='(') inout=1;
                j++;
                //printf("out\n");
            }
            else //in
            {   if(q[i]==')') inout=0;
            }
            i++;
        }
        jump[j]=i;
        //for(i=0;i<=l;i++)
        //    printf("%d ",jump[i]);
        ans=0;
        search(0,0,d-1);
        printf("Case #%d: %d\n",k+1,ans);
    }
    //system("pause");
    return 0;
}
