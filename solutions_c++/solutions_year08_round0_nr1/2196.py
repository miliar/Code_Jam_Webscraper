#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
using namespace std;

int main()
{
    ifstream  enter ("A-large.in");
    ofstream  exit ("output.txt");
    int N=0;
    int S=0;
    int Q=0;
    string query;
    enter >> N;
    for (int w=0; w<N; w++)
    {
             int counter=-1, change=0, pause=0, output=-1;
             enter >> S;
             string engine[S];
             string dub;
             getline(enter,dub);
             for (int j=0; j<S; j++)
             {
                    getline(enter,engine[j],'\n'); 
             }
             enter >> Q;
             string qrray[Q];
             getline(enter,dub);
             for (int k=0; k<Q; k++)
             {   
                 getline(enter,qrray[k],'\n');
             }
            while(output==-1)
             {
             for (int p=0; p<S; p++)
             {
                   for(int i=pause; i<=Q; i++)
                   {
                           if(i==Q)
                           { 
                                   output=change;
                                   exit << "Case #" << w+1 <<": " << output <<endl;
                                   break;
                           } 
                           if(qrray[i]== engine[p])             
                           {
                                    if(i > counter)
                                    {
                                                 counter = i;
                                    }
                                    break;
                           }
                   }
                   if (output!=-1)
                   {
                                  break;
                   }
             }
             pause=counter;
             change++;

             }
                           
    }
    
return 0;
}
