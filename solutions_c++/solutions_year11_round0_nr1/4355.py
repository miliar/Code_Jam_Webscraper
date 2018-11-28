#include<iostream>
#include<cmath>
using namespace std;

int nextO(char r[], int c, int n)
{
 	while(c++ < n)
 	{
         if(r[c-1]=='O')
             return (c-1);
    }
}

int nextB(char r[], int c, int n)
{	
	while(c++ < n)
 	{
         if(r[c-1]=='B')
             return (c-1);
    }
}

int main()
{	
	int t,n,p[100],tym,k;
	char r[100];
	cin>>t;
	
	for(int tc=1; tc<=t; tc++)
 	{  
 	   tym=0;
 	   cin>>n;
 	   
 	   for(int i=0;i<n;i++)
 	   {
 			 cin>>r[i]>>p[i];
	   }
	   
	   int cp=0,o[2],b[2];
	   o[0]=1;
	   b[0]=1;
	   
	   while(cp<n)
	   {
		  o[1] = p[nextO(r,cp,n)];
	   	  b[1] = p[nextB(r,cp,n)];
		  
		  //cout<<cp<<endl;
		  //cout<<"o: "<<o[0]<<" "<<o[1]; 
		  //cout<<"  b: "<<b[0]<<" "<<b[1];
		  //cout<<"\n\n"; 
		  
		  if(r[cp]=='O')
		  {
				k = abs(o[1]-o[0])+1;
				tym+=k;
				o[0]=o[1];
				
				if(abs(b[1]-b[0]) > k)
			    {
 				    if(b[1]>b[0])
	    			    b[0]+=k;
  			        else
  			            b[0]-=k;
				}
				else
				    b[0]=b[1];
		  
		  }else if(r[cp]=='B')
		  {
		   		k = abs(b[1]-b[0])+1;
				tym+=k;
				b[0]=b[1];
				
				if(abs(o[1]-o[0]) > k)
			    {
				    if(o[1]>o[0])
	    			    o[0]+=k;
  			        else
  			            o[0]-=k;
				}
				else
				    o[0]=o[1];
	   	  }
		   
 	      cp++;	  
	   }
	   
	   
	   
	   
	   cout<<"Case #"<<tc<<": "<<tym<<endl;
	   	   	   
	}
	  	   
	//system("pause");
 	return 0;
}
