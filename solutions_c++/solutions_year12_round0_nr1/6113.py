#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std ;

int main()
{

int t,i,k ; 
string st ;
cin >> t ; char st1[2];

cin.getline(st1,99);
for ( k = 0 ; k < t  ; k++ )
{


getline(cin,st);
cout << "Case #" << k+1 << ": " ;

for(i=0; st[i]; i++ )

{
switch (st[i])
{
case 'a' :
cout << 'y' ; break ;

case 'b' :
cout << 'h' ; break ;

case 'c' :
cout << 'e' ; break ;

case 'd' :
cout << 's' ; break ;

case 'e' :
cout << 'o' ; break ;

case 'f' :
cout << 'c' ; break ;

case 'g' :
cout << 'v' ; break ;

case 'h' :
cout << 'x' ; break ;

case 'i' :
cout << 'd' ; break ;

case 'j' :
cout << 'u' ; break ;

case 'k' :
cout << 'i' ; break ;

case 'l' :
cout << 'g' ; break ;

case 'm' :
cout << 'l' ; break ;

case 'n' :
cout << 'b' ; break ;

case 'o' :
cout << 'k' ; break ;

case 'p' :
cout << 'r' ; break ;

case 'q' :
cout << 'z' ; break ;

case 'r' :
cout << 't' ; break ;

case 's' :
cout << 'n' ; break ;

case 't' :
cout << 'w' ; break ;

case 'u' :
cout << 'j' ; break ;

case 'v' :
cout << 'p' ; break ;

case 'w' :
cout << 'f' ; break ;

case 'x' :
cout << 'm' ; break ;

case 'y' :
cout << 'a' ; break ;

case 'z' :
cout << 'q' ; break ;

case ' ' :
cout << ' ' ; break ;

default:
cout << st[i] ;
break;


}


}

cout << '\n' ;

}



}


