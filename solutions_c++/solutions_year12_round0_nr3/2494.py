#include <cstdio>
#include <set>

using namespace std;

int main (){

    int t,a,b,i,j,l,n,c;
    char ai[8], temp[8];
    set< pair<int,int> > d;

    scanf("%d\n",&n);

    for(c = 1; c <= n; c++){

        d.clear();
        scanf("%d %d\n",&a, &b);

        for(i = a; i <= b; i++){
            sprintf(ai, "%d", i);
            l = strlen(ai);
            for(j = 1; j < l; j++){
                strcpy(temp, &ai[j]);
                strncat(temp, ai, j);
                t = atoi(temp);
                if(a < t && t < b && t != i){
                    if(i < t)
                        d.insert(pair<int,int>(i,t));
                    else
                        d.insert(pair<int,int>(t,i));
                }

            }

        }

        printf("Case #%d: %d\n", c ,d.size());
    }
    return 0;
}

