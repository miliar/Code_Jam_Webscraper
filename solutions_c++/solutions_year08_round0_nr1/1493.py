#include<stdio.h>
#include<string.h>
#include<string>

using namespace std;

string s[200];
string q[2000];
char line[1000];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int n;
    scanf("%d",&n);
    int kase=1;
    while ( n--) {
          int snum,qnum;
          scanf("%d",&snum);

          gets(line);
          int i;
          for(i=0;i<snum;i++) gets(line), s[i] = line;
          scanf("%d",&qnum);
          gets(line);
          for(i=0;i<qnum;i++) gets(line), q[i] = line;
          int laststop = 0;
          int swit = 0;
          while ( laststop != qnum ) {
                int j;
                int maxcover=0;
                int maxindex;
                for (i=0;i<snum;i++) {
                    for(j=laststop;j<qnum;j++)
                     if ( q[j] == s[i] ) break;
                    if ( j-laststop > maxcover )
                       maxcover = j-laststop, maxindex=j; 
                }
                laststop=maxindex;
                if ( laststop < qnum ) swit++;
          }
     printf("Case #%d: %d\n",kase++,swit);
    }
    return 0;
}
