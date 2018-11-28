#include<cstring>
#include<iostream>
#include<cstdio>
using namespace std;
char a[30];
int cor[30];
string c="yhesocvxduiglbkrztnwjpfmaq";
int main(){

    int i,j,n;
   // freopen("A-small-attempt0.in","r",stdin);
   // freopen("out.txt","w",stdout);
    cin>>n;
    getchar();
    for(j=1;j<=n;j++){
        cout<<"Case #"<<j<<": ";
        gets(a);
        string d;
        for(i=0;i<strlen(a);i++)
            if(a[i]==' ') d+=' ';
            else d+=c[a[i]-'a'];
        cout<<d<<endl;
    }

}
