#include <iostream>
#include <cstdio>
#include <map>
#include <cstring>
using namespace std;
char ar[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("tounges.txt","w",stdout);
    int T;
    cin>>T;
    getchar();
    string str;
    for(int I=1;I<=T;I++){
        getline(cin,str);
        printf("Case #%d: ",I);
        int len = str.length();
        for(int i=0;i<len;i++){
            if ( str[i] == ' ')printf(" ");
            else printf("%c",ar[str[i]-'a']);  
        }
        printf("\n");
    }
return 0;
}
