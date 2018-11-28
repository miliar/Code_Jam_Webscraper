#include<iostream>

using namespace std;




int main()
{
    int t;
          cin>>t;
          int count =0;
          while(t--)
          {         
                    int v[100]={0};
                    
                    int n;
                    cin>>n;
                    int sp=0,ss=0,ssp=0;
                    int max=0;
			
                    for(int i=0;i<n;i++)
                            cin>>v[i];
                               
                    for(int i=0;i<(1<<n);i++)   
                    {
                            sp=0;ssp=0;ss=0;
			    bool spu=false,sspu=false;
                            for(int j=0;j<n;j++)
                            {
                                    if((1<<j) & i )
                                    {
                                                 ss+=v[j];
                                                 if(ssp==0)
							sspu=true;
						 ssp^=v[j];
                                    }
                                    else {
						if(sp==0)
							spu=true;
                                                 sp^=v[j];
                                         }
                            }
                           // cout<<"i:"<<i<<"   ss:"<<ss<<"  "<<"sp:"<<sp<<"  "<<"  ssp:"<<ssp<<"  max:"<<max<<endl;
			if(sspu && spu)
			{
                            if(ssp == sp && ssp !=0)
                                  if(ss > max)
                                        max=ss;
			}
                    }
                    if(max==0)
                              cout<<"Case #"<<++count<<": NO"<<endl;
                    else 
                        
                              cout<<"Case #"<<++count<<": "<<max<<endl;
          }
          return 1;
}
                                                
                                                        
                    
                    
