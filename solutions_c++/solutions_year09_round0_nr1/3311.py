#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <cstring>
extern "C" {
#include <stdint.h>
}

using namespace std;
int L = 0;
int D = 0;
int N = 0;


int main(int argc, char *argv[])
{
	if( argc != 2) 
	{
		cerr << "Error: Arguments incorrect" << endl;
		exit(1);
	}

	// Read Input
	string fname(argv[1]);
	ifstream ifs(fname.c_str());
	ifs >> L >> D >> N;
	string str="";
	getline(ifs,str); // Newline
	string words[D];
	for( int i = 0 ; i < D ; i++ )
	{
		getline(ifs,words[i]);
	}
	string patterns[N];
	for( int i = 0 ; i < N ; i++ )
	{
		getline(ifs,patterns[i]);
	}
	ifs.close();

	// Check Input
#if _DEBUG
	cout << "L=" << L << "\tD=" << D << "\tN=" << N << endl;
	cout << "Words:" << endl;
	for( int i = 0 ; i < D ; i++ )
	{
		cout << words[i] << endl;
	}
	cout << "Patterns:" << endl;
	for( int i = 0 ; i < N ; i++ )
	{
		cout << patterns[i] << endl;
	}
#endif

	string pat[N][L] ;
	
	for( int i = 0 ; i < N ; i++ )
	{
		str = "";
		str = patterns[i];
		int l = str.length();
		bool flag = false;
		int j = -1, k = -1;
		string s = "";
		while(j < l)
		{	
			j++;
			
			if( str[j] == '(' )
			{
				flag = true;
				s = "";
				k++;
				continue;
			}

			if( str[j] == ')' )
			{
				flag = false;
				continue;
			}

			if(flag == true)
			{
				s += str[j];
			}
			else
			{
				k++;
				s = str[j];
			}
			
			if ( (j < l) && (k < l) )
			{
				pat[i][k] = s;
			}
		} // end of while
	} // end of i loop


#ifdef _DEBUG
	cout << "Parsed Patterns:" << endl;
	for( int i = 0 ; i < N ; i++ )
	{
		for( int j = 0 ; j < L ; j++ )
		{
			cout << pat[i][j].c_str() << "\t";
		}
		cout << endl;
	}
#endif

	int64_t WP[D][N];
	memset(WP,0,D*N*sizeof(int64_t)); // Initialize
	
	for( int i = 0 ; i < D ; i++ ) // for every word
	{
		for ( int j = 0 ; j < N ; j++ ) // for every pattern
		{
			// Check for acceptance by automata
			int count = 0;
			for ( int k = 0 ; k < L ; k++ ) // for every letter
			{
				if( pat[j][k].find(words[i][k]) != string::npos )
				{
					count++;
				}
				else
				{
					break;
				}
			} // end of k loop

			if ( count == L )
			{
#ifdef _DEBUG
				cout << words[i] << " " << patterns[j] << "  Accept" << endl; 
#endif
				WP[i][j] = WP[i][j] + 1;
			}
		} // end of j loop
	} // end of i loop



#ifdef _DEBUG

	cout << "Word-Pattern Matrix:" << endl;
	for( int i = 0 ; i < D; i++ )
	{
		for( int j = 0 ; j < N ; j++ )
		{
			cout << WP[i][j] << "\t";
		}
		cout << endl;
	}
#endif


	for( int i = 0 ; i < N ; i++) // for each pattern
	{
		int64_t sum = 0;
		for( int j = 0 ; j < D ; j++ ) // for each word
		{
			sum += WP[j][i]; // sum of columns
		}
		cout << "Case #" << i+1 << ": " << sum << endl;
	}
	return 0;
}
