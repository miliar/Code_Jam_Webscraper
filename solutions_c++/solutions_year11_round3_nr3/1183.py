#include<iostream>
using namespace std;

int main()
{	
	int t,l,h,p[100],n,flag,j;
	cin>>t;
	
	for(int tc=1; tc<=t; tc++)
 	{  
 	    cin>>n>>l>>h;
 	    flag=0;
 	    
		for(int i=0;i<n;i++)
 	       cin>>p[i];
 	        
        for(j=l;j<=h;j++)
 	    {   
		    for(int i=0;i<n;)
		   {   
		   	   if(j%p[i]==0 || p[i]%j==0)
                   i++;
               else
                   break;
               
               if(i==n)
                  flag=1;
		   }
		   
		   if(flag==1)
		    break;
       }
       
	   cout<<"Case #"<<tc<<": ";
	   
	   if(flag==0)
		  cout<<"NO"<<endl;
       else
          cout<<j<<endl;
	   	   	   
	}
	  	   
	//system("pause");
 	return 0;
}
