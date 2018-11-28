#include <cstdio>


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,ncase = 0;
    int n,s,p;
    scanf("%d",&t);
    while(t--){
        int ans = 0,x;
        scanf("%d%d%d",&n,&s,&p);
        for(int i = 0; i < n; i++){
            scanf("%d",&x);
            int d  = x % 3;
            switch(d){
                case 0: if(x/3 >= p && x/3 <= 10) ans++;
                        else if(s > 0 && x/3+1 >= p && x/3+1 <= 10 && x/3-1 >= 0) ans++,s--;
                        break;
                case 1:if(x/3+1 >= p && x/3+1 <= 10 && x/3 >= 0) ans++;
                        break;
                case 2: if(x/3+1 >= p && x/3+1 <= 10 && x/3 >= 0) ans++;
                        else if(s > 0 && x/3+2 >= p && x/3+2 <= 10 && x/3 >= 0) ans++,s--;
                        break;
            }
        }
        printf("Case #%d: %d\n",++ncase,ans);

    }
    return 0;
}

