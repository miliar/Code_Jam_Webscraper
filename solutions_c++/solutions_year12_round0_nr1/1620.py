
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define SMALL
//#define LARGE
int main() {
#ifdef SMALL
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w+",stdout);
#endif
#ifdef LARGE
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w+",stdout);
#endif
    
    string code = "yhesocvxduiglbkrztnwjpfmaq";

    int n;
    cin>>n;
    for(int i=0;i<=n;++i) {
        string s,s1;
        getline(cin,s);
        for(int j=0;j<s.length();++j) {
            if(s[j]==' ')
                s1+=string(" ");
            else {
                char c=s[j];
                int x=c;
                s1+=code[x-97];
            }
        }
        if(i==0)
            continue;
        else {
            printf("Case #%d: ",i);
            cout<<s1<<endl;
        }
    }
    return 0;
}
