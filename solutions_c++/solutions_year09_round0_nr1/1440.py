#include <iostream>
using namespace std;

#define MaxL 15
#define MaxD 5000
#define MaxN 500
#define MaxLen 1000

int l,d,n;
int br,ret;
bool otvr, good;
char rec[MaxD][MaxL+5];
char word[MaxLen];
bool mark[MaxL][26];

int main()
{
    scanf("%d %d %d",&l,&d,&n);
    for (int i = 0; i < d; i++)
      scanf("%s",rec[i]);
    
    for (int i = 0; i < n; i++) {
        scanf("%s",word);
        
        br = 0;
        otvr = false;   
        memset(mark, 0, sizeof(mark));
        for (int j = 0; j < strlen(word); j++) {
            if ( word[j] == '(' ) { otvr = true; continue; }
            if ( word[j] == ')' ) { br++; otvr = false; continue; }
            
            mark[br][ word[j]-'a' ] = true;
            if ( !otvr ) br++;
        }
        
        ret = 0;
        for (int j = 0; j < d; j++) {
            good = true;
            for (int k = 0; k < l; k++) {
              if ( !mark[k][ rec[j][k]-'a' ] ) good = false;
              if ( !good ) break;
            }
            
            if ( good ) ret++;
        }
        
        printf("Case #%d: %d\n",i+1,ret);
    }

    return 0;
}
