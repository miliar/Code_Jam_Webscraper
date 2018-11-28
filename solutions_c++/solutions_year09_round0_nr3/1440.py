#include <cstdio>
#include <iostream>

using namespace std;

#define LINE_LEN    1024
#define MAX_LL  10000000

long long dp1[LINE_LEN], dp2[LINE_LEN];

char pat[21] = "welcome to code jam\0";
char buf[LINE_LEN];

int main()
{
    int K;
    
    cin >> K;
    
    cin.getline(buf, LINE_LEN);
    
    for(int j=1; j<=K; j++)
    {
        memset(dp1, 0, sizeof(dp1));
        memset(dp2, 0, sizeof(dp2));
        
        cin.getline( buf, LINE_LEN );
        
        long long count = 0;
        for(int i=0; buf[i] && i<LINE_LEN; i++)
        {
            if( 'w' == buf[i] )
                count ++;
            dp1[i] = count;            
        }
        
        
        long long *dp_old = dp1, *dp_new = dp2;
        for(int k=1; pat[k]; k++)
        {
            char c = pat[k];
            count = 0;
            dp_new[0] = 0;
            for(int i=1; buf[i]; i++)
            {
                if( c == buf[i] )
                {
                    count += dp_old[ (i-1) ];
                    while( count >= MAX_LL )
                        count -= MAX_LL;
                }
                dp_new[i] = count;
            }
            long long *tmp = dp_new;
            dp_new = dp_old;
            dp_old = tmp;
        }
        
        int _10_3, _10_2, _10_1, _10_0;
        
        _10_3 = (count / 1000) % 10;
        _10_2 = (count / 100) % 10;
        _10_1 = (count / 10) % 10;
        _10_0 = count % 10;
        
        cout << "Case #" << j << ": " << _10_3 << _10_2 << _10_1 << _10_0 << endl;
    }
    
    return 0;
}
