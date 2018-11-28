#include<iostream>
#include<cstdio>
#include<string>
#include<conio.h>

using namespace std;

#define min(a,b) (a<b?a:b)
#define max(a,b) (a<b?b:a)
#define Size(x) (int)x.size()
#define FORI(i,n) for(int i = 0; i < n; i++)
#define FORB(i,be,en) for(int i = be; i <= en; i++)

int T,r,c;
char a[52][52];

int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    FORI(t,T) {
        printf("Case #%d:\n",t+1);
        scanf("%d%d",&r,&c);
        cin.ignore();
        FORI(i,r) {
            FORI(j,c) {
                scanf("%c",&a[i][j]);
            }
            cin.ignore();
        }
        FORI(i,r) FORI(j,c) if (a[i][j] == '#' && a[i+1][j] == '#'
             && a[i][j+1] == '#' && a[i+1][j+1] == '#') {
                    a[i][j] = '/'; a[i+1][j] = '\\';
                    a[i][j+1] = '\\'; a[i+1][j+1] = '/';
        }
        bool flag = 1;
        FORI(i,r) {
            FORI(j,c)
                if (a[i][j] == '#') {
                    flag = 0;
                    break;
                }
            if (!flag) break;
            }
        if (flag) {
            FORI(i,r) {
                FORI(j,c) printf("%c",a[i][j]);
                if (i < r-1) printf("\n");
            }
        }
        else printf("Impossible");
        if (t < T-1) printf("\n");
    }
    fclose(stdin);
    return 0;
}
