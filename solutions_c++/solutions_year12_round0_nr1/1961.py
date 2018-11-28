#include<iostream>
#include<cstdio>
using namespace std;

char s[100];

char a[26] = {'y' ,'h','e','s','o','c','v','x','d','u','i','g','l','b','k',
             'r','z','t','n','w','j','p','f','m','a','q'};

void output(int count){
     for(int k = 0 ; k<count ; k++ )
      {       
              if(s[k] == ' ')
              cout<<" ";
              else
              cout<<a[s[k]-97];
      }
      cout<<"\n";
}

int main(){
    int n ;
    cin>>n;
    int i = 1;
    int count ;
    getchar();
    while(i<=n){
               fflush(stdin);
               count = 0;
               char c = getchar();
               while(c!='\n'){
                              s[count++] = c;
                              c = getchar();
               }
               cout<<"Case #"<<i<<": ";
               output(count);
               i++;
    }
    return 0;
}
