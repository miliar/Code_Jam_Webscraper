#include <iostream.h>
#include <fstream.h>

// Code Jam 2011
// Round 1 B
// A. RPI



int main(int argc, char *argv[])
{
	int T,t;
	int N,n;
	
	float RPI;
	float WP;
	float OWP;
	float OOWP;
	
	
	
	float OWPlist[100];
	float WPlist[100];
	
	char roster[100][100];
	
	int wins;
	int played;
	
	int otherwins;
	int otherplayed;
	
	int opponents;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		inFile >> N;
		
		for (n=0;n<N;n++)
		{
			for ( int nn=0;nn<N;nn++)
			{
				inFile >> roster[n][nn];
			}
		}
		
		for ( n=0;n<N;n++ )
		{
			wins = 0;
			played = 0;
			
			for ( int nn=0;nn<N;nn++)
			{
				if ( roster[n][nn] == '1' )
				{
					wins++;
					played++;
				}
				else if ( roster[n][nn] == '0' )
				{
					played++;
				}
			}
			WP = (float)wins/played;
			WPlist[n] = WP;
			//cout << "WP: " << WP << endl;
			
			OWP = 0.0f;
			
			opponents = 0;
			
			// calc OWP
			for ( int nn=0;nn<N;nn++)
			{
				// skip self..
				if ( nn==n )
					continue;
				
				// is opponent ?
				if ( roster[nn][n] == '.' )
					continue;
				
				opponents++;
				otherwins = 0;
				otherplayed = 0;
				for (int mm=0;mm<N;mm++)
				{
					// skip match vs self
					if ( mm==n )
						continue;
					if ( roster[nn][mm] == '1' )
					{
						otherwins++;
						otherplayed++;
					}
					else if ( roster[nn][mm] == '0' )
					{
						otherplayed++;
					}
				}
				OWP = OWP + (float)otherwins/otherplayed;
				
			}
			
			OWP = OWP/opponents;
			
			OWPlist[n] = OWP;
			
			//cout << "OWP: " << OWP << endl;
			
		}
		
		cout << "Case #" << t+1 << ":" << endl;
		for (n=0;n<N;n++)
		{
			OOWP = 0.0f;
			opponents = 0;
			for (int i=0;i<N;i++)
			{
				if ( roster[n][i] != '.' )
				{
					OOWP = OOWP + OWPlist[i];
					opponents++;
				}
			}
			OOWP = OOWP/opponents;
			
			RPI = 0.25f * WPlist[n] + 0.50f * OWPlist[n] + 0.25f * OOWP;
		
			cout << RPI << endl;
		}
		

		
	}
		
		
	
	inFile.close();
	return 0;
}