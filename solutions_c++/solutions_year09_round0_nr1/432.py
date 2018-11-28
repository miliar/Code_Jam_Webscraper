#include <iostream>
using namespace std;
char words[10000][20];
char next[10000];
int main() {
    int L,D,N; scanf("%d %d %d",&L,&D,&N);
    for (int i=0; i<D; i++) scanf("%s",words[i]);
    for (int i=0; i<N; i++) {
        scanf("%s",next);
        int ans = 0;
        for (int word=0; word<D; word++) {
            int pos = 0;
            int upto = 0;
            while (upto<L) {
                if (next[pos]=='(') {
                    bool found = false;
                    pos++;
                    while (next[pos]!=')') {
                        if (next[pos]==words[word][upto]) {
                            found=true;
                        }
                        pos++;
                    }
                    if (!found) goto nope;
                    pos++;
                } else {
                    if (next[pos]!=words[word][upto]) goto nope;
                    pos++;
                }
                upto++;
            }
            ans++;
            nope:;            
        }

        printf("Case #%d: %d\n",i+1,ans);        
    }
}
