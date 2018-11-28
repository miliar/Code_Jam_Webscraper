#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
char abc[100]={"yhesocvxduiglbkrztnwjpfmaq"},str[105];
int main(){
   freopen ( "A-small-attempt2.in", "r", stdin );
   freopen ( "gift1.out", "w", stdout );
    int cas,i,j,len,t=0;
    scanf("%d",&cas);
    getchar();
    while(cas--){
        t++;
        gets(str);
        //cin.getline(str,101);
        len=strlen(str);
        for(i=0;i<len;i++){
            if(str[i]!=' '){
                str[i]=abc[str[i]-'a'];
            }
        }
        cout<<"Case #"<<t<<": ";
        cout<<str<<endl;
    }
    return 0;
}
