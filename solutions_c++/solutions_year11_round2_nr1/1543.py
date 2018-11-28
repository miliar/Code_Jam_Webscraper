#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

const string inputFile = "A-small-attempt0.in";


int main()
{
	
	ifstream input;
	input.open(inputFile.c_str());
	int T;
	input>>T;
	ofstream output;
	output.open((inputFile+".out").c_str());

	double* WP = new double[101];
	double** OWP = new double*[101];
	double* OOWP = new double[101];
	char** score = new char*[101];
	double * finalOWP = new double[101];
	
	for(int i=1; i<=100; i++)
	{
		OWP[i] = new double[101];
	//	OOWP[i] = new double[101];
		score[i] = new char[101];
	}
	
	for(int t=1; t<=T; t++)
	{int N;
		input>>N;
		
		
		for(int n1=1; n1<=N; n1++)
		{
			WP[n1] = 0;
				OOWP[n1]= 0;
				finalOWP[n1]=0;
			for(int n2=1; n2<= N; n2++)
			{
				OWP[n1][n2] =0;
			
				score[n1][n2] = 0;
			}
		}
		
		
		for(int n1=1; n1<=N; n1++)
		{
			for(int n2=1; n2<= N; n2++)
			{
				input>>score[n1][n2];
			}
		}
		
		
		for(int n1=1; n1<=N; n1++)
		{
			int numOfGames = 0;
			for(int n2=1; n2<= N; n2++)
			{
				if(score[n1][n2]=='1')
				{
						WP[n1]++;
						numOfGames++;
				}
				else if(score[n1][n2]=='0')
				{
					numOfGames++;
				}
			}
		
		
			// OWP[n1][n2]  n2*s winning percentage against n1
				for(int n2=1; n2<= N; n2++)
				{
				//	cout<<n1<<" -M"<<score[n1][n2]<<endl;
					if(score[n1][n2]=='1')
					{
							OWP[n2][n1] = (WP[n1]-1)/double(numOfGames-1);
						//	cout<<" ---"<<WP[n1]<<" "<<numOfGames<<" "<<OWP[n2][n1]<<endl;
					}
					else if(score[n1][n2]=='0')
					{
							OWP[n2][n1] = (WP[n1])/double(numOfGames-1);
					}
				}
				
				WP[n1]/=double(numOfGames);
			
		}
		
		
		
		
		
		for(int n1=1; n1<=N; n1++)
		{
			int numOfGames = 0;
			 
			for(int n2=1; n2<= N; n2++)
			{
				if(score[n1][n2]!='.')
				{
						numOfGames++;
						finalOWP[n1]+=OWP[n1][n2];
					//	cout<<finalOWP[n1]<<"    -- "<<OWP[n1][n2]<<endl;
				}
			}
			finalOWP[n1]/=double(numOfGames);		
		}
		
		
		for(int n1=1; n1<=N; n1++)
		{
			int numOfGames = 0;
		
			for(int n2=1; n2<= N; n2++)
			{
				if(score[n1][n2]!='.')
				{
						numOfGames++;
						OOWP[n1] += finalOWP[n2];
				}
			}
			OOWP[n1]/=numOfGames;		
		}
		output<<"Case #"<<t<<":"<<endl;
		for(int n=1; n<=N; n++)
		{
		//	cout<<WP[n]<<" "<<finalOWP[n]<<" "<<OOWP[n]<<endl;
			output<<0.25*WP[n]+0.5*finalOWP[n]+0.25*OOWP[n]<<endl;
		}
	}
					
	

	return 0;
}
