#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
int getter(int ,int);
int checker(int,int ,int);
int power(int ,int);
int main()
{
     
    freopen( "inp.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	int t,i,j;
	vector<int>a,b;
	
	cin>>t;
	for(i=0;i<t;i++)
	{
             cin>>j;
             a.push_back(j);
             cin>>j;
             b.push_back(j);
            
    }
    for(i=0;i<t;i++)
    {
    cout<<"Case #"<<i+1<<": "<<getter(a[i],b[i]);
    cout<<endl;
    }

        
	
 return 0;
                        
}                    



int getter(int a,int b)
{
     int t,s=0;
     for(int i=a;i<=b;i++)
     {
             t=checker(i,a,b);
             
             s=s+t;
     }
     return s;
}

                  
int checker(int i,int a,int b)
{
 int r,c=0,z=a,l=0,t,x,counter=0;
     while(z!=0)
     {
             c++;
             z=z/10;
     }
     r=c;
     z=i;
     t=0;
     while(c>=0)
     {          
                l=l+(z%10)*power(10,t);
                z=z/10;
                c--;
                t++;
                x=(l*power(10,c))+z;
                if(x<=b && x>=a && x!=i)
                {
                        
                        if(x>i)
                        counter++;
                        
                        
                        
                } 
     }
     return counter;
 }
 int power( int a,int b)
 {
     int z=1;
     for(int i=1;i<=b;i++)
     {
           z=z*10;
     }
     return z;
 }  
                   
                               
                  
	
	
