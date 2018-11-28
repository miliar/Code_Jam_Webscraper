#include <iostream>
#include <cstdlib>
using namespace std;

int main()
{
    long nt;
    cin >> nt; // test cases
    
    for(long k=0;k<nt;k++)
    {
        long t;
        cin>>t;
        long step[100];
        char robot[100];
        long value[100];
        
        for(long i=0;i<t;i++)
        {
            step[i]=0;
        }
        
        for(long l=0;l<t;l++)
        {
            cin >>robot[l];
            cin >>value[l];
        }
        
        for(long i=0;i<t;i++)
        {
            if(robot[i]=='O')
            {
                long j= i-1;
                long steps=0;
                long count= value[i];
                long pos = 1;
                
                while(j>=0 && robot[j]=='B')
                {
                    steps+=step[j];
                    j--;
                }
                
                if(j>=0)
                {
                    if(robot[j]=='O')
                    {
                        count = (long)abs(value[i]-value[j]);
                        pos=0;
                    }
                }
                
                if(steps>=count)
                    step[i]=1;
                else
                    step[i]=count-steps+1-pos;
            }
            
            else if(robot[i]=='B')
            {
                long j=i-1;
                long steps=0;
                long count=value[i];
                long pos=1;
                while(j>=0 && robot[j]=='O')
                {
                    steps+=step[j];
                    j--;
                }
                if(j>=0)
                {
                    if(robot[j]=='B')
                    {
                        count = (long)abs(value[i]-value[j]);
                        pos=0;
                    }
                }
                if(steps>=count)
                    step[i]=1;
                else
                    step[i]=count-steps+1-pos;
            }
        }
        
        long values=0;
        for(long i=0;i<t;i++)
        {
            
            values+=step[i];
        }
        cout<<"Case #" << k+1 << ": "<<values<<endl;
    }
    return 0;
}
