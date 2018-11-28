//Vignesh M

#include<string>
#include<iostream.h>

#include<fstream.h>


   

class queue
{
      int lead;
      int n;
      long long double g[1001];      
public:       
              queue()
              {} 
       queue(int len,long long double garr[1001])
       {
              n=len;
              for(int i=0;i<1001;i++)g[i]=garr[i];
              lead=-1;
       }       

       long long double peek()
       {
           return(g[0]);
       }

       void plop()
       {
           long long double temp=g[0];
           int i=0;
           for(i=0;i<n-1;i++) g[i]=g[i+1];
           g[i]=temp;
       }       
       

};


long long double solve(int n,long long double g[1001],long long double r,long long double k)
{
    queue q(n,g);
    long long double cash=0;  
    for(long long double z=0;z<r;z++)
    {


            long long double cap=0,ploprest=0;
            for(int zi=0;zi<n;zi++)
            {
                    if(((cap+q.peek())<=k)&&(ploprest==0))
                    { cap+=q.peek();
                      cash+=q.peek();
                      q.plop();
                    }    
            }      
    }    
    return cash;


}


int main()
{
     ifstream x;
     x.open("q.in");
     ofstream y;
     y.open("a.in");  


long long double man; 
int T;

x>>T;
cout<<"\nTCases : "<<T;


pause();
//int solve(int n,int g[1000],int r,int k)
long long double r,k,n,ans;
int Tcount=1;
long long double g[1001]={0};

while(Tcount<=T)
{   
         cout<<"\n"<<"Test case: "<<Tcount;
    x>>r;
    x>>k;
    x>>n;    

    for(int ncounter=0;ncounter<n;ncounter++)
      x>>g[ncounter];
    ans=solve(n,g,r,k);
    y<<"Case #"<<Tcount<<": "<<ans<<"\n";
    Tcount++;
}    
     cout<<"! DONE BABY!:) ";
     
     
     x.close();
     //Saving Results
pause();
     return 0;
}
