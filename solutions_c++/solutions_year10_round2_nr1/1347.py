#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
int t,n,m;
char path[210][111];
int res, nmb;
char a[111],tmp[111];
int j;
int count(char *a)
{

    bool ok = true;
    
    tmp[j++] = '/';
    while((j<111)&&(a[j]!='/'))
    {
        if(a[j]!='?')
        {
            
            tmp[j] = a[j];
            a[j] ='?';
            ok = false;
            
        }
        ++j;        
    }
        
    
    if(a[j] == '/')
    {
        a[j] = '?';
    }
/*    for(int __ = j;__<111;++__)
    {
        if(((a[__]>=48)&&(a[__]<=57))||((a[__]<=122)&&(a[__]>=97)))
        {
            ok = false;         
            break;
        }
        
    }*/
    if(ok) 
    {
        return 0;   
    }        
    for(int _ = 0;_<=nmb;++_)
    {
        
        if(strcmp(tmp, path[_])==0)
        {
            
            return count(a);
        }
    }
    ++nmb;
    for(int __=0;__<111;++__)
        path[nmb][__] = tmp[__];
    return count(a) + 1;
}
int main()
{
    
    scanf("%d",&t);
    for(int i = 0; i < t; ++i)
    {
        nmb = 0;
        res = 0;
        scanf("%d %d",&n,&m);
        for(int _=0;_<n; ++_)
        {
            scanf("%s",&path[_]);   
            ++nmb;
        }
        path[100][0] = '/';
        ++nmb;
        for(int _=0;_<m;++_)
        {
            j = 0;
            scanf("%s",&a);
            int restmp = count(a);
            res += restmp;
            for(int __ = 0; __<111;++__)
            {
                tmp[__] = 0;   
            }
        
        }
        printf("Case #%d: %d\n",i+1,res);
    }
    
    
    
    return 0;   
}
