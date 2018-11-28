#include<iostream>
#include<string>
#include<vector>
#include<math.h>
using namespace std;
vector <int> prim;
void prime()
{
   long long const p=10000;
   //long long const n=10;
   bool a[p];
   for(long long i=0;i<p;i++)
   a[i]=1;
   a[0]=0;
   a[1]=0;
   for(long long i=2;i<sqrt(p);i++)
   {
       if(a[i])
       for(long long j=i*i;j<p;j=j+i)
                a[j]=0;        
   }
  
   //long long sum=0;
   for(long long i=0;i<p;i++)
            if(a[i])
            {
                    //   sum+=i;
                  prim.push_back(i);
                  //cout<<i<<"  ";
            }
            
  // cout<<endl<<sum;
   //getchar();
   ///return 0;
}
void sets(int a,int b,int p)
{
     vector <int> n(b-a+1);    
     for(int i=a;i<=b;i++)
     {
             n[i-a]=i;        
     }
     int m=0;
     while(prim[m]<p)
     {
            m++;        
     }
     int fp=prim[m];
     vector <int> flag=n;
     while(fp<=b)
     {
                 
     for(int i=0;i<flag.size();i++)
     {
             if(n[i]%fp==0)
             {
                  for(int j=i;j<flag.size();j=j+fp)    
                  {    
                       int x=flag[i];
                       int y=flag[j];
                       for(int k=0;k<flag.size();k++)
                       if(flag[k]==y)
                              flag[k]=x;
                       flag[j]=flag[i];  
                  }        
             }        
     }
     m++;
     fp=prim[m];
     /* for(int i=0;i<flag.size();i++)
             cout<<flag[i]<<endl;
      cout<<endl<<endl;*/
     }
    
     sort(flag.begin(),flag.end());
     int count=1;
     for(int i=1;i<flag.size();i++)
     {
          if(flag[i-1]==flag[i])
          continue;
          else count++;   
     }
     cout<<count;
}
int main()
{
    int k;
    cin>>k;
    prime();
     for(int i=0;i<k;i++)
        {
                int a,b,p;
                cin>>a>>b>>p;
                cout<<"Case #"<<(i+1)<<": ";
                sets(a,b,p);
                
                if(i!=(k-1))
                            cout<<endl;
        }
     getchar();
     return 0;
}
