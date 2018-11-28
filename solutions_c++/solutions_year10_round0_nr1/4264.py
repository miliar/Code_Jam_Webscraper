# include <iostream>
using namespace std;
# include <stdio.h>
int main()
{
        int cases,size,count=1,old_power[1000];
        bool state[1000],power[1000];
        long long int switches;
cin>>cases;
        while(cases--)
        {
            cin>>size;
            cin>>switches;
            for(int i=0;i<size;i++)
            {
                    state[i]=0;
                    power[i]=0;
            }
            power[0]=1;
    int i;
            while(switches--)
            {
                    for(i=0;i<size;i++)
                    {
                            if(power[i])
                            state[i]=1-state[i];
                    }
                    for(i=1;i<size;i++)
                    {
                        power[i]=power[i-1]&state[i-1];
                    }


            }

            cout<<"Case #"<<count++<<": ";
            if(state[size-1]&power[size-1])
            cout<<"ON";
            else
            cout<<"OFF";
            cout<<"\n";
        }
return 0;
}
