#include<iostream.h>
#include<stdio.h>
#include<conio.h>
#include<algorithm>

using namespace std;

int main()
{
    int N, P,K,L, freqarr[100];
    cin.clear();
    cin>>N;
    int i,j,k,z,temp;
    int sum, sortfreqarr[100], keyarr[12];
    
    for(i=0; i<N; i++)
    {
             sum=0;
             
             cin.clear();
             cin>>P>>K>>L;
             
             cin.clear();
             for(j=0; j<L; j++)
             {
                      cin>>freqarr[j];
                      sortfreqarr[j]=freqarr[j];
             }
             for(j=0; j<K; j++)
                      keyarr[j]=0;

             
              sort(sortfreqarr, sortfreqarr + L);
             
             //for(j=0; j<L; j++)
             //cout<<" "<<sortfreqarr[j];
             k=0;
             temp=L;
             for(z=1; k<L; z++)
             {
                      //cout<<"hello";
                      for(j=0; j<K&&k<L; j++)
                     {
                               if(keyarr[j]>P)
                              continue;
                              //cout<<"hello";
                              sum+=sortfreqarr[--temp]*z;
                              k++;
                              keyarr[j]++;
                     }
             }
             
             cout<<"Case #"<<i+1<<": "<<sum<<endl;
             
    }
    //getch();
    return 0;
}
             
                     
                      
             
             
             
                      
             
                      
                      
                      
                      
                      
                      
             
             
    
