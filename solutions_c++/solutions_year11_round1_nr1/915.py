#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<cstdlib>

using namespace std;

int main()
{
    int T,totalcase;
    cin>>T;
    totalcase=T;
    
    while(T)
    {
           string k;
           int n;
		   float pg,pd; 
           cin>>k>>pd>>pg;

		   int flag = 0;           

//			cout<<k.length()<<endl;

          if(k.length() < 3)
          {
				const char* c = k.c_str();
				n = atoi(c);
          
           for(int i=1;i<=n;i++)
           {
				for(int j=0;j<=n;j++)
				{
					float fpd = (((float)j*100)/(float)i);
					if(pd==fpd)
					{
						flag=1;
						break;
					}
				}
		   }
		}
		else
		 flag=1;
		   

		   
		   if((pg==0&&pd!=0)||pg==100&&pd!=100)
		   {
				flag=0;
		   }

		   
		   if(flag==1)
		   cout<<"Case #"<<totalcase-T+1<<": Possible"<<endl;
		   else
		   		   cout<<"Case #"<<totalcase-T+1<<": Broken"<<endl;
		   
            
            
            T--;
    }
    
    return 0;
    
}


		   //for( int k=0;k<poss.size();k++)
//		   {
//				for(int l = poss[k].first;;l++)
//				{
//					for(int m = max(poss[k].second,l);;m++)
//					{
//						float fpg = (((float)l*100)/(float)m);
//							if(fpg==pg)
//							{
//								flag =1;
//								break;		
//							}
//							if(fpg<pg)
//							{
//								flag=-1;
//								break;
//							}
//					}
//					
//					if(flag==1)
//					{
//						break;
//					}
//				}
//		   }
