#include<iostream>
#include<cstdio>
#include<string>


using namespace std;

int main(){
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("out.txt","wt",stdout);
	string str;
	int t;
	cin>>t;
/*
	"ynficwlbkuomxsevzpdrjgthaq"
	"abcdefghijklmnopqrstuvwxyz"
*/
	getline(cin,str);
     for(int i=0;i<t;i++){
         getline(cin,str);
         for(int j=0;j<str.length();j++){
        	 switch(str[j]){
        	     case 'y' : { str[j]='a'; break;}
        	     case 'n' : { str[j]='b'; break;}
        	     case 'f' : { str[j]='c'; break;}
        	     case 'i' : { str[j]='d'; break;}
        	     case 'c' : { str[j]='e'; break;}
        	     case 'w' : { str[j]='f'; break;}
        	     case 'l' : { str[j]='g'; break;}
        	     case 'b' : { str[j]='h'; break;}
        	     case 'k' : { str[j]='i'; break;}
        	     case 'u' : { str[j]='j'; break;}
        	     case 'o' : { str[j]='k'; break;}
        	     case 'm' : { str[j]='l'; break;}
        	     case 'x' : { str[j]='m'; break;}
        	     case 's' : { str[j]='n'; break;}
        	     case 'e' : { str[j]='o'; break;}
        	     case 'v' : { str[j]='p'; break;}
        	     case 'z' : { str[j]='q'; break;}
        	     case 'p' : { str[j]='r'; break;}
        	     case 'd' : { str[j]='s'; break;}
        	     case 'r' : { str[j]='t'; break;}
        	     case 'j' : { str[j]='u'; break;}
        	     case 'g' : { str[j]='v'; break;}
        	     case 't' : { str[j]='w'; break;}
        	     case 'h' : { str[j]='x'; break;}
        	     case 'a' : { str[j]='y'; break;}
        	     case 'q' : { str[j]='z'; break;}
        	 }
         }
	     cout<<"Case #"<<i+1<<": "<<str<<endl;
     }
	return 0;
}
