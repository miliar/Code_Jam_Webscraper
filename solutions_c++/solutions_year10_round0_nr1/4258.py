#include <iostream>
#define NOFF  1
#define NON  2
#define ROFF 3
#define RON 4

using namespace std;

int snap(int state)
{
    switch(state)
    {
        case NOFF:
        case NON:
             return state;
        case ROFF:
             return RON;
        case RON:
             return ROFF;   
    }     
}

int adjust(int prefixState, int curstate)
{
   switch(prefixState)
    {
        case NOFF:
        case NON:
        case ROFF:
             if(curstate == ROFF)
             {
                return NOFF;
             }   
             else if(curstate == RON)
             {
                  return NON;
             }
             else
             {
                 return curstate;
             }
        case RON:
             if(curstate == NOFF)
             {
                return ROFF;
             }   
             else if(curstate == NON)
             {
                  return RON;
             }
             else
             {
                 return curstate;
             }
    }
}

int doSim(int N, long long K)
{
    //init
    int arr[30];
    arr[0] = ROFF;
    for(int i=1; i<N; ++i)
        arr[i] = NOFF;
    
    //k simulation
    for(long long k=0; k<K; ++k)
    {
        for(int i=0; i<N; ++i)
        {
            arr[i] = snap(arr[i]);
            if((i-1)>=0)
            {
               arr[i] = adjust(arr[i-1],arr[i]);
            }
        }
    }
     
    return (arr[N-1] == RON);
}

int main()
{
    int t;
    cin >> t;
    for(int i =0; i < t; ++i)
    {
          int N;
          long long K;
          cin >> N >> K;  
          if(doSim(N, K) == 0)
          {
            cout << "Case #" << i+1 <<": OFF\n";
          }
          else
          {
            cout << "Case #" << i+1 <<": ON\n";  
          }
    } 
    return 0;
}
