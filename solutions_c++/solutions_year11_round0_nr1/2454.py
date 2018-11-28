#include<iostream> 
#include<cstdio>
#include<queue>
#include<fstream>
using namespace std;

queue<int> O;
queue<int> B;

int main()
{
	int n , t , T , N;
	int i = 0;
	int output = 0;
	char r[101];
	int p , tmp;
	int step;
	int posO , posB;

    ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");

	//scanf( "%d" , &T );
	fin >> T;
	for( t = 1 ; t <= T ; ++t )
	{
		posO = 1;
		posB = 1;
		output = 0;
		while(  !O.empty()  )
			O.pop();
		while(  !B.empty()  )
			B.pop();

		//scanf( "%d" , &N );
		fin >> N;

		for( n = 0 ; n < N ; ++n )
		{
			fin >> r[n];
			//scanf( "%d" , &p );
			fin >> p;

			if( r[n] == 'O' )
				O.push(p);
			else
				B.push(p);
		}

		for( n = 0 ; n < N ; ++n )
		{
			//cout << "O: " << posO << "  B: " << posB << endl;
			//cout << "output : " << output << endl;
			++output;	//«ö«ö¶s
			if( r[n] == 'B' )
			{
				p = B.front();
				if( p > posB )
					step = p - posB;
				else
					step = posB - p;
				posB = p;
				output += step;
				++step;
				B.pop();

				if(  !O.empty()  )
				{
					tmp = O.front();
					if( tmp == posO )
						;
					else if(   tmp > posO   )
					{
						if(   tmp - posO >= step   )
							posO += step;
						else
							posO = tmp;
					}
					else //posO > tmp
					{
						if(   posO - tmp >= step   )
							posO -= step;
						else
							posO = tmp;
					}
				}
			}
			else //if( r[n] == 'O' )
			{
				p = O.front();
				if( p > posO )
					step = p - posO;
				else
					step = posO - p;
				posO = p;
				output += step;
				++step;
				O.pop();

				if(  !B.empty()  )
				{
					tmp = B.front();
					if( tmp == posB )
						;
					else if(   tmp > posB   )
					{
						if(   tmp - posB >= step   )
							posB += step;
						else
							posB = tmp;
					}
					else //posO > tmp
					{
						if(   posB - tmp >= step   )
							posB -= step;
						else
							posB = tmp;
					}
				}
			}
			//cout << "output : " << output << endl;
		}
		//printf( "Case #%d: %d\n" , t , output );
		fout << "Case #" << t << ": " << output << endl; 
	}//end while(cin)
}
