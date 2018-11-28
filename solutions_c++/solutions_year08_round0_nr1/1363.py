#include <cstdio>
#include <set>
#include <string>
using namespace std;


void endline() {
    char tmpch;
    do { scanf("%c", &tmpch); } while (tmpch!='\n');
}


int main() {
    char tmpbuf[128];
    
    int N; scanf("%d", &N); endline();
    
    for (int tc=0; tc<N; tc++) {
    
        int S; scanf("%d", &S); endline();
        
        set<string> SEN;

        while (S-->0) {
            scanf("%[^\n]", tmpbuf); endline();
            SEN.insert(tmpbuf);
        }
        
        int Q; scanf("%d", &Q); endline();
        set<string> SEN2=SEN;
        int result=0;
        
        while (Q-->0) {
            scanf("%[^\n]", tmpbuf); endline();
            if (SEN2.count(tmpbuf)>0) SEN2.erase(tmpbuf);
            if (SEN2.empty()) {
                result++;
                SEN2=SEN;
                if (SEN2.count(tmpbuf)>0) SEN2.erase(tmpbuf);
            }
        }
        
        printf("Case #%d: %d\n", tc+1, result);
    }
    
    return 0;
}
