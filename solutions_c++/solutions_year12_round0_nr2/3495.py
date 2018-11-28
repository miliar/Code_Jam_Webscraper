#include<iostream>
#include<fstream>
using namespace std;

void fun(const int  z, const int & googlers,  int  surp,const int & p, int *& max,ofstream & wyj)
{
/*
cout<<endl;
cout<<" "<<googlers<<" "<<surp<<" "<<p<<" "<<endl;
for(int i=0;i<googlers;i++)
{
        cout<<" "<<max[i];
        cout<<endl;
}
*/
/*
for(int i=0;i<googlers;i++)
{
        if(max[i] != 0)
        {
        if(max[i] % 3 == 0 )
        {
                  max[i]/=3;//bez reszty
        }
        else
        {
                  max[i]/=3;
                  max[i]+=1;
        }
        }
        
}
*/

int i = 0;
int tmp = p-1;
while(i<googlers)
{
             /*
          if(max[i] == tmp && max[i] != 0)
          {
                    max[i]+=1;
                    surp--;
          }*/
          if(max[i]!=0)
          {
          if(max[i] % 3 == 0)
          {
                    max[i]/=3;
                    if(max[i] == tmp && surp>0)
                    {
                    max[i]+=1;
                    surp--;
                    }
                    goto a;
          }
          
           if(max[i] % 3 == 1)
          {
                    max[i]/=3;
                    max[i]+=1;
                     goto a;
          }
          
           if(max[i] % 3 == 2)
          {
                    max[i]/=3;
                    max[i]+=1;
                      if(max[i] == tmp && surp>0)
                      {
                    max[i]+=1;
                    surp--;
                    }
                     goto a;
          }
          }
       a:   
         
          
          i++;
}
int licznik=0;
for(int i=0;i<googlers;i++)
{
if(max[i]>=p)
licznik++;
}

wyj<<"Case #"<<z+1<<": "<<licznik<<endl;

}

void wczytaj()
{
     ifstream wejscie("Problem B. Dancing With the Googlers.in");
     ofstream wyjscie("Problem B. Dancing With the Googlers.out");
     if(wejscie.good())
     {
     
     int N;
     
     wejscie>>N;
  //   cout<<N;
     for(int i=0;i<N;++i)
     {
             int googlers;
             
             int surp;
             int p;
             wejscie>>googlers;
             
             int * max = new int [googlers];
             
             wejscie>>surp;
             wejscie>>p;
             
             for(int j=0;j<googlers;j++)
             wejscie>>max[j];
             
             fun(i,googlers,surp,p,max,wyjscie);
             
             
             
             
             delete [] max;
             
             
             
     }
}
}
             
             
     



int main()
{
    
    
    
    wczytaj();
    
    
    cin.ignore();
    getchar();
    return 0;
}
