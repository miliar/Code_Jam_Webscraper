#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<iostream>
using namespace std;

int n,m;
vector<string> L[210];
char ch[10010];
string str;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("result.out","w",stdout);
    int test;
    scanf("%d",&test);
    int cas=0;
    while(test--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n+m;i++) L[i].clear();
        for(int i=0;i<n+m;i++)
        {
            scanf("%s",ch);
            int l=strlen(ch);
            int loc=0;
            while(loc<l)
            {
                if(ch[loc]=='/')
                {
                    str="";
                    loc++;
                    while(ch[loc]!='/'&&loc<l)
                    {
                        str+=ch[loc];
                        loc++;
                    }
                    //cout<<str<<endl;
                    L[i].push_back(str);
                }
                else loc++;
            }
        }
        int ans=0;
        for(int j=n;j<n+m;j++)
        {
            int maxnum=0;
            int l1=L[j].size();
            for(int k=0;k<j;k++)
            {
                int l2=L[k].size();
                int t1=0,t2=0;
                int temp=0;
                while(t1<l1&&t2<l2)
                {
                    if(L[j][t1]==L[k][t2])
                    {
                        t1++;
                        t2++;
                        temp++;
                    }
                    else break;
                }
                if(temp>maxnum) maxnum=temp;
            }
            //printf("%d %d\n",l1,maxnum);
            ans+=(l1-maxnum);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
            
                        
                
            
                    
        
        
        
