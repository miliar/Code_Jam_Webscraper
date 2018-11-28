#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    int N;
    scanf("%d",&N);
    int c = 0;
    while( c < N ) {
        int S,Q;
        scanf("%d",&S);
        map< string, int > dict;
        int i,j,k;
        char buf[200];
        getchar();
        string tmp = "";
        int len = 0;
        for( i = 0; i < S; i++ ) {
            cin.getline(buf,sizeof(buf));
            len = strlen(buf);
            tmp = "";
            for( j = 0; j < len; j++ ) tmp += buf[j];
            dict[tmp] = i+1;
        }
        int dp[2][100];
        memset(dp[0],0,sizeof(dp[0]));
        int base = 0;
        scanf("%d",&Q);
        getchar();
        cin.getline(buf,sizeof(buf));
        tmp = "";
        len = strlen(buf);
        for( i = 0; i < len; i++ ) tmp += buf[i];
        if( dict.find(tmp) != dict.end() ) {
            int id = dict[tmp];
            dp[0][id-1] = -1;
        }
        for( i = 1; i < Q; i++ ) {
            cin.getline(buf,sizeof(buf));
            tmp = "";
            len = strlen(buf);
            for( j = 0; j < len; j++ ) tmp += buf[j];
            int id = -1;
            if( dict.find(tmp) != dict.end() ) {
                id = dict[tmp]-1;
            }
            int next = (base+1)%2;
            memset(dp[next],-1,sizeof(dp[next]));
            for( j = 0; j < S; j++ ) {
                if( j == id ) continue;
                int mm = 1000000;
                for( k = 0; k < S; k++ ) {
                    if( dp[base][k] > -1 ) {
                        if( k != j ) {
                            if( dp[base][k]+1 < mm ) mm = dp[base][k]+1;
                        }
                        else {
                            if( dp[base][k] < mm ) mm = dp[base][k];
                        } 
                    } 
                }
                dp[next][j] = mm;
            }
            base = next;
        }
        int res = 1000000;
        for( i = 0; i < S; i++ )
            if( dp[base][i] > -1 && res > dp[base][i] ) res = dp[base][i];
        printf("Case #%d: %d\n",c+1,res);
        c++;
    }
}
