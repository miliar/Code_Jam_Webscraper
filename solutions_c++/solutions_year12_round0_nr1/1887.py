#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int main()
{
    freopen("x.in","r",stdin);
    freopen("x.out","w",stdout);
    char map[]="yhesocvxduiglbkrztnwjpfmaq";
    char str[120];
    int T;
    int len;
    int tmp;
    scanf("%d",&T);
    getchar();
    for(int i = 1;i<=T;i++){
        gets(str);
        len = strlen(str);

        for(int j = 0;j<len;j++){
            if(tmp = str[j]-'a' >=0)
                str[j] = map[str[j]-'a'];
        }
        cout<<"Case #"<<i<<": "<<str<<endl;
    }
    return 0;
}
