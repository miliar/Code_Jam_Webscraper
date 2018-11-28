#include<fstream>
#include<cmath>
using namespace std;

int main()
{
	int T , N ,P, Otime, Btime , Opos , Bpos , max;
	double  time;
	char c;
	ifstream in; 
	in.open( "in.txt" );
	ofstream out;
	out.open( "out.txt" );
	in >>T;
	for ( int i=0 ; i < T ; i++ )
	{
		Otime = 0;  Opos = 1; Btime = 0; Bpos = 1 ; max=0;
		in>>N;
		for ( int j=0; j < N ; j++ )
		{
			in >> c>>P;
			if ( c == 'O' )
			{
				time = P-Opos;
				time = fabs ( time );
				time+=1;
				Opos = P;
				Otime+=time;
				if ( Otime <= max )
				{max++; Otime = max;}
				else
					max = Otime;
			}
			else
			{
				time = P-Bpos;
				time = fabs ( time );
				time+=1;
				Bpos = P;
				Btime+=time;
				if ( Btime <= max )
				{ max++; Btime = max;}
				else
					max = Btime;
			}
		}
		out<<"Case #"
			<<i+1<<": "
			<<max<<'\n';
	}
	in.close();
	out.close();
	return 0;
}