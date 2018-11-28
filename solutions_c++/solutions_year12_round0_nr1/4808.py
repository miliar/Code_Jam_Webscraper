//
//  main.cpp
//  google code jam 2012 language qs
//
//  Created by nitish on 14/04/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#include <iostream>
using namespace std;
void language();
char mapping[26];
int c=0;
int main ()
{
    int t;
    cin>>t;
    getchar();
    mapping[0]='y';
    mapping[1]='h';
    mapping[2]='e';
    mapping[3]='s';
    mapping[4]='o';
    mapping[5]='c';
    mapping[6]='v';
    mapping[7]='x';
    mapping[8]='d';
    mapping[9]='u';
    mapping[10]='i';
    mapping[11]='g';
    mapping[12]='l';
    mapping[13]='b';
    mapping[14]='k';
    mapping[15]='r';
    mapping[16]='z';
    mapping[17]='t';
    mapping[18]='n';
    mapping[19]='w';
    mapping[20]='j';
    mapping[21]='p';
    mapping[22]='f';
    mapping[23]='m';
    mapping[24]='a';
    mapping[25]='q';
    
    
    while(t--)
    {
        c++;
       // cout<<c<<endl;
        language();
    }
    return 0;
}

void language()
{
    char G[101],S[101];
   // char ch='a';
  //  cout<<(int)ch;
  //  cout<<"enter a line\n";
    cin.getline(G,101);
    int i=0;
    while(G[i]!='\0')
    {
        if(G[i]==' ')
            S[i]=' ';
        else
        {
            S[i]=mapping[G[i]-97];
        }
            
        i++;
    }
    S[i]='\0';
    cout<<"Case #"<<c<<": "<<S<<endl;
    
    
}