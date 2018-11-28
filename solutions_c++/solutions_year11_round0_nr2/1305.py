#include <cstdio>
using namespace std;

int c,d;
char cc[50][4];
char dd[50][4];

int main() {
    int Z; scanf("%d",&Z);
    for(int z=1;z<=Z;z++) {
        scanf("%d",&c);
        for(int i=0;i<c;i++) scanf("%s",cc[i]);
        scanf("%d",&d);
        for(int i=0;i<d;i++) scanf("%s",dd[i]);
        int l,n=0;
        char w[200], s[200];
        scanf("%d%s",&l,w);
        for(int i=0;i<l;i++) {
            s[n++] = w[i];
            while(n>=2) {
                int found = (-1);
                for(int j=0;j<c;j++) {
                    if (s[n-1]==cc[j][0] && s[n-2]==cc[j][1]) 
                        found = j;
                    if (s[n-1]==cc[j][1] && s[n-2]==cc[j][0]) 
                        found = j;
                }
                if (found<0) break;
                n--;
                s[n-1] = cc[found][2];
            }
            for(int j=0;j<d;j++) 
                for(int x=0;x<n;x++)
                    for(int y=0;y<n;y++)
                        if (dd[j][0]==s[x] && dd[j][1]==s[y]) n=0;
        }
        printf("Case #%d: [",z);
        for(int i=0;i<n;i++) {
            if (i>0) printf(", ");
            printf("%c",s[i]);
        }
        printf("]\n");
    }
    return 0;
}
                       

