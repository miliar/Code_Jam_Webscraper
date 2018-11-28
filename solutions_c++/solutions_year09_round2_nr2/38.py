// Author: Adam Polak
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;
const int NIL = (-1);

#define REP(i,n) for(int i=0;i<(n);i++)
#define SIZE(c) ((int)((c).size()))

#define mp make_pair
#define st first
#define nd second
#define pb push_back

void scase(int case_num) {
    char s[30];
    scanf("%s",s);
    int n = strlen(s);
    printf("Case #%d: ",case_num);
    if (!next_permutation(s,s+n)) {
        sort(s,s+n);
        int fnz=0;
        while (s[fnz]=='0') fnz++;
        printf("%c0",s[fnz]);
        for(int i=0;i<fnz;i++) printf("%c",s[i]);
        for(int i=fnz+1;i<n;i++) printf("%c",s[i]);
        printf("\n");
    } else printf("%s\n",s);

}

int main() {
    int cases; 
    scanf("%d",&cases);
    //cin >> cases;
    REP(case_num,cases) scase(case_num+1);
    return 0;
}

    
