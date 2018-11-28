#include <iostream>
#include <cmath>

using namespace std;

int v[512];
int num[50];
char s[1000];

int main()
{
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int cases,i,j,caseid;
    __int64 ans,b,w;
    scanf("%d", &cases);
    for(caseid=1; caseid<=cases; ++caseid)
    {             
        scanf("%s", s);     
        memset(v, -1, sizeof(v)); 
        memset(num, 0, sizeof(num));
        int len = strlen(s);
        v[s[0]]=1;b=1;
        for(i=1,j=0; i<len; ++i)
        {
            if(v[s[i]]==-1) v[s[i]]=j,++b,++j;
            if(j==1) ++j;
        }
        
        if(b==1) ++b;
        for(i=0; i<len; ++i)
            num[i]=v[s[i]];         
        ans=0;w=1;
        for(i=len-1; i>=0; --i)
        {
            ans+=(__int64)num[i]*w;w*=b;
        }
        printf("Case #%d: %I64d\n", caseid, ans);
    }
    
    return 0;    
}
