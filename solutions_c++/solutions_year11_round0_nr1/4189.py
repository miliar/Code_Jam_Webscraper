#include<iostream>
#include<cstdio>
#include<algorithm>
#include<stack>


using namespace std;
int bot[10000],move[10000],orange[10000],blue[10000];


int main()
{
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        int ir=0,im=0,steps=0;
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
        
        
            	char ch=0;
            while(!(ch=='O' || ch=='B'))    scanf("%c",&ch);
            bot[ir++]=ch;
            scanf("%d",&move[im]);
            im++;
        }
        
        int orangei=0,bluei=0,lpo=-1,lpb=-1,currento=1,currentb=1;;
        for(int i=0;i<n;i++)
        {
            
            
            if(bot[i]=='O')
            {
                while(move[i] > currento)
                {
                    orange[orangei++]=1;
                    currento++;
                }
            
            
                while(move[i] < currento)
                {
                    orange[orangei++]=1;
                    currento--;
                }
                while(orangei <= lpb)
                	orangei++;
                orange[orangei++]=2;
                lpo=orangei-1;
            }
            
            
            
            if(bot[i]=='B')
            {
                while(move[i] > currentb)
                {
                	    blue[bluei++]=1;
               		    currentb++;
                }
            
//            cout<<"hello";
            
               		 while(move[i] < currentb)
                	 {
                	    blue[bluei++]=1;
                	    currentb--;
                	 }
                while(bluei <= lpo)
                	bluei++;
                blue[bluei++]=2;
                lpb=bluei-1;
            }
        }
        cout<<"Case #"<<z<<": "<<max(orangei,bluei)<<endl;
    }
}
