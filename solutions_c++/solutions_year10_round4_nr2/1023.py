#include <iostream>
#include <map>
using namespace std;

#define MaxN 100
#define MaxLen 105
#define MaxM 100

map<string,int> ma;
int n,m;
char s[MaxLen];

class Trie {
      
   public:   
   string val;
   Trie *list[MaxN];
   int l;
   
   void Delete() {
        for (int i = 0; i < l; i++) {
           (*list[i]).Delete();
           delete( list[i] );
        }
        l = 0;
   };
   
   void Add( int ps, char se[MaxLen] ) {
        if ( ps >= strlen(se) ) return;
        
        string s = "";
        while ( (ps < strlen(se)) && ( (se[ps] >= '0' && se[ps] <= '9') || (se[ps] >= 'a' && se[ps] <= 'z') ) )
              s += se[ps++];
        
        for (int i = 0; i < l; i++) {
            if ( (*list[i]).val == s ) {
               list[i]->Add( ps+1, se );
               return;
            }
        }
        
        list[l++] = new(Trie);
        (*list[l-1]).val = s;
        (*list[l-1]).l = 0;
        (*list[l-1]).Add( ps+1, se );
   };
   
   int Find( int ps, char se[MaxLen] ) {
       if ( ps >= strlen(se) ) return 0;
       
       string s = "";
       while ( (ps < strlen(se)) && ( (se[ps] >= '0' && se[ps] <= '9') || (se[ps] >= 'a' && se[ps] <= 'z') ) ) {
             s += se[ps++];
       }
             
       for (int i = 0; i < l; i++) {
           if ( (*list[i]).val == s ) {
              return list[i]->Find( ps+1, se );
           }
       }
       
       int ret = 1;
       while ( ps < strlen(se) ) {
             if ( se[ps] == '/' ) ret++;
             ps++;
       }
       
       return ret;
   };
      
};

Trie *p;

int main()
{
    
    freopen("google.in","r",stdin);
    freopen("google.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    
    p = new(Trie);
    p->l = 0;
    
    for (int t = 0; t < T; t++) {
    
        (*p).Delete();
        
        scanf("%d%d",&n,&m);
        
        for (int i = 0; i < n; i++) {
            scanf("%s",s);
            p->Add(1,s);
        }
        
        int ret = 0;
        for (int j = 0; j < m; j++) {
            scanf("%s",s);
            ret += p->Find(1,s);
            p->Add(1,s);
        }
        
        printf("Case #%d: %d\n",t+1,ret);
        
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
    
}
