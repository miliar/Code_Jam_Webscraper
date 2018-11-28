#include<cstdio>
#include<map>
#include<cstring>

using namespace std;

int T,C,D,N;

int main() {
    scanf("%d",&T);
    for(int t=0;t<T;t++) {
        map< char , map<char,char> > combine;
        map<char,char> oppose;
        char str[1000];

        /* input combines */
        scanf("%d",&C);
        for(int i=0;i<C;i++) {
            char cstr[4];
            scanf("%s",cstr);
            combine[cstr[0]][cstr[1]] = cstr[2];
            combine[cstr[1]][cstr[0]] = cstr[2];
        }

        /* input opposes */
        scanf("%d",&D);
        for(int i=0;i<D;i++) {
            char cstr[2];
            scanf("%s",cstr);
            oppose[cstr[0]] = cstr[1];
            oppose[cstr[1]] = cstr[0];
        }

        scanf("%d",&N);
        scanf("%s",str);

        char stack[1000];
        int stackend=0;
        for(int i=0;i<N;i++) {
            stack[stackend++] = str[i];
            if(stackend > 1)
                if(combine[stack[stackend-1]].count(stack[stackend-2])) {
                    stack[stackend-2] = combine[stack[stackend-1]][stack[stackend-2]];
                    stackend--;
                }
            stack[stackend]=0;
            if(oppose.count(stack[stackend-1])
                    && strchr(stack,oppose[stack[stackend-1]]))
                stackend=0;
        }

        printf("Case #%d: [",t+1);
        for(int i=0;i<stackend;i++)
            printf("%s%c",(i?", ":""),stack[i]);
        printf("]\n");
    }
    return 0;
}
