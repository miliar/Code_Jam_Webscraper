#include <iostream>
#include <fstream>
#include <string>
 
#include <windows.h>
using namespace std;
const int MAX_TEAMS = 100;
void CalcRPI(int line ,ifstream& input ,ofstream& output);
int main()
{
	long start = GetTickCount();
	ifstream input("A-large.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("A-large.out",ios::out);
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;
	
	int i =0;
	for (i=0;i<lines;i++)
	{
		CalcRPI(i ,input,output);
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	system("pause");
	return 0;
}
void CalcRPI(int line ,ifstream& input ,ofstream& output)
{
	int teams ,i, j , k;
	input>> teams ;
	char scores[MAX_TEAMS][MAX_TEAMS];
	for(i=0; i<teams ; i++)
		for(j=0; j<teams ; j++)
		{
			input>>scores[i][j];
		}

	float WP[MAX_TEAMS] ;
	float gameAcount =0, points =0 ;
	for(i=0 ;i<teams ;i++)
	{
		gameAcount= 0 ;
		points= 0;
		for(j=0; j<teams ; j++)
		{
			if(scores[i][j] !='.')
			{
				gameAcount +=1.0;
				points +=  (scores[i][j]-'0') ;
			}
		}
		WP[i] = points/gameAcount;
		//cout<<WP[i]<<"\n";
	}

	float OWP[MAX_TEAMS] ;
	float compAcount = 0;
	float sum = 0;
	for(i=0 ;i<teams ;i++)
	{
		compAcount =0;
		sum= 0;
		//考察哪些球队与当前球队比过赛
		for(j=0; j<teams ; j++)
		{
			//球队j与当前队比过赛，那么考察球队j的WP，但是是除了与i比赛战绩的WP
			if(scores[i][j] !='.')
			{
				compAcount +=1.0 ;
				gameAcount =0 ;
				points = 0;
				for(k=0 ;k<teams ;k++)
				{
					if(k!=i &&k!=j &&scores[j][k]!='.' )
					{
						gameAcount +=1.0;
						points +=  (scores[j][k]-'0') ;
					}				
				}//end of for 将球队j的新WP算出来了
				sum +=  (points/gameAcount);
			}//end of if
		}
		OWP[i] = sum/compAcount ;
	}

	float OOWP[MAX_TEAMS] ;
	float compOWPs =0 ;
	for(i=0;i<teams ;i++)
	{
		compAcount = 0;
		compOWPs = 0;
		for(j=0;j<teams ; j++)
		{
			if(scores[i][j] !='.')
			{
				compAcount+= 1.0;
				compOWPs += OWP[j] ;
			}
		}
		OOWP[i] = compOWPs/compAcount ;
		
	}

	float RPI[MAX_TEAMS] ;
	output<<"Case #"<<line+1<<": \n";
	for(i=0 ;i<teams ;i++)
	{
		RPI[i] = 0.25 *WP[i] +0.50*OWP[i] +0.25*OOWP[i] ;
		output<<RPI[i]<<"\n";
	}
}