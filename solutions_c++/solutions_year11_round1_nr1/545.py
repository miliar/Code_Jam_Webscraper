#include <iostream>
using namespace std;
int main()
{
    freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
            long long  N;
            int PD,PG;
            cin>>N>>PD>>PG;
            if(PG==100)
            {
                    if(PD!=100){
                      cout<<"Case #"<<t<<": Broken"<<endl;
                      continue;
                    }
                    else
                    {
                     cout<<"Case #"<<t<<": Possible"<<endl;
                     continue;
                    }       
            }
            if(PG==0)
            {
                   if(PD==0){
                     cout<<"Case #"<<t<<": Possible"<<endl;
                     continue;
                   }
                   else
                   {
                   cout<<"Case #"<<t<<": Broken"<<endl;
                   continue;
                   }
            }
            bool ss=true;
            if(N>100000) 
            {  cout<<"Case #"<<t<<": Possible"<<endl; continue;
            }
            for(long long  i=1;i<=N*PD/100.0;i++)
            {   if(i*100%PD==0){
                 cout<<"Case #"<<t<<": Possible"<<endl;
                 ss=false;
                 break;
                 }
            }
            if(ss)
            cout<<"Case #"<<t<<": Broken"<<endl;            
    }    
    getchar();
    return 0;
}
