#include <iostream>
#include <algorithm>


using namespace std;

int main()
{
    int T,totalcase;
    cin>>T;
    totalcase = T;
    
    while(T)
    {
            int N;
            cin>>N;
            
            char bot;
            int but,poso,posb,timeo,timeb,timet;
            poso=1;
            posb=1;
            timeo=0;
            timeb=0;
            timet=0;
            
            int travtime, waittime,addtime;
            
            for(int i =0;i<N;i++)
            {
                    cin>>bot>>but;
                    
                    if(bot=='O')
                    {
                        travtime=but-poso;
                        if(travtime <0)
                                    travtime = -travtime;
                              
                        waittime = timet-timeo;
                        addtime = waittime-travtime;
                        if(addtime < 0)
                                   timet = timet-addtime;
                        //timet = timet + max(travtime,waittime);
                        timet++;
                        timeo=timet;     
                        poso=but;
                          
                    }
                    else
                    {
                        travtime=but-posb;
                        if(travtime <0)
                                    travtime = -travtime;
                        waittime = timet-timeb;
                        
                        addtime = waittime-travtime;
                        if(addtime < 0)
                                   timet = timet-addtime;

                        //timet = timet+max(travtime,waittime);
                        timet++;
                        timeb=timet;       
                        
                        posb=but;
                    }
            }
            
            cout<<"Case #"<<(totalcase+1-T)<<": "<<timet<<endl;
            
            T--;
    }
    
}
