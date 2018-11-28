#include <iostream>
#include <stdio.h>
#include <map>
#include <sstream>

using namespace std ;

int FormNumber(string s,int j) 
{
    int ctr = 0 ;
    int n = 0 ;
    int size = s.size() ;
    while(ctr < s.size()){
              n = n*10 + (s[j%size]-48) ;
              j++ ;
              ctr++ ;
    }
    return n ; 
}

int main()
{
    int t ;
    scanf("%d",&t) ;
    int ctr = 1 ;
    while(t--){
               int a,b ;
               scanf("%d%d",&a,&b) ;
               map<int,int> mp ;
               int ans =  0 ;
               for(int i = a;i <= b;i++){
                       stringstream ss ;
                       string s ;
                       ss << i ;
                       ss >> s ;
                       mp[i] = 1 ;
                       int temp =  1 ;
                       for(int j=0;j < s.size();j++){
                               if(s[j] != '0') {
                               int n = FormNumber(s,j) ;
                               if(!mp[n]){
                                         if(n <= b && n >= a){
                                              mp[n] = 1 ;
                                              temp++ ;
                                         } 
                               }
                               }
                       }
                       ans += temp*(temp-1)/2 ;                                                                                                                 
               }
               cout << "Case #" << ctr++ << ": " <<  ans << endl ;
    }
    //system("pause") ;
    return 0 ;
}                       
               
