#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<fstream>
#include<stdio.h>
#include <stdlib.h>

#define INPUT "large.txt"
#define FOR(i,n) for(int i=0;i<n;i++)

FILE* ifp = fopen(INPUT,"r");
FILE* ofp = fopen("output.txt","w+");
//FILE* ifp = stdin;

#define MAXC 36
#define MAXD 26
#define MAXN 100

using namespace std;

int main()
{
int t,c,d,n, D[26][26];
char C[26][26], str[MAXN+1];

fscanf(ifp,"%d",&t);

FOR(T,t)
{
         FOR(i,26)
                 FOR(j,26){
                          D[i][j]= 0;
                          C[i][j]='.';
                 }
                 
        fscanf(ifp,"%d",&c);
        //cout<<c<<endl;
        
        FOR(i,c)
               {
                       
                       fscanf(ifp,"%s",str);
               //cout<<str<<endl;
                                 C[str[0]-'A'][str[1]-'A'] = str[2];
                                 C[str[1]-'A'][str[0]-'A'] = str[2];
               }
        
        fscanf(ifp,"%d",&d);
       
        FOR(i,d)
                {
                        fscanf(ifp,"%s",str);
                        D[str[0]-'A'][str[1]-'A'] = 1;
                        D[str[1]-'A'][str[0]-'A'] = 1;
                        
               }
        
       fscanf(ifp,"%d",&n);
       fscanf(ifp,"%s",str);
       char l[MAXN];
       int ptr=0;
       
       FOR(i,n)
       {
             l[ptr++]=str[i];
             
             if(ptr>1)
             {
              /*check combine*/
              char comb = C[l[ptr-2]-'A'][str[i]-'A'];  
             
              if(comb!='.'){
                       ptr-=2;
                       l[ptr++]=comb;
                     }
               else {
                    FOR(j,ptr-1)
                              if(D[l[j]-'A'][str[i]-'A'])
                              {
                                  ptr=0;
                                  break;
                              }     
               }   
             }
       }
       
       fprintf(ofp,"Case #%d: [",T+1);
       FOR(i,ptr)
       {
                 fprintf(ofp,"%c",l[i]);
                 if(i<ptr-1)    
                                fprintf(ofp,", ");
                       
       }
       fprintf(ofp,"]\n");
       
       /*FOR(i,26)
       {
               FOR(j,ptrc[i])
                            cout<<C[i][j];
               cout<<endl;
       } */
       
}


system("Pause");
return 0;
}
