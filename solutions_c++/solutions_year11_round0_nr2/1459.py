#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < (int )b ; i++)

#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

#define LL long long
#define ULL unsigned long long
#define UI unsigned int

#define VI vector<int>
#define VS vector<string>

#define pb push_back

struct combine {
    char a,b,c;
};

struct opposed {
    char a,b;
};

int main() {
    int tc,c,d,n;
    scanf("%d",&tc);
    FOR(i,1,tc+1) {
        struct combine a[100];
        struct opposed b[100];
        char ch;
        vector <char> str;
        cin>>c;
        FOR(j,0,c) {
            scanf("%*c%c%c%c",&a[j].a,&a[j].b,&a[j].c);
        }
        cin>>d;
        FOR(j,0,d) {
            scanf("%*c%c%c",&b[j].a,&b[j].b);
        }
        cin>>n;
        scanf("%*c%c",&ch);
        str.pb(ch);
        bool check = true;
        FOR(j,1,n) {
            scanf("%c",&ch);
            str.pb(ch);
            check = true;
            char s1 = str[str.size()-2];
            FOR(x,0,c) {
                if((a[x].a == s1 && a[x].b == ch) || (a[x].a == ch && a[x].b == s1)) {
                    str.pop_back();
                    str.pop_back();
                    str.pb(a[x].c);
                    check = false;
                    break;
                }
            }
            FOR(k,0,str.size()-1) {
                if(check) {
                    FOR(x,0,d) {
                        if((b[x].a == str[k] && b[x].b == ch) || (b[x].a == ch && b[x].b == str[k])) {
                            str.resize(0);
                            j++;
                            if(j<n) {
                                scanf("%c",&ch);
                                str.pb(ch);
                            }
                            check = false;
                            break;
                        }
                    }
                    if(!check) break;
                }
            }
        }
        printf("Case #%d: [",i);
        FOR(j,0,str.size()-1) {
            printf("%c, ",str[j]);
        }
        if(str.size() > 0) {
            printf("%c",str[str.size()-1]);
        }
        printf("]\n");
    }
    return (0);
}
