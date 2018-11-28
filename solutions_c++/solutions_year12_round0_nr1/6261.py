/* By Neciu Dan
LANG=C++*/


#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main(){
    freopen("A-small-attempt2.in","rt",stdin);
    freopen("A0.out","wt",stdout);
    
    int T;
    cin >> T;

    for(int ii=0;ii<T;++ii)
{
   char G[1000];
   cin.getline (G,1000);
    
    for(int i=0;i < G[0];++i)
    {
            if(G[i]=='a')
            G[i]='y';
            else
            if(G[i]=='b')
            G[i]='h';
            else
            if(G[i]=='c')
            G[i]='e';
            else
            if(G[i]=='d')
            G[i]='s';
            else
            if(G[i]=='e')
            G[i]='o';
            else
            if(G[i]=='f')
            G[i]='c';
            else
            if(G[i]=='g')
            G[i]='v';
            else
            if(G[i]=='h')
            G[i]='x';
            else
            if(G[i]=='i')
            G[i]='d';
            else
            if(G[i]=='j')
            G[i]='u';
            else
            if(G[i]=='k')
            G[i]='i';
            else
            if(G[i]=='l')
            G[i]='g';
            else
            if(G[i]=='m')
            G[i]='l';
            else
            if(G[i]=='n')
            G[i]='b';
            else
            if(G[i]=='o')
            G[i]='k';
            else
            if(G[i]=='p')
            G[i]='r';
            else
            if(G[i]=='q')
            G[i]='z';
            else
            if(G[i]=='r')
            G[i]='t';
            else
            if(G[i]=='s')
            G[i]='n';
            else
            if(G[i]=='t')
            G[i]='w';
            else
            if(G[i]=='u')
            G[i]='j';
            else
            if(G[i]=='v')
            G[i]='p';
            else
            if(G[i]=='w')
            G[i]='f';
            else
            if(G[i]=='x')
            G[i]='m';
            else
            if(G[i]=='y')
            G[i]='a';
            else
            if(G[i]=='z')
            G[i]='q';
            }
            cout<<"Case #"<<ii+1<<": "<<G<<endl;
            }
            return 0;
            }
            
            
            
            
