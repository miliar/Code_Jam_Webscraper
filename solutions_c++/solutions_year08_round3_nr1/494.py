#include<iostream>
#include<vector>

using namespace std;

#define MAXLEN 1000

int P,K,L;
unsigned long long f[MAXLEN];

void init()
{
}

void sort()
{
     for(int i=0;i<L;i++)
     {
             for(int j=i+1;j<L;j++)
             {
                     if(f[i] < f[j])
                     {
                             int temp =f[i];
                             f[i] = f[j];
                             f[j] = temp;
                     }
             }
     }
}

int main()
{
    int N;
    cin>>N;
    
    for(int caseno=1;caseno<=N;caseno++)
    {
                 cin>>P;
                 cin>>K;
                 cin>>L;
                 
                 for(int i=0;i<L;i++)
                 {
                         cin>>f[i];
                 }                 
                 
                 sort();
                 
                 long pos = 1;
                 unsigned long long press = 0;
                 long j=0;
                 for(int i=0;i<L;i++)
                 {
                        press += f[i]*pos; 
                        j++;
                        if(j==K)
                        {
                                pos++;
                                j=0;
                        }                        
                 }
                 cout<<"Case #"<<caseno<<": "<<press<<endl;
    }
    return 0;
}
                                
                 
    
                 
                 
                 
    


