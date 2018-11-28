#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int T;
    cin>>T;
    
    int N;
    char R[100];
    int P[100];
    
    int Diff = 0;
    int Time = 0;
    int BluePos = 1;
    int OrPos = 1;
    
    for(int t=0;t<T;t++)
    {
        Diff = 0;
        Time = 0;
        BluePos = 1;
        OrPos = 1;
        
        cin>>N;
        for(int i=0;i<N;i++)                 
            cin>>R[i]>>P[i];      
        
        for(int i=0;i<N;i++)
        {
            if(R[i]=='O')
            {
                if(i==0) { Diff = P[i] - OrPos + 1; Time = P[i] - OrPos + 1; OrPos = P[i]; }
                else if(R[i-1]==R[i]) { Diff = Diff + abs(P[i]-OrPos) + 1; Time = Time + abs(P[i]-OrPos) + 1; OrPos = P[i]; }
                else 
                { 
                    if(Diff >= abs(OrPos - P[i])) { Time = Time + 1; OrPos = P[i]; Diff = 1; }
                    else { Time = Time + abs(P[i] - OrPos) - Diff + 1 ; Diff = abs(P[i] - OrPos) - Diff + 1; OrPos = P[i]; }
                }                  
            }
            
            else
            {                        
                if(i==0) { Diff = P[i] - BluePos + 1; Time = P[i] - BluePos + 1; BluePos = P[i]; }
                else if(R[i-1]==R[i]) { Diff = Diff + abs(P[i]-BluePos) + 1; Time = Time + abs(P[i]-BluePos) + 1;  BluePos = P[i]; }
                else 
                { 
                    if(Diff >= abs(BluePos - P[i])) { Time = Time + 1; BluePos = P[i]; Diff = 1; }
                    else { Time = Time + abs(P[i] - BluePos) - Diff + 1 ; Diff = abs(P[i] - BluePos) - Diff + 1; BluePos = P[i]; }
                }     
            }
            
            
        }
      
        cout<<"Case #"<<t+1<<": "<<Time<<endl;
        
    }   
    return 0;
}
