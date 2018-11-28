#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t,l,i,j=0,x;
    
    
    char a[100];
    
    
    
    cin>>t; t++;   
    while(t--)
    {
              j++;
              
        gets(a);
        l=strlen(a);
        for(i=0;i<l;i++)
        {
                        switch(a[i])
                        {
                                    case 'a': a[i]='y';break;
                                    case 'b': a[i]='h';break;
                                    case 'c': a[i]='e';break;
                                    case 'd': a[i]='s';break;
                                    case 'e': a[i]='o';break;
                                    case 'f': a[i]='c';break;
                                    case 'g': a[i]='v';break;
                                    case 'h': a[i]='x';break;
                                    case 'i': a[i]='d';break;
                                    case 'j': a[i]='u';break;
                                    case 'k': a[i]='i';break;
                                    case 'l': a[i]='g';break;
                                    case 'm': a[i]='l';break;
                                    case 'n': a[i]='b';break;
                                    case 'o': a[i]='k';break;
                                    case 'p': a[i]='r';break;
                                    case 'q': a[i]='z';break;
                                    case 'r': a[i]='t';break;
                                    case 's': a[i]='n';break;
                                    case 't': a[i]='w';break;
                                    case 'u': a[i]='j';break;
                                    case 'v': a[i]='p';break;
                                    case 'w': a[i]='f';break;
                                    case 'x': a[i]='m';break;
                                    case 'y': a[i]='a';break;
                                    case 'z': a[i]='q';break;
                        }
                                    
        }
        if(j>1)
        cout<<"Case #"<<j-1<<": "<<a<<"\n";
        
    }
}                         
