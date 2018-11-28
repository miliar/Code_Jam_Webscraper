#include <fstream>
#include <iostream>
#include <vector>


using namespace std;
ifstream inp("c:\\B-large.in");
ofstream out("c:\\gcj\\no2.out");


void process(int t)
{
	int N,S,p;
	inp >> N >> S >> p;
	int ret = 0;
	for ( int i = 0; i < N; i++)
	{
		
		int score;
		inp >> score;
		
		int p1 = p-1;
		if ( p1 < 0 ) p1 = 0;
		int p2 = p1-1;
		if ( p2 < 0 ) p2 = 0;
		
		if ( score >= p + p1 + p1 ) ret ++;
		else
		if ( S > 0 && score >= p + p2 + p2)
		{
			S--;
			ret++;
		}
	}
	
	out<<"Case #"<<t+1<<": "<<ret<<endl;
 
}

int main()
{
	int T;
	inp >> T;
	for ( int t = 0; t < T; t++)
	{
		process(t);
		
	}
}