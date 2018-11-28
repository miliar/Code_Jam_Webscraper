#include<cstdio>
#include<cstdlib>
#include<iostream>
using namespace std;
int main(){

    char mapping[30] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t;
    cin >> t;
    string goo;
    getline(cin,goo);
    for (int i =1; i <=t;i++) {

        getline(cin, goo);
        printf("Case #%d: ", i);
        for(int j = 0 ; j< goo.size();j ++ ) {
            if(goo[j]>='a' && goo[j]<='z')
                printf("%c", mapping[goo[j]-'a']);
            else 
                printf("%c",goo[j]);
        }
        printf("\n");
    }
    
}
