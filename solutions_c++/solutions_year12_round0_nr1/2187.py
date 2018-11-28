#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args);

typedef long long lint;
typedef pair<int,int> pii;

const int INF = 0x3f3f3f3f;
char m[][30] = {"yhesocvxduiglbkrqtnwjpfmaz","yhesocvxduiglbkrztnwjpfmaq"};
char text[2][1000];

int main() {
    FILE *f1,*f2;
    f1 = fopen("out1.txt","w");
    f2 = fopen("out2.txt","w");
    int T;
    scanf("%d ",&T);
    for(int t=1;t<=T;++t) {
        fprintf(f1,"Case #%d: ",t);
        fprintf(f2,"Case #%d: ",t);
        gets(text[0]);
        strcpy(text[1],text[0]);
        int len = strlen(text[0]);
        for(int a=0;a<len;++a) 
            if(isalpha(text[0][a])) {
                text[0][a] = m[0][text[0][a]-'a'];
                text[1][a] = m[1][text[1][a]-'a'];
            }
        fprintf(f1,"%s\n",text[0]);
        fprintf(f2,"%s\n",text[1]);
    }
    return 0;
}
