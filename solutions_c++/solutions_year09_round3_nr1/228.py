#include <iostream>
#include <string>
using namespace std;

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int xxx[350] = {1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38};
    int T;
    cin>>T;
    for(int i = 1; i <= T; i++)
    {
        string s;
        cin>>s;
        int v = 2;
        int cnt = 0;
        int n[13] = {0};
        int c[33] = {0};
        
        int ss = s.size();
        for(int i = 0; i < ss; i++)
        {
            if(s[i] >= '0' && s[i] <= '9')
            {
                if(n[s[i] - '0']) continue;
                n[s[i] - '0'] = xxx[cnt++];
                printf("%d\n", n[s[i] - '0']);
            }
            else
            {
                if(c[s[i] - 'a']) continue;
                c[s[i] - 'a'] = xxx[cnt++];
            }
        }  
        v = max(v, cnt);
        //printf("%d\n", v);
        int res = 0;
        cnt = 1;
        for(int i = ss-1; i >= 0; i--)
        {
            int mid;
            
            if(s[i] >= '0' && s[i] <= '9')
            {
                mid = n[s[i] - '0']; 
            }
            else
            {
                mid = c[s[i] - 'a'];
            }
            
            printf("%d\n", mid);
            
            res += mid * cnt;
            cnt *= v;
        }
        printf("Case #%d: %d\n", i, res);
    }
    while(1);
} 
