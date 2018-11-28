#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
    string s;
    string arr="yhesocvxduiglbkrztnwjpfmaq";
    int test,m=1;
    cin>>test;
    getline(cin,s) ;
    while(test--)
    {
              
                 getline(cin,s);
                 printf("Case #%d: ",m++);
                 for(int i=0;i<s.length();i++)
                 {
                         if(s[i]==' ')
                         cout<<" ";
                         else
                         cout<<arr[s[i]-'a'];
                 }
                 cout<<endl;
                         
    }
    cin>>m;

return 0;
}
