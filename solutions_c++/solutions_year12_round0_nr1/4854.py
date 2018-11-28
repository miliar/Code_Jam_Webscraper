/* 
 * File:   main_gcj.cpp
 * Author: vijay
 *
 * Created on 7 May, 2011, 5:50 PM
 */
#include<sstream>
#include <cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;
char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
void convert(void);
/*
 * 
 */
int main() {
freopen("a.in", "r", stdin); 
freopen("a.out", "w", stdout); 
//cout<<"no outpu   t";
int T,i=1;
cin>>T;
//cout<<T<<"value T";
convert();
while(T>0){
    cout<<"Case #"<<i<<": ";
    convert();
    cout<<endl;
    i++;
    T--;
}
return 0;
}

void convert(void){
//    char test;
//    cin>>test;
    //cout<<test;
    char inputstr[101];
     cin.getline(inputstr,101);
     for(int i=0;inputstr[i]!='\0';i++)
        { if(inputstr[i]!=' ')  
          {cout << map[inputstr[i]-'a'];}
          else
           cout<<' ';
        }
//    while(test!='\0' || test!='\n'){
//        if(test==' ') cout<<" ";
//        else cout<<map[test-'a'];
//        cin>>test;
//    }
    
}
