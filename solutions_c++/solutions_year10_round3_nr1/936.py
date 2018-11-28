#include <cstdio>
#include <cstdlib>

using namespace std;
struct wire
{
    int a,b;
};
int main()
{
    int t,n;
    scanf("%d",&t);
    
    for(int i = 0; i <t; ++i)
    {
        int res = 0;
        scanf("%d", &n);   
        wire w[1000];
        for(int _=0;_<n;++_)
        {
            scanf("%d %d",&w[_].a,&w[_].b);               
        }
        for(int _=0;_<n;++_)
        {
            for(int __=_+1;__<n;++__)
            {
                if(w[__].a <w[_].a)
                {
                    if(w[__].b > w[_].b)
                    {
                        ++res;   
                    }   
                    
                }
                else
                {
                    if(w[__].b < w[_].b)
                    {
                        ++res;   
                        
                    }
                    
                }
            }   
            
        }
        
        printf("Case #%d: %d\n",i+1,res);
    }
    
    
    
    return 0;   
}
