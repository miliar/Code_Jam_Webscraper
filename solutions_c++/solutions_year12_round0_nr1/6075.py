#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

char map[26] = {'y', 'h' ,'e','s','o','c','v','x','d','u','i','g','l','b','k','r', 'z','t','n','w','j','p','f','m','a','q'};
char in[105];

int main(){
        int t;
        scanf("%d", &t);
        for(int a=1; a<=t; a++){
                getchar();
                scanf("%[^\n]", in);
                printf("Case #%d: ", a);
                for(int i=0; in[i]!='\0'; i++){
                        if(in[i] == ' ')
                                printf(" ");
                        else
                                printf("%c", map[in[i]-'a']);
                }
                printf("\n");
        }
        return 0;
}
