#include<iostream>
using namespace std;
#include<fstream>
#include<stdio.h>
#include<string>
#include<vector>

//int a[15][26];
int b[15][26];

void split(string s)
{

  int lth=s.size();
  int i=0,ctr=-1;
    
  while(i < lth)
  {
    ctr++;
    if( s[i] != '(' )
    {
        b[ctr][s[i]-'a']++;
        i++;
        continue;
    }
    i++;
    while( i<lth && s[i] != ')' )
    {
           b[ctr][s[i]-'a']++;
           i++;
    } 
    i++;
  }

  return;
}

bool feasible(string s, int L)
{
     for(int i=0; i<L; i++)
     {
             if(b[i][s[i]-'a'] == 0)
                 return false; 
     }
     return true;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    
    int L,D,N,ctr;
    vector <string> dict;
    string s,t;
    
    fin>>L>>D>>N;
    
    for(int i=0; i<D; i++)
    {
            fin>>s;
            dict.push_back(s);
//            for(int j=0; j<L; j++)
//                    a[j][s[i]-'a']++;
    }
//    sort(dict.begin(), dict.end());
    
    for(int C=1; C<=N; C++)
    {
            fin>>s;
            
            for(int i=0; i<15; i++)
               for(int j=0; j<26; j++)
                   b[i][j] = 0;
            
            split(s);
            
            ctr = 0;
            for(int i=0; i<D; i++)
            {
                    if(feasible(dict[i], L))
                         ctr++;
            }
            fout<<"Case #"<<C<<": "<<ctr<<"\n";
    }
          
    return 0;
}
