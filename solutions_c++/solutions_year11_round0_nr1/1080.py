#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#define TASK "A-large"
using namespace std;

int T,N,P;
char R;

int main()
{
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    
    cin>>T;
    
    for(int i=0; i<T; i++)
    {
        //0 -> Orange   1 -> Blue
        int Pos[2]={1,1}, Time[2]={0,0};
        
        cin>>N;
        for(int j=0; j<N; j++)
        {
            cin>>R>>P;
            
            if(R=='O')
            {
                 int length=abs(Pos[0]-P);
                 Time[0]=max(Time[0]+length+1,Time[1]);
                 Pos[0]=P;
                 if(Time[0]==Time[1])Time[0]++;
            }
            else
            {
                int length=abs(Pos[1]-P);
                Time[1]=max(Time[1]+length+1,Time[0]);
                Pos[1]=P;
                if(Time[1]==Time[0])Time[1]++;
            }
            
        }
        
        cout<<"Case #"<<i+1<<": "<<max(Time[0],Time[1])<<endl;
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
