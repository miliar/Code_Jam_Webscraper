#include<iostream>
#include<string>
#include<string.h>
#include<stdio.h>
using namespace std;


char change(char c)
{ 
 if(c=='y')return 'a';  
 if(c=='n')return 'b'; 
 if(c=='f')return 'c';
 if(c=='i')return 'd';  
 if(c=='c')return 'e'; 
 if(c=='w')return 'f';  
 if(c=='l')return 'g'; 
 if(c=='b')return 'h';  
 if(c=='k')return 'i'; 
 if(c=='u')return 'j'; 
 if(c=='o')return 'k'; 
 if(c=='m')return 'l'; 
 if(c=='x')return 'm';   
 if(c=='s')return 'n';
 if(c=='e')return 'o';   
 if(c=='v')return 'p';   
 if(c=='p')return 'r';  
 if(c=='d')return 's'; 
 if(c=='r')return 't'; 
 if(c=='j')return 'u'; 
 if(c=='g')return 'v'; 
 if(c=='t')return 'w';
 if(c=='h')return 'x'; 
 if(c=='a')return 'y';
 if(c=='q')return 'z';
 if(c=='z')return 'q';
      
     
}

int main(){
    int T,i;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("tt.out","w",stdout);
    cin>>T;
    char k[200];
     cin.getline(k,200);
    for(int cas = 1;cas<=T;cas++)
    {
     cin.getline(k,200);
     int n = strlen(k);
     for(i=0;i<n;i++)
     if(isalpha(k[i]))k[i]=change(k[i]); 
     cout<<"Case #"<<cas<<": "<<k<<endl;        
    }
    
    
    
    return 0;    
}
