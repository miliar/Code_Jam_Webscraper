#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

#define pb push_back

vector <int> br;
char s[25];
int t;


int main()
{
    scanf("%d",&t);
    for (int i = 0; i < t; i++) {
        scanf("%s",s);
        
        br.clear();
        int l = strlen(s);
        for (int j = 0; j < l; j++)
          br.pb( s[j] - '0' );
          
        if ( !next_permutation( br.begin(), br.end() ) ) {
           br.pb( 0 );
           sort( br.begin(), br.end() );
           int p = 0;
           while ( br[p] == 0 ) p++;
           int pom = br[p];
           br[p] = 0;
           br[0] = pom;
           printf("Case #%d: ",i+1);
           for (int j = 0; j < br.size(); j++)
               printf("%d",br[j]);
           printf("\n");
        }
        else {
             printf("Case #%d: ",i+1);
             for (int j = 0; j < br.size(); j++)
               printf("%d",br[j]);
             printf("\n");
        }
    }
    
}
