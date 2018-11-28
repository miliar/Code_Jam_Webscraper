/* A. Speaking in Tongues [filename: A.cpp]

           Codejam :: Qualification Round 2012
          ---------------------------------------------

                      Written in C++ Programming
       Tested and Compiled - Microsoft Windows 7 / Dev-C++ v4.9

*/

/******************************************************
           WRITTEN BY K21G [K-piXjuv-G]
           
         [ nepal.mountpk@msdnnepal.net ]
               [ puncoz@live.com ]
       [ http://www.facebook.com/puncoz ]
*******************************************************/

#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

char convert(char);

int main()
 {
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  
  int T;
  cin>>T;
  
  int len = T+1;
  //string sI[len],sO[len];
  
  for(int i=0; i<=T; i++)
   {
    string sI,sO;
    getline(cin,sI);
    
    if(i == 0)
     continue;
    
    int lenS = sI.length();
    
    cout<<"Case #"<<i<<": ";
    for(int j=0; j<lenS; j++)
     {
      char chI = sI[j];
      char chO;
      
      if(chI == 32)
       cout<<" ";
      else
       {
        chO = convert(chI);
        cout<<chO;
       }    
      //sO.insert(j,&chO);   
     } 
    cout<<endl;
   }
      
  return 0;    
 }
 
char convert(char ch)
 {
  char chr;
  switch(ch)
   {
    case 'a': chr = 'y'; break;
    case 'b': chr = 'h'; break;
    case 'c': chr = 'e'; break;
    case 'd': chr = 's'; break;
    case 'e': chr = 'o'; break;
    case 'f': chr = 'c'; break;
    case 'g': chr = 'v'; break;
    case 'h': chr = 'x'; break;
    case 'i': chr = 'd'; break;
    case 'j': chr = 'u'; break;
    case 'k': chr = 'i'; break;
    case 'l': chr = 'g'; break;
    case 'm': chr = 'l'; break;
    case 'n': chr = 'b'; break;
    case 'o': chr = 'k'; break;
    case 'p': chr = 'r'; break;
    case 'q': chr = 'z'; break;
    case 'r': chr = 't'; break;
    case 's': chr = 'n'; break;
    case 't': chr = 'w'; break;
    case 'u': chr = 'j'; break;
    case 'v': chr = 'p'; break;
    case 'w': chr = 'f'; break;
    case 'x': chr = 'm'; break;
    case 'y': chr = 'a'; break;
    case 'z': chr = 'q'; break; 
    default: chr = '?'; break;   
   }   
   
  return chr;   
 }
