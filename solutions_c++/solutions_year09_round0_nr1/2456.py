#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

char Dic[10000][20];
char Src[10240];
char Pat[10][256];

int main(int arg, char *argv)
{
    int l, d, n;
    
    scanf("%d %d %d", &l, &d, &n);
    for(int i=0; i<d; ++i) {
        scanf("%s", Dic[i]);
    }
    
    for(int i=1; i<=n; ++i) {   
        scanf("%s", Src);        
        char *p=Src;
        for(int j=0; j<l; ++j) {
            if(*p=='(') {
                ++p;
                char *e=strchr(p, ')');
                assert(NULL!=e);
                strncpy(Pat[j], p, e-p);
                Pat[j][e-p]='\0';
                p=e+1;
            }
            else if(*p!='\0') {
                Pat[j][0]=*p;
                Pat[j][1]='\0';
                ++p;
            }
            else
                assert(0);
        }
        
        int m=0;
        for(int j=0; j<d; ++j) {
            int match=1;
            for(int k=0; k<l; ++k) {
                if(Pat[k][1]=='\0') {
                    if(Pat[k][0]==Dic[j][k])
                        continue;
                }     
                else if(strchr(Pat[k], Dic[j][k]))
                    continue;
                match=0;
                break;        
            }
            if(match) ++m;
        }
    
        printf("Case #%d: %d\n", i, m);
    }

    return 0;    
}

