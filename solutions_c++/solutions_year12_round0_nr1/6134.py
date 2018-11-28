#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t,l,i,j=0,x;
    
    
    char str[100];
    
     
    cin>>t; 
      t++;   
    while(t--)
    {
              j++;
              
        gets(str);
        l=strlen(str);
        for(i=0;i<l;i++)
        {
                        switch(str[i])
                        {
                                    case 'a': str[i]='y';break;
                                    case 'b': str[i]='h';break;
                                    case 'c': str[i]='e';break;
                                    case 'd': str[i]='s';break;
                                    case 'e': str[i]='o';break;
                                    case 'f': str[i]='c';break;
                                    case 'g': str[i]='v';break;
                                    case 'h': str[i]='x';break;
                                    case 'i': str[i]='d';break;
                                    case 'j': str[i]='u';break;
                                    case 'k': str[i]='i';break;
                                    case 'l': str[i]='g';break;
                                    case 'm': str[i]='l';break;
                                    case 'n': str[i]='b';break;
                                    case 'o': str[i]='k';break;
                                    case 'p': str[i]='r';break;
                                    case 'q': str[i]='z';break;
                                    case 'r': str[i]='t';break;
                                    case 's': str[i]='n';break;
                                    case 't': str[i]='w';break;
                                    case 'u': str[i]='j';break;
                                    case 'v': str[i]='p';break;
                                    case 'w': str[i]='f';break;
                                    case 'x': str[i]='m';break;
                                    case 'y': str[i]='a';break;
                                    case 'z': str[i]='q';break;
                        }
                                    
        }
        if(j>1)
        cout<<"Case #"<<j-1<<": "<<str<<"\n";
        
    }
}                         
