#include<cstdio>
#include<vector>
#include<cstring>
using namespace std;

char ch[255][255];
vector< char > oppose[255];
int count[255];
char st[200];

int main() {
    int ntc;
    scanf("%d", &ntc);
    for( int TC=1; TC <= ntc; TC++ ) {
        for( int i=0; i<255; i++ ) oppose[i].clear();
        int ncom, nopp, nstr;
        scanf("%d", &ncom);
        memset( ch, 0, sizeof(ch) );
        for( int i=0; i<ncom; i++ ) {
            char ns[10];
            scanf("%s", ns);
            ch[ ns[0] ][ ns[1] ] = ch[ ns[1] ][ ns[0] ] = ns[2];
        }
        scanf("%d", &nopp);
        for( int i=0; i<nopp; i++ ) {
            char ns[10];
            scanf("%s", ns);
            oppose[ ns[0] ].push_back( ns[1] );
            oppose[ ns[1] ].push_back( ns[0] );
        }
        memset( count, 0, sizeof(count) );
        scanf("%d", &nstr);
        scanf("%s", st);
        
        vector< char > ans;
        for( int i=0; i<nstr; i++ ) {
            int nsize = ans.size();
            if ( nsize > 0 && ch[ ans[nsize-1] ][ st[i] ] > 0 ) {
                char to   = ch[ ans[nsize-1] ][ st[i] ];
                count[ ans[nsize-1] ]--;
                ans.pop_back();
                ans.push_back( to );
                count[ to ]++;
            } else {
                int found = 0;
                for( int k=0; found==0 && k<oppose[ st[i] ].size(); k++ ) {
                    if ( count[ oppose[ st[i] ][k] ] > 0 ) {
                        memset( count, 0, sizeof(count) );
                        ans.clear();
                        found = 1;
                    }
                }
                if ( !found ) {
                    ans.push_back( st[i] );
                    count[ st[i] ]++;
                }
            }
        }
        printf("Case #%d: [", TC);
        for( int i=0; i<ans.size(); i++ ) {
            if ( i > 0 ) printf(", ");
            printf("%c", ans[i]);
        }
        puts("]");
    }
    return 0;
}
