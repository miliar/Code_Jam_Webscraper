#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<climits>
#include<map>
using namespace std;
int main()
{
	int cases;
	cin>>cases;
	for(int numCase=1;numCase<=cases;numCase++)
	{
		int n;
		cin>>n;
		//get Input!
		char **a=new char*[sizeof(char*)*n];
		for(int i=0;i<n;i++)
			a[i]=new char[sizeof(char)*n];
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cin>>a[i][j];
		
		int **b=new int*[sizeof(int*)*n];// 0 = won  , 1 = games
		for(int i=0;i<n;i++)
			b[i]=new int[sizeof(int)*2];
		
		
			
		vector<long double> WP(n);
		for(int i=0;i<n;i++)
		{
			int games=0,won=0;
			for(int j=0;j<n;j++)
			{
				if(a[i][j]=='0') games++;
				else if(a[i][j]=='1') {games++;won++;}
			}
			b[i][0]=won;
			b[i][1]=games;
			WP[i]=won/(games*1.0);

		}
		
		vector<long double> OWP(n);
		
		/*
			.11.
			0.00
			01.1
			.10.
		
		*/
		
		for(int i=0;i<n;i++)//Counting games against i 
		{
			long double owp=0.0;
			int games=0;
			for(int j=0;j<n;j++)
			{
				if( i==j) continue;
				if(a[j][i]=='0') 
				{ 
					owp+= (b[j][0]/(1.0*(b[j][1]-1)));
					games++; 
					//cout<<i<<" ---- "<<b[j][0]<< " ===================== "<<(b[j][1]-1)<<endl;
				}
				else if(a[j][i]=='1') 
				{
					if(b[j][0]!=0)
					{ 
						owp+= ((b[j][0]-1)/(1.0*(b[j][1]-1)));
					}
						
						games++;
						
						//cout<<i<<" ---- "<<b[j][0]-1<< " ===================== "<<(b[j][1]-1)<<endl;
					
				} 
				
			}
			
			OWP[i]=owp/(games*1.0);
			//cout<<OWP[i]<<" ................ "<<games<<endl;
		
		}
		
		vector<long double> OOWP(n);
		
		for(int i=0;i<n;i++)
		{
			long double oowp=0;
			for(int j=0;j<n;j++)
			if(i==j || a[i][j]=='.') continue;
			else oowp+=OWP[j];
			OOWP[i]=oowp/b[i][1];
		}	
		
		vector<long double> RPI(n);
		
		for(int i=0;i<n;i++)
		{
			RPI[i]=(0.25*WP[i])+(0.50*OWP[i])+(0.25*OOWP[i]);
		}
		
		//for(int i=0;i<n;i++)
		//cout<<OWP[i]<<" ................ "<<endl;
		cout.precision(12);
		cout<<"Case #"<<numCase<<":"<<endl;
		for(int i=0;i<n;i++)
		cout<<RPI[i]<<endl;
	}
	return 0;
}
