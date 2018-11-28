#include <iostream.h>
#include <fstream.h>
#include <vector>




#define VECTOR_SIZE 1000
#define MAXLEN 1000

long int N, P, Q, X, C;


int i,j;

int sum;

char sLine[MAXLEN];

int cells[10000];

ifstream inFile;

vector<int> sequence;

vector<int>::iterator itera,iterb;



int main(int argc, char* argv[])
{
	if ( argc < 2 )
	{
		inFile.open("C-test.in");
	}
	else
	{
		inFile.open(argv[1]);
	}
	
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	
	
	inFile >> N;
	inFile.getline(sLine,MAXLEN);
	
	
	for (X=0;X<N;X++)
	{
		inFile >> P;
		inFile >> Q;
		inFile.getline(sLine,MAXLEN);
		
		C = 0;
		
		sequence.clear();
		
			
		for (i=0;i<Q;i++)
		{
			inFile >> j;
			sequence.push_back(j);
		}
		

		
		inFile.getline(sLine,MAXLEN);
		
		itera = sequence.begin();
		iterb = sequence.end();
		sum = 0;
		C = 1000000;
		do
		{
		/*
			cout << " seq: ";
			for ( itera = sequence.begin();itera!=sequence.end();itera++ )
			{
				cout << *itera;
				cout << " ";
			}
			cout << endl;
			*/
			for (i=0;i<10000;i++)
				cells[i] = 1;
			
			sum = 0;
			
			for ( itera = sequence.begin();itera!=sequence.end();itera++ )
			{
			/*
				cout << "sequence: ";
				for ( iterb = sequence.begin();iterb!=sequence.end();iterb++ )
				{
					cout << *iterb;
					cout << " ";
				}
				cout << endl;
				*/
				cells[(*itera)-1] = 0;
				
				/*
				for ( i=0;i<P;i++ )
				{
					cout << "i=" << i << "  cell[i]=" << cells[i] << endl;
				}
				*/
				
				for ( i=(*itera);i<P;i++ )
				{
					if ( cells[i] == 1 )
					{
						sum++;
					}
					if ( cells[i] == 0 )
						break;
				}
				for ( i=(*itera)-2;i>=0;i-- )
				{
					if ( cells[i] == 1 )
					{
					
						sum++;
					}
					if ( cells[i] == 0 )
						break;
				}
				//cout << "sum=" << sum << endl;
			}
			if ( sum < C )
					C = sum;
		} while ( next_permutation( sequence.begin(), sequence.end() ) );
		
		
		cout << "Case #" << X+1 << ": " << C << endl;

	}
	
	inFile.close();
	return 0;
}