#include<iostream>
#include<string>
#include<map>
using namespace std;


int jw1(int i){
    int cnt=1;
    int jl=i;
    while(jl/=10)
       cnt++;    
    return cnt;
}

int main(){
    int cnt;
   // freopen("in.txt",'r',stdin);
   freopen("input.txt","r",stdin); 
   freopen("output.txt","w",stdout); 
 int data[5000];

    
    
    
    
   // scanf("%d\n",&cnt);
    cin>>cnt;
   // int a=cin.get();
  // fflush(stdin);

    
    for(int k=0;k<cnt;k++)
    {
            
          memset(data,0,sizeof(data));
           int m,n;
           int res=0;
           cin>>m>>n;
           int jw=0;
           jw=jw1(m);

          if((m/10))
          {
            for(int i=m;i<=(n);i++)
            {
                   data[i]=1;
                   int *shuzu=new int[jw];
                   int *jie=new int[jw];
                   int tem=i;
                   for(int j=jw-1;j>=0;j--)
                   {
                           shuzu[j]=tem%10;
                           tem=tem/10;
                   }
                   jie[0]=m;
                   for(int j=1;j<jw;j++)
                   {
                          jie[j]=shuzu[j];
                           for(int j2=1;j2<jw;j2++){
                                   int temj=j+j2;
                                  int tem2=shuzu[(temj)%jw];
                                  jie[j]=jie[j]*10+tem2;
                           }
                           
                         if(jie[j]>i&&jie[j]<=n){
                            res++;
                          //  cout<<"res:"<<res<<"  "<<i<<"--"<<jie[j]<<endl;
                         }
                   
                   }    



            }
                      
            
          }         
           
          
  

          
          
          
          cout<<"Case #"<<k+1<<": ";
          cout<<res;         
          cout<<endl;
            
    }
    

    
}
