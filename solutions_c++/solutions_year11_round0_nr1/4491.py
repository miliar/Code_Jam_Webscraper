
#include "robot.h"





int main( int argc, const char* argv[] )
{

	

	ifstream file( argv[1]);
	string s;

	ofstream out;
	out.open(argv[2], ios::trunc);

	getline( file, s);
	
	int T = atoi( s.c_str() );

	char * one;
	char * two;
	char * cline;

	cline = new char [s.size()+1];
	strcpy (cline, s.c_str());

	
	
	for ( int i = 0; i < T; i++)
	{
		getline( file, s);
		cline = new char [s.size() + 1];
		strcpy (cline, s.c_str() );
		
		one = strtok (cline," ");
		
		int N = atoi( one);
		
		int button[N];
		char robot[N];
		
		for ( int j = 0; j < N; j++)
		{
			one = strtok (NULL," ");
			two = strtok (NULL, " ");
			
			button[j] = atoi(two);
			robot[j] = one[0];
		}
		
		int Ostep = 0;
		int Bstep = 0;
		
		int Opos = 1;
		int Bpos = 1;
		
		int time = 0;
		

		
		while (Ostep < N || Bstep < N)
		{
			while ( Bstep < N && robot[Bstep] != 'B')
				Bstep++;
			
			while ( Ostep < N && robot[Ostep] != 'O')
				Ostep++;
			
			if ( Ostep < N)
			{
				if ( Opos != button[Ostep])
				{
					if ( Opos < button[Ostep] )
						Opos ++;
					else
						Opos --;
				}
				else if ( Ostep < Bstep)
					Ostep++;
			}
			
			if ( Bstep < N)
			{
				if ( Bpos != button[Bstep])
				{
					if ( Bpos < button[Bstep] )
						Bpos ++;
					else
						Bpos --;
				}
				else if ( Bstep < Ostep)
					Bstep++;
			}
			
			time++;
		}
		

		
		out << "Case #" << i + 1 << ": " << time << endl;
		
		
	}
	
	file.close();
	out.close();
	return 1;
}
		

