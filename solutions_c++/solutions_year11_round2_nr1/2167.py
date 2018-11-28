#include <iostream>
#include <fstream>
#include <vector>
#include <string>



using namespace std;

class Fraction{
public:
	int a; 
	int b;
Fraction( int a1,int b1)
{
	a = a1;
	b = b1;
}
int getA() 
{
	return a;
}
int getB()
{
	return b;
}

};

vector<string> theArray;
vector<Fraction> winPercent;
vector<double> OWP;
vector<double> OOWP;

int main()
{
	ifstream in;
	ofstream out;

	in.open("input.txt");
	out.open("output.txt");

	int T,N;

	in >> T;
	for ( int i = 0; i < T; i++ )
	{
		in >> N;
		string temp;

		theArray.clear();
		theArray.reserve(N);
		winPercent.clear();
		OWP.clear();
		winPercent.reserve(N);
		OWP.reserve(N);
		OOWP.clear();
		OOWP.reserve(N);

		for ( int j = 0; j < N; j++)
		{
			in >> temp;
			theArray.push_back(temp);
		}
		int total;
		int wins;
		for ( int y = 0; y < N; y++)
		{
			total = 0;
			wins = 0;
			for( int u =0; u<N; u++)
			{
				if ( theArray[y][u] == '1')
				{
					total++;
					wins++;
				}
				else if( theArray[y][u] == '0')
				{
					total++;
				}
			}
			winPercent.push_back( Fraction(wins,total) );
		}
		double ftotal;
		int Tteams;
		for ( int q = 0; q< N; q++)
		{
			ftotal = 0;
			Tteams = 0;
			for ( int e = 0; e < N; e++ )
			{
				if ( theArray[q][e] == '1' )
				{
					ftotal += (double)winPercent[e].getA()/(double)((double)winPercent[e].getB()-(double)1);
					Tteams++;
				}
				else if ( theArray[q][e] == '0' )
				{
					ftotal += (double)((double)winPercent[e].getA()-(double)1)/(double)((double)winPercent[e].getB()-(double)1);
					Tteams++;
				}
			}
			OWP.push_back( ftotal/(double)Tteams);
		}
		for ( int n = 0; n < N; n++ )
		{
			ftotal = 0;
			Tteams = 0;
			for ( int s = 0; s < N; s++ )
			{
				if ( theArray[n][s] == '1'  || theArray[n][s] == '0' )
				{
					ftotal += OWP[s];
					Tteams++;
				}
			}
			OOWP.push_back( (double)ftotal/(double)Tteams);
		}
		out << "Case #" << i + 1<<":" << endl;
		for ( int d = 0; d < N; d++ )
		{
			//out << "WP:" << ((double)winPercent[d].getA()/(double)winPercent[d].getB())<<endl;
			//out << "OWP:" << OWP[d]<<endl;
			//out << "OOWP:" <<OOWP[d] <<endl;
			out << (double)((double)1/(double)4)*((double)winPercent[d].getA()/(double)winPercent[d].getB()) + (double)((double)1/(double)2) * OWP[d] + (double)((double)1/(double)4) * OOWP[d]<<endl;
		}
		
	}

}