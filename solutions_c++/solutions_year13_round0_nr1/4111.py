#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
char di();
char row();
char cul();
string x[4] ;

int main()
{
     freopen("input.txt","r",stdin) ;
     freopen("output.txt","w",stdout) ;
     int t ;
     char y , z , h  ;
     cin>>t ;
     bool f = false ;
     for(int i = 0 ; i<t ; i++){

           for(int k = 0 ; k<4 ; k++)cin>>x[k] ;
           y = di() ;
           z= row() ;
           h = cul() ;

           if(y=='x'||z=='x'||h=='x')cout<<"Case #"<<i+1<<": X won" <<endl ;
         else if(y=='o'||z=='o'||h=='o')cout<<"Case #"<<i+1<<": O won"<<endl ;
         else if(z=='s')cout<<"Case #"<<i+1<<": Game has not completed"<<endl ;
         else{
          cout<<"Case #"<<i+1<<": Draw"<<endl ;
         }




     }

    return 0;
}
char di(){
     int x2=0  , x1 = 0 , o1 = 0   , o= 0 ;
for(int i = 0 ; i<4 ; i++){
     if(x[i][i]=='T'||x[i][i]=='O')o++ ;
      if(x[i][i]=='T'||x[i][i]=='X')x2++ ;
     if(x[i][3-i]=='T'||x[i][3-i]=='O')o1++ ;
     if(x[i][3-i]=='T'||x[i][3-i]=='X')x1++ ;
}
if(x2==4||x1==4)return 'x'  ;
if(o==4||o1==4)return 'o' ;
return 't' ;
}
char row(){
     int o = 0 , x1 = 0 , s= 0  ;
for(int i = 0 ; i<4 ; i++){
     o = 0 ;
     x1 = 0 ;
     for(int k = 0 ; k<4 ; k++){
          if(x[i][k]=='X'||x[i][k]=='T')x1++  ;
          if(x[i][k]=='O'||x[i][k]=='T')o++ ;
          if(x[i][k]=='.')s++ ;

     }
     if(x1==4)return 'x' ;
     if(o==4)return 'o' ;
}
if(s>0)return 's' ;
return 't';

}
char cul(){
int o = 0 , x1 = 0 ;
for(int i = 0 ; i<4 ; i++){
     o = 0 ;
     x1= 0 ;
     for(int k = 0 ; k<4 ; k++){
          if(x[k][i]=='X'||x[k][i]=='T')x1++ ;
          if(x[k][i]=='O'||x[k][i]=='T')o++ ;
     }
     if(x1==4)return 'x' ;
     if(o==4)return 'o' ;
}
return 't';


}
