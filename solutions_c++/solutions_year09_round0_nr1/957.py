#include<stdio.h>
#include<string.h>

int nx[15*5100][28];
int sz;

char buf[10000];
int l;
void insert(int a, int b)
{   
    if(buf[a]==0)
        return;
    if(nx[b][buf[a]-'a']==-1)
    {
        nx[b][buf[a]-'a']=sz;
        sz++;
    }
    insert(a+1,nx[b][buf[a]-'a']);    
}

bool val[25][30];

int ways(int i, int ti)
{
    if(ti==-1)
        return 0;
    if(i==l)
        return 1;
    int ans=0;
    for(int j=0;j<26;j++)
        if(val[i][j])
            ans+=ways(i+1,nx[ti][j]);
    return ans;

}

int main()
{
    //freopen("A1.in","r",stdin);
    //freopen("A1.out","w",stdout);
    freopen("A2.in","r",stdin);
    freopen("A2.out","w",stdout);
    memset(nx,-1,sizeof(nx));
    sz=1;
    int d,n,i;
    scanf("%d%d%d",&l,&d,&n);

    for(i=0;i<d;i++)
    {
        scanf("%s",buf);
        insert(0,0);
    }
    for(int cs=1;cs<=n;cs++)
    {
        scanf("%s",buf);
        memset(val,0,sizeof(val));
        int k=0;
        for(i=0;i<l;i++)
        {
            if(buf[k]!='(')
            {
                val[i][buf[k]-'a']=1;
                k++;
                continue;
            }
            k++;
            while(buf[k]!=')')
            {
                val[i][buf[k]-'a']=1;
                k++;
            }
            k++;
        }
        int ans=ways(0,0);
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}