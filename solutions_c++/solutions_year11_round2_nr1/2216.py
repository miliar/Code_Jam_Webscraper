#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
 	int nt;
 	cin>>nt;
 	for(int i=0;i<nt;i++)
 	{
 		int n;
 		cin>>n;
 		vector<string> hold;
	 	for(int j=0;j<n;j++)
 		{
 			//find wp,owp and oowp
 			string temp;
		 	cin>>temp;
			hold.push_back(temp);	 
			 		
 		}
 		vector<double> wp;
 		vector<double> owphold;
 		for(int m=0;m<n;m++)
 		{
			int sum=0,count=0;
			for(int k=0;k<n;k++)
			{
		
		
				//for team m find the wp
				if(hold[m][k]!='.')
				{	
					count++;
					sum+=hold[m][k]-48;	
				}
				
			}
			//cout<<"sum:"<<sum<<"count:"<<count<<endl;
			wp.push_back((double)(sum)/count);
 		}
 		
 		//find the owp
 		for(int curr=0;curr<n;curr++)
 		{
 			double owp=0,count2=0;
 			for(int m=0;m<n;m++)
 			{
 				if(m!=curr&&hold[curr][m]!='.')
 				{
				count2++;
 				int sum=0,count=0;
 		//		cout<<"going on:"<<m<<endl;
 				for(int k=0;k<n;k++)
 				{
 					if(k!=curr&&hold[m][k]!='.')
 					{
 		//				cout<<"now its:"<<m<<" "<<k<<endl;
				 		sum+=hold[m][k]-48;
 						count++;		
 					}
 					
 				}
 				
				owp+=(double)sum/count;
 				}
 			}
 		//	cout<<"owp:"<<owp<<endl;
 			owphold.push_back((double)owp/count2);
	 	
 		}
 		
 		//calcuate oowp
 		vector<double> oowp;
 		for(int m=0;m<n;m++)
 		{
 			double sum=0;
			 int count=0;
 			for(int l=0;l<n;l++)
 			{
 				if(m!=l&&hold[m][l]!='.')
				{
					sum+=owphold[l]; 	
					count++;		
				}
 			}
 		//	cout<<"count:"<<count<<"sum:"<<sum<<endl;
 			oowp.push_back(sum/count);
 		}
		
		
	 	cout<<"Case #"<<i+1<<":\n";
 			for(int m=0;m<n;m++)
		 	{
		 		double RPI=0.25*wp[m]+0.50*owphold[m]+0.25*oowp[m];
		 		cout<<RPI<<endl;
		 	}
		 
	 	hold.clear();
 		wp.clear();
 		owphold.clear();
 		oowp.clear();
 	}
	
	return 0;
}
