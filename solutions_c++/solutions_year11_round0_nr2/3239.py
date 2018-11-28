#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <queue>
#include <map>
#include <vector>
#include <stack>
#include <stdio.h>

using namespace std;


int main()
{
   int t;
   cin>>t;
   int cont = 1;
   while(t>0)
   {
        map<char, map<char, char> > combinacoes;
        map<char, vector<char> > opostos;
       t--;
       int c;
       cin>>c;
       for(int i=0;i<c;i++)
       {
           char ele[3];
           cin>>ele;
           combinacoes[ele[0]][ele[1]] = ele[2];
           combinacoes[ele[1]][ele[0]] = ele[2];
       }
       int d;
       cin>>d;
       for(int i=0;i<d;i++)
       {
           char op[2];
           cin>>op;
           opostos[op[0]].push_back(op[1]);
           opostos[op[1]].push_back(op[0]);
       }
       map<char, int> contem;
       int n;
       cin>>n;
       char pilha[100];
       int index=0;
       for(int i=0;i<n;i++)
       {
           cin>>pilha[index];
           //cout<<pilha[index]<<endl;
           //system("PAUSE");
           if(index>0)
           {
               int entrou = 0;
               //cout<<pilha[index-1]<<" "<<pilha[index]<<" "<<combinacoes[pilha[index-1]][pilha[index]]<<endl;
               if(combinacoes[pilha[index-1]][pilha[index]]>='A')
               {
                   contem[pilha[index-1]]--;
                   pilha[index-1] = combinacoes[pilha[index-1]][pilha[index]];
                   contem[pilha[index-1]]++;
                   entrou = 1;
               }
               else
               {
                   vector<char> ops = opostos[pilha[index]];
                   for(int i=0;i<ops.size();i++)
                   {
                       if(contem[ops[i]]>=1)
                       {
                           entrou = 1;
                           index = 0;
                           map<char, int>::iterator pos;
                           contem.clear();
                           break;
                       }
                   }
               }
               if(entrou == 0)
               {
                   contem[pilha[index]]++;
                   index++;
               }
           }
           else
           {
               contem[pilha[index]]++;
               index++;
           }
       }
       pilha[index] = '\0';
       cout<<"Case #"<<cont<<": [";
       for(int i=0;i<index;i++)
       {
           cout<<pilha[i];
           if(i!=index-1)
               cout<<", ";
       }
       cout<<"]"<<endl;
       cont++;
       //cout<<pilha<<endl;
   }
   return 0;
}
