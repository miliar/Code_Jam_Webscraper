#include <iostream>
#include <algorithm>
using namespace std;

const int inf = 1 << 30;

int num[110];
int wer[13];
int p, q;

int cal()
{
    int res = 0;
    bool asd[110] = {0};
    for(int i = 1; i <= q; i++)
    {
        int now = num[wer[i]];    
        for(int j = now-1; j >= 1;j--)
        {
            if(asd[j]) break;
            res++;    
        }
        for(int j = now+1; j <= p; j++)
        {
            if(asd[j]) break;
            res++; 
        }
        asd[now] = 1;
    }
    return res;    
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;
    for(int qq = 1; qq <= T; qq++)
    {
        cin>>p>>q;
        
        int cnt = 1;
        for(int i = 1; i <= q; i++)
        {
            //cout<<"qqq"<<endl;
            cnt *= i;
            wer[i] = i;
            scanf("%d", &num[i]);
        } 
        //printf("YES\n");
        int res = inf;
        while(cnt--)
        {
            //printf("%d\n", cnt);
            int mid = cal();
            
            res = min(res, mid);
            
            next_permutation(wer+1, wer+1+q);
        }
        printf("Case #%d: %d\n", qq, res);
        //printf("%d\n", res);
    }    
   // while(2);
}
