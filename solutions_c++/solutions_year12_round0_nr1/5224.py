#include<stdio.h>
#include<string.h>
#include<iostream>
#include<string>
using namespace std;
//typedef char string[100];

int main()
{
    int i,j,t,count;
    string S[1000];
    
    scanf("%d",&t);
    fflush(stdin);
    //gets(S[0]);
	getline(cin,S[i]);
    for(i=0;i<t;i++)
    {
                    //gets(S[i]);
			//cin.getline(S[i],100);
		getline(cin,S[i]);
                    count=S[i].size();
                    for(j=0;j<count;j++)
                    {
                                        switch(S[i][j])
                                        {
                                                    case 'a': S[i][j]='y'; break;
                                                    case 'b': S[i][j]='h'; break;
                                                    case 'c': S[i][j]='e'; break;
                                                    case 'd': S[i][j]='s'; break;
                                                    case 'e': S[i][j]='o'; break;
                                                    case 'f': S[i][j]='c'; break;
                                                    case 'g': S[i][j]='v'; break;
                                                    case 'h': S[i][j]='x'; break;
                                                    case 'i': S[i][j]='d'; break;
                                                    case 'j': S[i][j]='u'; break;
                                                    case 'k': S[i][j]='i'; break;
                                                    case 'l': S[i][j]='g'; break;
                                                    case 'm': S[i][j]='l'; break;
                                                    case 'n': S[i][j]='b'; break;
                                                    case 'o': S[i][j]='k'; break;
                                                    case 'p': S[i][j]='r'; break;
                                                    case 'q': S[i][j]='z'; break;
                                                    case 'r': S[i][j]='t'; break;
                                                    case 's': S[i][j]='n'; break;
                                                    case 't': S[i][j]='w'; break;
                                                    case 'u': S[i][j]='j'; break;
                                                    case 'v': S[i][j]='p'; break;
                                                    case 'w': S[i][j]='f'; break;
                                                    case 'x': S[i][j]='m'; break;
                                                    case 'y': S[i][j]='a'; break;
                                                    case 'z': S[i][j]='q'; break;
                                                    default: break;
                                        }
                    }
    }
    for(i=0;i<t;i++)
    {
             //   printf("Case #%d: %s\n",i+1,S[i]);
		cout<<"Case #"<<i+1<<": "<<S[i]<<endl;
    }                                                   
                                                          
    return 0;
}