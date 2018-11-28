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



 freopen("c.in","rt",stdin);
freopen("c.out","wt",stdout);
 
int T,N,p;

int i,j,k,z,counter,c[1000], t,sum;
int poss,max=-1;
int a,b[100];
int t1,t2,sum1,sum2; 
int M;
 
int test;
cin>>T;

for(int test=0;test<T;test++)
{
max=-1;
		cin>>N;
		for(int i=0;i<N;i++)
		cin>>c[i];








	//split to 1 and N-1

	for(k=0;k<N;k++)
	{t=0;sum=0;
	//cout<<"case of chosen "<<c[k]<<endl;

			for(j=0;j<N;j++)
			{ 
				if(j!=k) 
				{t^=c[j];
				 sum+=c[j];
				}
			}
		//cout<<"actual sum= "<<sum<<" predict sum="<<t<<endl;

		if(t==c[k]) 
		{
			 
				 
				if(sum>c[k]) poss=sum;
				else poss=c[k]; 
			if(poss>max) max=poss;
			 
		
		//cout<<"sean wins= "<<poss<<endl;
		 
		}
	}

	/*
	//split to 2 and N-2

	for(a=0;a<N;a++)
	{
		for(b=a+1;b<N;b++)
		{
	//Pile 1
				cout<<"case of chosen "<<c[a]<<" and "<<c[b]<<endl;
					{t1=c[a]^c[b]; sum1=c[a]+c[b];}
				cout<<"actual sum of pile1= "<<sum1<<" predict sum of pile1 ="<<t1<<endl;
			
	//Pile 2
				t2=0;sum2=0;

				for(j=0;j<N;j++)
				{ 
					if(j!=a && j!=b) 
					{t2^=c[j];
					 sum2+=c[j];
					}
				}
			cout<<"actual sum of pile2= "<<sum2<<" predict sum of pile2 ="<<t2<<endl;

			if(t1==t2) 
			{
				if(sum1>sum2) poss=sum1;
				else poss=sum2;

				if(poss>max) max=poss;
			cout<<"sean wins= "<<poss<<endl;
			 
			}
	 
		} 
	}





	//split to 3 and N-3
	int d;
	 
	for(a=0;a<N;a++)
	{
		for(b=a+1;b<N;b++)
		{

			for(d=b+1;d<N;d++)
			{
	//Pile 1
				cout<<"case of chosen "<<c[a]<<" and "<<c[b]<<" and "<<c[d]<<endl;
					{t1=c[a]^c[b]^c[d]; sum1=c[a]+c[b]+c[d];}
				cout<<"actual sum of pile1= "<<sum1<<" predict sum of pile1 ="<<t1<<endl;
			
	//Pile 2
				t2=0;sum2=0;

				for(j=0;j<N;j++)
				{ 
					if(j!=a && j!=b && j!=d) 
					{t2^=c[j];
					 sum2+=c[j];
					}
				}
				cout<<"actual sum of pile2= "<<sum2<<" predict sum of pile2 ="<<t2<<endl;

				if(t1==t2) 
				{
					if(sum1>sum2) poss=sum1;
					else poss=sum2;
					if(poss>max) max=poss;
				cout<<"sean wins= "<<poss<<endl;
			
				}
			}
	 
		} 
	}


	*/
	int cond;
	int it[100],d;
	int final=( (int)N/2 )-1;
	for(M=1;M<=final;M++)
	{
	//cout<<"Number of nesting(pile1 pieces) = "<<M+1<<endl;

			for(b[0]=0;b[0]<N;b[0]++)
			{
			
				counter=1;it[counter]=1;
				j:for(b[counter]=b[counter-1]+it[counter];b[counter]<N;b[counter]++)

				{

				if(counter<M) { counter++;it[counter]=1;goto j;}
			
				//Pile 1
						//cout<<"case of chosen ";
						//for(z=0;z<counter;z++)
						//cout<<c[b[z]]<<" and ";
						//cout<<c[b[counter]]<<endl;
	//////////////////////////////////



	//Pile 1
				 
					 
					t1=0;sum1=0;
					for(z=0;z<counter;z++) {t1^=c[b[z]]; sum1+=c[b[z]];}
					//cout<<"actual sum of pile1= "<<sum1<<" predict sum of pile1 ="<<t1<<endl;
			
	//Pile 2
				t2=0;sum2=0;

				for(j=0;j<N;j++)
				{ 
				cond=1;
				for(z=0;z<counter;z++)  cond= cond && (j!=b[z]);
					if(cond) 
					{t2^=c[j];
					 sum2+=c[j];
					}
				}
				//cout<<"actual sum of pile2= "<<sum2<<" predict sum of pile2 ="<<t2<<endl;

				if(t1==t2) 
				{
					if(sum1>sum2) poss=sum1;
					else poss=sum2;
					if(poss>max) max=poss;
				//cout<<"sean wins= "<<poss<<endl;
				}
	//////////////////////////////////////////




	 




	for(d=counter-2;d>=0;d--)
	 if(b[counter-d]==N-1-d ) {counter-=(1+d); it[counter]++; goto j;}

				//Pile 2
				}
			}
	}
	
			 

	//cout<<"========================================================="<<endl;
	//cout<<"Max earn= "<<max<<endl;

if(max==-1)
cout<<"Case #"<<test+1<<": "<<"NO"<<endl;
else
cout<<"Case #"<<test+1<<": "<<max<<endl;

}



  

 
return 0;

                                          
 	}

