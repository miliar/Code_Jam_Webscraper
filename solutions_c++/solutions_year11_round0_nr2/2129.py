#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <queue>
#include <iostream>
#include <algorithm>


using namespace std;

int main()
{
   freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T,kas=0;
    cin>>T;
    while(T--)
    {
        
        int SM,OP,i;
        string SS[300],PP[300],W;
        cin>>SM;
        for(i=0;i<SM;i++) cin>>SS[i];
        cin>>OP;
        for(i=0;i<OP;i++) cin>>PP[i];
        
        int LW;
        cin>>LW;
        cin>>W;
    
        vector<char>STK;
    
               
        
        for(i=0;W[i];i++)
        {
            char ch=W[i];
            STK.push_back(ch);
              
            if(i && SM)
            {
                for(int k=0;k<SM;k++)
                {
					if(STK.back()==SS[k][0] && STK[STK.size()-2]==SS[k][1])
					{
                    	STK.pop_back();
						STK[STK.size()-1]=SS[k][2];
						ch=STK.back();
                    }
					else if(STK.back()==SS[k][1] && STK[STK.size()-2]==SS[k][0])
					{
                    	STK.pop_back();
						STK[STK.size()-1]=SS[k][2];
						ch=STK.back();
					}
				}
            
            }
            if(i && OP)
            {
				for(int k=0;k<OP;k++)
				{
					int flag=0,flag2=0;
					for(int j=STK.size()-1;j>=0;j--)
					{
                    if(STK[j]==PP[k][0]) flag=1;
                    if(STK[j]==PP[k][1]) flag2=1;
					}
                
					if(flag && flag2){STK.clear();break;}
				}
            }
            
          
        }


        printf("Case #%d: ",++kas);
        printf("[");
        for(int j=0;j<(int)STK.size();j++)  
        {
            if(j) printf(", ");
            printf("%c",STK[j]);
        }
        printf("]");
        puts("");

        
    }
    
    
    
    
    
    
}

