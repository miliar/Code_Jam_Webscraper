#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main(){
//    freopen("a.in","r",stdin);
//    freopen("a.out","w",stdout);
    int nc,cont = 0,n;
    scanf("%d\n",&nc);
    string cad;
    char c[150];
    char arr[30] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    while(nc--){
      cont++;
      cad = "";
      gets(c);
      n = strlen(c);
      for(int i=0;i<n;i++){
        if(c[i] == ' ') cad += " ";
        else cad += arr[c[i]-'a'];
        }
      cout<<"Case #"<<cont<<":"<<" "<<cad<<endl;
      }
    //system("pause");
    }



