#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;


int main (int argc, char * const argv[]) {
    
	string WELC="welcome to code jam";
	
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
		
	int T;
	INP>>T;
	
	for(int c=0;c<T;c++)
		{
		int H,W;
		INP>>H>>W;
		
		vector<vector<int> > aus(H,vector<int>(W,0));
		
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				aus[i][j]=W*i+j;
		
		vector<vector<int> > mapp(H,vector<int>(W,0));
		
		for(int i=0;i<H;i++)
			for(int j=0;j<W;j++)
				INP>>mapp[i][j];
			
		cout<<"MAPPA"<<endl;
			for(int i=0;i<H;i++)
			{
			for(int j=0;j<W;j++)
				cout<<mapp[i][j];
			cout<<endl;
			}
		cout<<endl;	
		for(int cont=0;cont<10000;cont++)
			{
			
			for(int i=0;i<H;i++)
				for(int j=0;j<W;j++)
				{
					int mini=20000;
					int cellmin=0;
					
					if(i>0)
						{
						if(mapp[i-1][j]<mapp[i][j])
							{
							cellmin=1;
							mini=mapp[i-1][j];
							}
						}
					if(j>0)
						{
						if(mapp[i][j-1]<mapp[i][j] and mapp[i][j-1]<mini)
							{
							cellmin=2;
							mini=mapp[i][j-1];
							}
						}
					
					if(j<W-1)
						{
						if(mapp[i][j+1]<mapp[i][j] and mapp[i][j+1]<mini)
							{
							cellmin=3;
							mini=mapp[i][j+1];
							}
						}
									
					if(i<H-1)
						{
						if(mapp[i+1][j]<mapp[i][j] and mapp[i+1][j]<mini)
							{
							cellmin=4;
							mini=mapp[i+1][j];
							}
						}
					
					
					
					if(cellmin==1)
						{
						int k=min(aus[i-1][j],aus[i][j]);
						
						aus[i-1][j]=k;
						aus[i][j]=k;
						}
					if(cellmin==2)
						{
						int k=min(aus[i][j-1],aus[i][j]);
						
						aus[i][j-1]=k;
						aus[i][j]=k;
						}
					if(cellmin==3)
						{
						int k=min(aus[i][j+1],aus[i][j]);
						
						aus[i][j+1]=k;
						aus[i][j]=k;
						}
					if(cellmin==4)
						{
						int k=min(aus[i+1][j],aus[i][j]);
						
						aus[i+1][j]=k;
						aus[i][j]=k;
						}
			
				}
			
			
			}
		
		map<int, char> corr;
		char part='a';
		
		set<int> used;
		
		for(int i=0;i<H;i++)
			{
			for(int j=0;j<W;j++)
				{
				if(used.find(aus[i][j])!=used.end())
					continue;
				else
					{
					used.insert(aus[i][j]);
					corr[aus[i][j]]=part;
					part++;
					}
				
				}
			}
		
		vector<vector<char> >real(H,vector<char>(W,' '));
		
		for(int i=0;i<H;i++)
			{
			for(int j=0;j<W;j++)
				{
				real[i][j]=corr[aus[i][j]];
				
				}
			}
		OUT<<"Case #"<<c+1<<": "<<endl;
		for(int i=0;i<H;i++)
			{
			for(int j=0;j<W;j++)
				{
				OUT<<real[i][j]<<" ";
				
				}
			OUT<<endl;
			}
		
		}
		
		
	
	
    return 0;
}
