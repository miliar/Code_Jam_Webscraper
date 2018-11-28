#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

char t[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char tmp[200];

int main(int argc, char** argv) {
    int T,cas=1;
    scanf("%d",&T);
    getchar();
    while(cas<=T){
        gets(tmp);
        for(int i=0;tmp[i];i++){
            if(tmp[i]>='a'&&tmp[i]<='z') tmp[i]=t[tmp[i]-'a'];
        }
        printf("Case #%d: %s\n",cas,tmp);
        cas++;
    }
    return 0;
}

