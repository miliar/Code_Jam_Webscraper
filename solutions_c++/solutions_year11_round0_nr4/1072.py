#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#define TASK "D-large"
#define Max 1000
using namespace std;

int T,N,Seq[Max];

int main()
{
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    
    cin>>T;
    
    for(int i=0; i<T; i++)
    {
        cin>>N;
        
        for(int j=0; j<N; j++)
        {
            cin>>Seq[j];
        }
        
        long long Expected=0;
        
        for(int j=0; j<N; j++)
        {
            if(Seq[j]>0)
            {
                int length=1, ind=Seq[j]-1;
                Seq[j]=0;
                
                while(Seq[ind]>0)
                {
                    int tmp=ind;
                    ind=Seq[ind]-1;
                    Seq[tmp]=0;
                    length++;
                }
                
                Expected+=(length>1)?length:0;
            }
        }
        
        cout<<"Case #"<<i+1<<": "<<Expected<<".0"<<endl;
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
