#include<iostream>
#include<cstdio>


using namespace std;

int main(){
    int n;
    scanf("%d", &n);
    char c;
    scanf("%c", &c);
    string data;
    string dic = "yhesocvxduiglbkrztnwjpfmaq";
    for(int i=0;i<n;i++){
        cout<<"Case #"<<i+1<<": ";
        while(~scanf("%c", &c))
        {
            if(c=='\n') break;
            if(c>=97) printf("%c", dic.at(c-97));
            else printf("%c", c);
        }
        cout<<endl;
    }
    return 0;
}
