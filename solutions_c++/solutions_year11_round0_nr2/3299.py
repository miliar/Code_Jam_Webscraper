#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <queue>
#include <map>
#include <vector>
#include <stack>
#include <stdio.h>
#include <cstdio>

using namespace std;


int main()
{
   freopen("B-large.in","r",stdin);
   freopen("magicout.txt","w",stdout);
   int t;
   cin>>t;
   int cont = 1;
   while(t>0)
   {
        map<char, map<char, char> > Combinations;
        map<char, vector<char> > arrAostos;
       t--;
       int c;
       cin>>c;
       for(int i=0;i<c;i++)
       {
           char ele[3];
           cin>>ele;
           Combinations[ele[0]][ele[1]] = ele[2];
           Combinations[ele[1]][ele[0]] = ele[2];
       }
       int d;
       cin>>d;
       for(int i=0;i<d;i++)
       {
           char arrA[2];
           cin>>arrA;
           arrAostos[arrA[0]].push_back(arrA[1]);
           arrAostos[arrA[1]].push_back(arrA[0]);
       }
       map<char, int> contem;
       int n;
       cin>>n;
       char pilha[100];
       int index=0;
       for(int i=0;i<n;i++)
       {
           cin>>pilha[index];

           if(index>0)
           {
               int entrou = 0;
               if(Combinations[pilha[index-1]][pilha[index]]>='A')
               {
                   contem[pilha[index-1]]--;
                   pilha[index-1] = Combinations[pilha[index-1]][pilha[index]];
                   contem[pilha[index-1]]++;
                   entrou = 1;
               }
               else
               {
                   vector<char> arrAs = arrAostos[pilha[index]];
                   for(int i=0;i<arrAs.size();i++)
                   {
                       if(contem[arrAs[i]]>=1)
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
   }
   return 0;
}
