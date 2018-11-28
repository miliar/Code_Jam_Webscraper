#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
char f[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l',
            'b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);

    char s[1000];
    int T; cin >> T; getchar();
    for (int o = 1; o <= T; o++){
        printf("Case #%d: ", o);
        cin.getline(s,1000);
        for (int i = 0; i < strlen(s); i++)
            if (s[i] == ' ') cout << ' ';
            else cout << f[s[i] - 'a'];
        cout << endl;
    }
}
