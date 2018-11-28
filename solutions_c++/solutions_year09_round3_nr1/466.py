#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

long long pow(long long x, long long y)
{
    int i;
    long long sum = 1;
    for(i=1;i<=y;i++) sum *=  x;
    return(sum);
}

int main(int argc, char *argv[])
{   
    int t,o;
    //freopen("E:/in.txt","r",stdin);
 //freopen("E:/out.txt","w",stdout);
    scanf("%d",&t);
    for(o=1;o<=t;o++)
    {
        long long  i,j,k,l;
        string s;
        cin>>s;
        l = s.length();
        bool p[130] = {false};
        long long int num[130] = {0};
        long long int r = 0;
        for(i=0;i<l;i++)
        {
            if(!p[s[i]])
            {
                r ++;
                p[s[i]] = true;
            }
        }
        if(r==1) r++;
        memset(p,false,sizeof(p));
        k = -1;
        p[s[0]] = 1;
        num[s[0]] = 1;
        for(i=1;i<l;i++)
        {
           if(!p[s[i]])
           {
               k++;
               if(k==1) k++;
               num[s[i]] = k;
               p[s[i]] = true;
           }
        }
        
        long long ans = 0;
        for(i=0;i<l;i++)
        {
            ans += num[s[i]]*pow(r,l-i-1);
        }
        printf("Case #%d: %lld\n",o,ans);
    }
    return EXIT_SUCCESS;
}
