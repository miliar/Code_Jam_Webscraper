#include <iostream>
#include <stdio.h>

using namespace std ;

int main()
{
    char T[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'} ;
    int t ;
    scanf("%d",&t) ;
    string s ;
    getline(cin,s) ;
    int ctr = 1 ;
    while(t--) {
               getline(cin,s) ;
               string temp = "" ;
               for(int i=0;i < s.size();i++)
                       if(s[i] != ' ')
                               temp += T[s[i]-'a'] ;
                       else
                           temp += ' ' ;
               cout << "Case #" << ctr++ << ": " << temp << endl ;
    }
    //system("pause") ;
    return 0 ;
}
