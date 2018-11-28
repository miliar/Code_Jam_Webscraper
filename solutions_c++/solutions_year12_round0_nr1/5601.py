#include<iostream>
#include<string>

using namespace std;

int main()
{int t,count=1,i;
char arr[100];
     cin>>t;
     gets(arr);
    while(count<=t)
    {      
        gets(arr);
        for(i=0;i<strlen(arr);i++)
          { 
               switch(arr[i])
                {  case 'y': arr[i]='a';
                                 break;
                   case 'n': arr[i]='b';
                                 break;
                   case 'f': arr[i]='c';
                                 break;
                   case 'i': arr[i]='d';
                                 break;
                    case 'c': arr[i]='e';
                                  break;
                    case 'w': arr[i]='f';
                                 break;
                    case 'l': arr[i]='g';
                                 break; 
                    case 'b': arr[i]='h';
                                 break;  
                    case 'k': arr[i]='i';
                                 break;  
                    case 'u': arr[i]='j';
                                 break;
                    case 'o': arr[i]='k';
                                 break;
                    case 'm': arr[i]='l';
                                 break;
                  case 'x': arr[i]='m';
                                 break;        
                   case 's': arr[i]='n';
                                 break;  
                   case 'e': arr[i]='o';
                                 break;
                   case 'v': arr[i]='p';
                                 break;                  
                   case 'z': arr[i]='q';
                                 break;                
                   case 'p': arr[i]='r';
                                 break;                
                  case 'd': arr[i]='s';
                                 break;                 
                   case 'r': arr[i]='t';
                                 break;                
                   case 'j': arr[i]='u';
                                 break;                
                   case 'g': arr[i]='v';
                                 break; 
                   case 't': arr[i]='w';
                                 break;
                    case 'h': arr[i]='x';
                                 break;
                    case 'a': arr[i]='y';
                                 break;                                                                                                                                                                       
                   case 'q': arr[i]='z';
                                 break;
                                 }}
                      cout<<"Case #"<<count<<": ";
                      puts(arr);
           count++;
           }      

   return 0;
}                                               
