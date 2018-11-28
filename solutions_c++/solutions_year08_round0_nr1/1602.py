#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.txt");
	int N;
	fin>>N;
	for(int i=0;i<N;i++)
	{
		int n_se,n_qe;
		
		fin>>n_se;
		fin.ignore();
		string *engine = new string[n_se];
		
		for(int j=0;j<n_se;j++)
		getline(fin,engine[j]);
		
		fin>>n_qe;
		fin.ignore();
		string *query = new string[n_qe];
		
		for(int j=0;j<n_qe;j++)
		getline(fin,query[j]);
		
		int rank=0;
		string current;
		current=engine[0];
		for(int j=0;j<n_se;j++)
		{
			for(int k=0;k<n_qe;k++)
			{
				if(query[k]==engine[j])
				{
					if(k>rank)
					{
						current=engine[j];
						rank=k;
					}
					break;
				}
				if(k==n_qe-1)
				{
					current=engine[j];
					rank=n_qe;
				}
			}
		}
		
		
		int pos=0,switches=0;
		while(pos<n_qe)
		{
			if(current==query[pos])
			{
				switches++;
				for(int j=0;j<n_se;j++)
				{
					for(int k=pos;k<n_qe;k++)
					{
						if(query[k]==engine[j])
						{
							if(k>rank)
							{
								current=engine[j];
								rank=k;
							}
							break;
						}
						if(k==n_qe-1)
						{
							current=engine[j];
							rank=n_qe;
						}
					}
				}
			}	
			pos++;
		}			
		fout<<"Case #"<<i+1<<": "<<switches<<endl;
	}
		
    fout<<endl;
    
    return 0;
}
