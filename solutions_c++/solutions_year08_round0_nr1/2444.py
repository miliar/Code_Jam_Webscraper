#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include <fstream>
#include<string>
#include<vector>

using namespace std;

//FILE *in =fopen("A-small.in","r");
FILE *in =fopen("A-large.in","r");

//FILE *out =fopen("A-small.out","w");
FILE *out =fopen("A-large.out","w");

int N,S,Q;

vector <string> ser;
vector <string> qur;

vector <int> serflag;

int main ()
{

    char ch;
    int i,j,k,l,n,count;
    string str;
    
    fscanf(in,"%d\n",&N);
    
    for( i=0 ; i < N ; i++ )
    {
         //read servers
         fscanf(in,"%d\n",&S);
         ser.resize(S);
         for( j=0 ; j < S ; j++ )
         {
              ser[j]="";
              fscanf(in,"%c",&ch);
              while(ch!='\n')
              {
                        ser[j]+=ch;
                        fscanf(in,"%c",&ch);
              }
         }
         //check
        /* for( j=0 ; j < S ; j++ )
         {
              cout<<ser[j]<<endl;
         }*/
         
         //read queries
         fscanf(in,"%d\n",&Q);
         qur.resize(Q);
         for( j=0 ; j < Q ; j++ )
         {
              qur[j]="";
              fscanf(in,"%c",&ch);
              while(ch!='\n')
              {
                        qur[j]+=ch;
                        fscanf(in,"%c",&ch);
              }
         }
         //check
         /*for( j=0 ; j < Q ; j++ )
         {
              cout<<qur[j]<<endl;
         }*/
         
         //process
         
         n=ser.size();
         serflag.resize(S);
         for(j=0;j<ser.size();j++)serflag[j]=0;
         count=0;
         for(j=0;j<qur.size();j++)
         {
                for( k=0 ; k< ser.size();k++)
                {
                     if( qur[j] == ser[k] )
                     {
                         if( serflag[k] == 0 )
                         {
                             serflag[k]=1;
                             n--;
                             break;
                         }
                         if( serflag[k] == 1 )
                         {
                             break;
                         }
                                           
                     }
                }
                if( n == 0 )
                {
                    count++;
                    for( l=0 ; l < serflag.size() ; l++)
                    {
                           if(ser[l] != ser[k] )
                           {
                                     serflag[l]=0;
                                     n++;
                           }                           
                    }
                }                  
         }
         
         //output
         fprintf(out,"Case #%d: %d\n",i+1,count);
    }

    return 0;
}
