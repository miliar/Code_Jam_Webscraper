
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int C,n,x,y,xt,yt,ret,pos;
char s[5];

int main(){

        scanf("%d",&C);
        for (int tc=1; tc<=C; tc++){

                scanf("%d", &n);
                x = y = 1;
                xt = yt = 0;
                ret = 0;

                while (n--){
                        scanf("%s%d", s, &pos);
                        if (s[0]=='O'){
                                xt += abs(x-pos) + 1;
                                if (xt <= yt) xt = yt + 1;
                                x = pos;
                                ret = xt;
                        }
                        if (s[0]=='B'){
                                yt += abs(y-pos) + 1;
                                if (yt <= xt) yt = xt + 1;
                                y = pos;
                                ret = yt;
                        }
                }

                printf("Case #%d: %d\n", tc, ret);

        }

        return 0;
}
