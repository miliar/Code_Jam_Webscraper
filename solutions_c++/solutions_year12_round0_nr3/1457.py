#include<iostream>
#include<map>

int tens[]={1,10,100,1000,10000,100000,1000000,10000000};      


using namespace std;

int main()
{
    freopen("A5.in","r",stdin);
    freopen("GCJO3L.txt","w",stdout);
    
    int t,x=0;
    scanf("%d",&t);
    while(t--)
    {
              int a,b,i,j,k,dig=0,c;
              int ans=0;
              scanf("%d%d",&a,&b);
              
                  
              
              c=a;
              while(c)
              {
                    dig++;
                    c/=10;
              }
                
              for(i=a;i<=b;i++)
              {
                      
                      map<int,int> m;

                      j=i;
                      int num;
                      m[i]=1;
                      
                      for(k=2;k<=dig;k++)
                      {
                            num=(i%tens[dig-k+1])*tens[k-1]+(i/tens[dig-k+1]);  
                            
                            if(!m[num] && num>i && num<=b)
                            {
                                    ans++;
                                    m[num]=1;
                            }     
                      }       
                      
                      
                               
              }
              cout<<"Case #"<<++x<<": "<<ans<<endl;
    }
}
