#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>

#include <stdio.h>
using namespace std;
///////////////////////

//#define SMALL
#define LARGE

/////////////////////
int main ()
{

///////////////////////////
 
#ifdef SMALL
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif

//////////////////////////

 cout.precision(12);
int T,c,N,i,j,k,l;
float wp[100],wpp[100],owp[100];
char map[10000];
float win[100],tot[100],tott,num;
	
float numm,tottt,owpp[100];
float rpi;

cin>>T;

	for(  c=0;c<T;c++)
	{
		 cin>>N;
		for(i=0;i<N;i++)
		{
		win[i]=0;tot[i]=0;
			for(j=0;j<N;j++)
			{
			cin>>map[(i*N)+j];
			if(map[(i*N)+j]!='.') tot[i]++;
			if(map[(i*N)+j]=='1') win[i]+=1;
			
			
			}
		//cout<<"tot["<<i+1<<"]= "<<tot[i]<<"  and win["<<i+1<<"]= "<<win[i]<<endl;	
		if(tot[i]!=0) wp[i]=win[i]/tot[i];
		//cout<<"wp["<<i+1<<"]= "<<wp[i]<<endl;		
		}
		//cout<<"============================================"<<endl;




		for(i=0;i<N;i++)
		{
		num=0;tott=0;
			for(j=0;j<N;j++)
			{


    				if(map[(i*N)+j]!='.' && j!=i)
				{
 
							{num++;
							if(map[(j*N)+i]=='1') wpp[j]=(win[j]-1)/(tot[j]-1);
							if(map[(j*N)+i]=='0') wpp[j]=(win[j])/(tot[j]-1);
							tott+=wpp[j];
							//cout<<"wpp["<<j+1<<"]= "<<wpp[j]<<endl;					
							}
						 		
 				}
			}
		
			owp[i]=tott/num;
			//cout<<"owp["<<i+1<<"]= "<<owp[i]<<endl;

		}

	
		for(i=0;i<N;i++)
		{tottt=numm=0;	
			for(j=0;j<N;j++)
			{
				if(map[(i*N)+j]!='.' && j!=i)
				{tottt+=owp[j];numm++;}
			}
		owpp[i]=tottt/numm;
		}



cout<<"Case #"<<c+1<<":"<<endl;
		for(i=0;i<N;i++)
		{
		   rpi = (0.25 * wp[i] )+( 0.50 * owp[i]) +( 0.25 * owpp[i]);
			cout<<rpi<<endl;
		}


	}
					
				  



return 0;
   	
}

