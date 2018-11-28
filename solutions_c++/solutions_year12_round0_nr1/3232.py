#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <utility>
#include <climits>
#include <cfloat>

using namespace std;
#define readint(n) scanf("%d",&n);
#define readf(n) scanf("%f",&n);
#define readd(n) scanf("%lf",&n);
#define readstr(s) scanf("%s",&s);
int pabs(int n){return (n>0?n:-n);}

int main(){
    char maps[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t;
    readint(t);
    string str;
    getline(cin,str);
    for(int ii=1;ii<=t;ii++){
        getline(cin,str);
        int maxi=str.length();
        printf("Case #%d: ",ii);
        for(int i=0;i<maxi;i++){
            if(str[i]==' '){
                printf(" ");
                continue;
            }
            printf("%c",maps[str[i]-'a']);
        }
        printf("\n");
    }
    return 0;
}
