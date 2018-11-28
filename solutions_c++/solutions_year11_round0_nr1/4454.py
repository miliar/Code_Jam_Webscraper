#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>

#include <stdio.h>
using namespace std;
///////////////////////


/////////////////////
int main ()
{



 freopen("A-large.in","rt",stdin);
 freopen("A-large.out","wt",stdout);
 
int T,N,p,robb,time,ltime,ofinal,bfinal;
char temp,rob;
cin>>T;

for(int i=0;i<T;i++)
{
	cin>>N;
	
	cin>>temp;
	cin>>p;
	rob=temp;
	robb=p;
time=0;ltime=0;
time+=p;ltime+=p;

			if(temp=='O') {ofinal=p;bfinal=0;}
			if(temp=='B') {bfinal=p;ofinal=0;}

//cout<<"[first]Case of "<<temp<<" "<<p<<"   time= "<<p<<" ltime="<<ltime<<endl;

	for(int j=0;j<N-1;j++)
	{
	cin>>temp;
	cin>>p;
			if(temp==rob)
			{
				if(p>robb) 
					{
					ltime+=p-robb+1;time+=p-robb+1;
					//cout<<"[Same]Case of "<<temp<<" "<<p<<"   time= "<<p-robb+1<<" ltime="<<ltime<<endl;
					}
				else 
				{
					ltime+=robb-p+1;time+=robb-p+1;
					//cout<<"[Same]Case of "<<temp<<" "<<p<<"   time= "<<robb-p+1<<" ltime="<<ltime<<endl;
				}
			robb=p;rob=temp;
			if(temp=='O') ofinal=p;
			if(temp=='B') bfinal=p;
			
			}
			else
			
			{	if(temp=='O')
				{	
					////////////////////////////////////////////////////////////////////////////
					if(p-ofinal<=ltime && p-ofinal>=0) 
					{
					time+=1;ltime=1;robb=p;rob=temp;ofinal=p;		
					//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<1<<" ltime="<<ltime<<endl;
					}
					////////////////////////////////////////////////////////////////////////////
					 else if(p-ofinal>ltime && p-ofinal>=0) 
					{ 
					if(ofinal==0) 
						{
						time+=((p-ofinal)-ltime);
						//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<((p-ofinal)-ltime);
						ltime=((p-ofinal)-ltime);
						//cout<<" ltime="<<ltime<<endl;
						}
					else  
						{
						time+=((p-ofinal)-ltime)+1;
						//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<((p-ofinal)-ltime)+1;	
						ltime=((p-ofinal)-ltime)+1;
						//cout<<" ltime="<<ltime<<endl;
						}

 
					 robb=p;rob=temp;ofinal=p;
					}
					////////////////////////////////////////////////////////////////////////////
					 else if(ofinal-p<=ltime && ofinal-p>0) 
					{
					time+=1;ltime=1;robb=p;rob=temp;ofinal=p;		
					//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<1<<" ltime="<<ltime<<endl;
					}
					////////////////////////////////////////////////////////////////////////////
 					else if(ofinal-p>ltime && ofinal-p>0) 
 
					{
						{
						time+=((ofinal-p)-ltime)+1;
						//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<((p-ofinal)-ltime)+1;	
						ltime=((ofinal-p)-ltime)+1;
						//cout<<" ltime="<<ltime<<endl;
						}

 
					 robb=p;rob=temp;ofinal=p;
					}
					////////////////////////////////////////////////////////////////////////////
				}
				if(temp=='B')
				{	
					////////////////////////////////////////////////////////////////////////////
					if(p-bfinal<=ltime && p-bfinal>=0) 
					{
					time+=1;ltime=1;robb=p;rob=temp;bfinal=p;		
					//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<1<<" ltime="<<ltime<<endl;
					}
					////////////////////////////////////////////////////////////////////////////
					 else if(p-bfinal>ltime && p-bfinal>=0) 
					{ 
					if(bfinal==0) 
						{
						time+=((p-bfinal)-ltime);
						//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<((p-bfinal)-ltime);
						ltime=((p-bfinal)-ltime);
						//cout<<" ltime="<<ltime<<endl;
						}
					else  
						{
						time+=((p-bfinal)-ltime)+1;
						//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<((p-bfinal)-ltime)+1;	
						ltime=((p-bfinal)-ltime)+1;
						//cout<<" ltime="<<ltime<<endl;
						}

 
					 robb=p;rob=temp;bfinal=p;
					}
					////////////////////////////////////////////////////////////////////////////
					 else if(bfinal-p<=ltime && bfinal-p>0) 
					{
					time+=1;ltime=1;robb=p;rob=temp;bfinal=p;		
					//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<1<<" ltime="<<ltime<<endl;
					}
					////////////////////////////////////////////////////////////////////////////
 					else if(bfinal-p>ltime && bfinal-p>0) 
 
					{
						{
						time+=((bfinal-p)-ltime)+1;
						//cout<<"[Change]Case of "<<temp<<" "<<p<<"   time= "<<((p-bfinal)-ltime)+1;	
						ltime=((bfinal-p)-ltime)+1;
						//cout<<" ltime="<<ltime<<endl;
						}

 
					 robb=p;rob=temp;bfinal=p;
					}
					////////////////////////////////////////////////////////////////////////////
				}







			}
	}
cout<<"Case #"<<i+1<<": "<<time<<endl;
//cout<<"================================================"<<endl;
}
					
			  



return 0;

                                          
 	}

