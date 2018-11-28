#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
class themePark
{
	long long int t,R,K,N,res;
	vector <int> v;
	public:
	themePark(){
       res=0;

	}

  void accept()
    {
    cin>>R>>K>>N;
    for(int i=0;i<N;i++)
     {
            cin>>t;
            v.push_back(t);
	 }
    
    }

void func()
  {
    long long int *store_cost=new long long int[N];
    long long int *next_pos=new long long int[N];
     long long int i;
    long long int sum,p,st,k;
bool fl=true;
 for(i=0;i<N;i++)
 {
  store_cost[i]=-1;
  next_pos[i]=-1;
}

      if(N==1)
      {
	res=R;
	return;
      }
	 
          p=0;
         st=p; 
                 
  
    for( i=1;i<=R;i++)
     {
     	fl = true;
	    sum=0; 
           if(store_cost[p]!=-1)
            {res+=store_cost[p];
             p=next_pos[p];
            }
           else
	   {
      
              do
               {                                    
                  if(sum+v[p]<=K && (p!=st || fl==true))
                  {              
                   sum+=v[p];
                    p=(p+1)%N;
                   if(p==st)
                   fl=false;
                   }
                 else
                 {
                 store_cost[st]=sum;
                 next_pos[st]=p;
                 st=p;  
       
                    res+=sum;    
                 break;
                 }            
            
               }  while(1);
          
                         
	  }                
            
     
     }


}

long long int ret()
	{
	
	return res;

	}

	
};
int main()
{
	int T,i;
	cin>>T;
	themePark *ob;
	ob=new themePark[T+1];
	for(i=1;i<T+1;i++)
	{
		ob[i].accept();
                ob[i].func();

	}
	for(i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": "<<ob[i].ret()<<endl;
	}
	return 0;
}
