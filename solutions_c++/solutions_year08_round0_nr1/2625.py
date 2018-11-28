#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main(void)
{
   int ncases=0;
   cin>>ncases;
   for (int i=0 ; i<ncases ; i++)
   {
     int Res=0;
     vector <string> engines;
     vector <string> strs;

     string engine;
     int nengines=0;
     cin>>nengines;
     getline(cin, engine); // <- workaround

     for (int j=0 ; j<nengines ; j++)
     {
        getline(cin, engine);
//        cout<<"engine["<<j<<"]"<<"["<<engine<<"]"<<endl;
        engines.push_back(engine);
     }
     
     bool engGroup[100];
     int nengGroup = 0;
     for (int j=0 ; j<100 ; j++)
     {
       engGroup[j]=0;
     }
     
     int nstrs=0;
     cin>>nstrs;
     getline(cin, engine); // <- workaround

     for (int j=0 ; j<nstrs ; j++)
     {
       getline(cin, engine);
       
       for (int k=0 ; k<nengines ; k++)
       {
         if (engine == (string)(engines[k]))
         {
           if (engGroup[k] == 0)
           {
             // Only case - rest all engines are already picked up
             if (nengGroup == nengines-1)
             {
               //reset other pistons
               for (int l=0 ; l<100 ; l++)
               {
                 engGroup[l] = 0;
               }
               engGroup[k] = 1;
               Res++;
               nengGroup = 1;
             }
             else
             {
               engGroup[k] = 1;
               nengGroup++;
             }
           }
           break;
         }
       }
     }
     cout<<"Case #"<<i+1<<": "<<Res<<endl;

   }
    return 0;
}

