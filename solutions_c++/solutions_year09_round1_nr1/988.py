#include <cstdlib>
#include <iostream>

using namespace std;

int sum(int n, int r)
{
    int m = 0, ans = 0;
    m = n;
    while(m > 0)
    {
        int k = m%r;
        m = m / r;
        ans += k*k;
    }
    return(ans);
}

bool base(int n, int r)
{
     int i,j,k;
     bool p[10000]={false};
     k =  sum(n,r);
     p[k] = true;
     for(i=1;i<=1000;i++)
     {
         if(k == 1) return(true);
         k = sum(k,r);
         if(p[k]) return(false);
         else p[k] = true;
     }
     return(false);
}

int main(int argc, char *argv[])
{
    int t, o;freopen("E:/in.txt","r",stdin);
freopen("E:/out.txt","w",stdout);
    scanf("%d",&t);
    getchar();
    for(o=1;o<=t;o++)
    {
        int i,j,k;
        char s[20];
        gets(s);
        int l =  strlen(s);
        int n[20],len = 0;
        for(i=0;i<l;)
        {
            if(s[i]>='0' && s[i]<='9' && s[i+1]>='0' && s[i+1]<='9') { n[++len] = 10; i+=2;}
            else if(s[i]>='0' && s[i]<='9') { n[++len] = s[i]-'0'; i++; }
            i++;
        }
        for(i=2;i<=1000000;i++)
        {
            bool flag = true;
            for(j=1;j<=len;j++)
            {
                if(!base(i,n[j]))
                {
                    flag =  false;
                    break;
                }
            }
            if(flag) break;
        }
        
        printf("Case #%d: %d\n",o,i);
    }
    return EXIT_SUCCESS;
}
