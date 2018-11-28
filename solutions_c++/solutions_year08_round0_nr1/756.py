#include<iostream>
#include<map>
using namespace std;
int ans,n,s;
int a[110][1100];
int b[110];
struct str
{
    char a[110];
}t;
bool operator ==(str x,str y)
{
    return strcmp(x.a,y.a)==0;    
}
bool operator <(str x,str y)
{
    return strcmp(x.a,y.a)<0;    
}
map <str,int> m;
int main()
{
    int p,i,j,tmp,ma,flag,k=0,just,now;
    //freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    for(scanf("%d",&p);p--;printf("Case #%d: %d\n",++k,ans))
    {
        m.clear();
		scanf("%d",&n);
        for(i=0;i<n;++i)
        {
                while(gets(t.a)&&strcmp(t.a,"")==0);
                m[t]=i; 
                a[i][0]=0;b[i]=1;   
        }
        scanf("%d",&s);
        for(i=0;i<s;++i)
        {
                 while(gets(t.a)&&strcmp(t.a,"")==0);
                if(m.find(t)!=m.end())
                {
                     j=m[t];
                     a[j][++a[j][0]]=i;  
                }         
        }
        tmp=ma=-1;flag=ans=0,just=-1;
        while(!flag)
        {
       // printf("max:%d %d\n",tmp,ans);  
		for(i=0;i<n;++i)
         {
             while(b[i]<=a[i][0]&&a[i][b[i]]<=tmp)b[i]++;   
            // printf("(%d %d:%d)",i,b[i],a[i][b[i]]);
             if(i!=just&&a[i][0]<b[i])
             {
                    flag=1;break;    
             }
             else
             {
                if(i!=just&&a[i][b[i]]>ma)ma=a[i][b[i]],now=i;     
             }
         }
        // printf("\n");
         if(!flag)ans++;
         tmp=ma;
		 just=now;
       }    
    }  
    return 0;  
}
