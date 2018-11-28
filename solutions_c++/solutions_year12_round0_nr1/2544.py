/*#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define maxn 101

char s[maxn],t[maxn],m[30];

int main()
{
    freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int c;
    scanf("%d",&c);
    getchar();
    while(c--){
        gets(s);
        gets(t);
        cout << s << endl << t << endl;
        for(int i=0;s[i];i++){
            if(islower(s[i])){
                m[s[i]-'a'] = t[i];
                //cout << s[i]-'a' << ' ' << s[i] << ' ' << t[i] << endl;
            }
        }
        //cout << endl;
        //for(int i=0;i<30;i++)printf("%c ",m[i]);
        //puts("");
    }
    for(int i=0;i<30;i++)printf("'%c',",m[i]);
    return 0;
}
*/



#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

char m[30] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',};
char s[101],t[101];

int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small-attempt4.out","w",stdout);
    int c;
    scanf("%d",&c);
    getchar();
    for(int ca=1;ca<=c;ca++){
        gets(s);
        int i;
        for(i=0;s[i];i++){
            if(islower(s[i])){
                t[i] = m[s[i]-'a'];
            }
            else t[i] = s[i];
        }
        t[i] = 0;
        printf("Case #%d: %s\n",ca,t);
    }
    return 0;
}
