#include <string>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define VALID(y,x) ((y) >= 0 && (y) < H && (x) >= 0 && (x) < W)

int H, W;

bool isSink( vector< vector<int> > & M, int j, int k )
{
	if ( VALID(j,k-1) && M[j][k-1] < M[j][k] ) return false;
	if ( VALID(j,k+1) && M[j][k+1] < M[j][k] ) return false;
	if ( VALID(j-1,k) && M[j-1][k] < M[j][k] ) return false;
	if ( VALID(j+1,k) && M[j+1][k] < M[j][k] ) return false;
	return true;
}

int getDirection( vector< vector<int> > & M, vector< vector<int> > & M1, int j, int k )
{
	if ( M1[j][k] == 1 ) return 0;
	// norte, oeste, leste, sul
	int MIN = 1000000, ind = 0;
	if ( VALID(j-1,k) && M[j-1][k] < MIN ) { MIN = M[j-1][k]; ind = 1; }
	if ( VALID(j,k-1) && M[j][k-1] < MIN ) { MIN = M[j][k-1]; ind = 2; }
	if ( VALID(j,k+1) && M[j][k+1] < MIN ) { MIN = M[j][k+1]; ind = 3; } 
	if ( VALID(j+1,k) && M[j+1][k] < MIN ) { MIN = M[j+1][k]; ind = 4; }
	return ind;
}

void fillFlood( vector< vector<int> > & M, vector< vector<int> > & M2, int j, int k, int aux)
{
	M[j][k] = aux;
	if ( VALID(j-1,k) && M2[j-1][k] == 4 ) fillFlood(M, M2, j-1, k, aux);
	if ( VALID(j,k-1) && M2[j][k-1] == 3 ) fillFlood(M, M2, j, k-1, aux);
	if ( VALID(j,k+1) && M2[j][k+1] == 2 ) fillFlood(M, M2, j, k+1, aux);
	if ( VALID(j+1,k) && M2[j+1][k] == 1 ) fillFlood(M, M2, j+1, k, aux);
}

void markSinks( vector< vector<int> > & M, vector< vector<int> > & M1 )
{
	for ( int j = 0; j < H; ++j )
	{
		for ( int k = 0; k < W; ++k )
		{
			if ( isSink(M, j, k) )
			{
				M1[j][k] = 1;
			}
		}
	}
}

void markDirections( vector< vector<int> > & M, vector< vector<int> > & M1, vector< vector<int> > & M2 )
{
	for ( int j = 0; j < H; ++j )
	{
		for ( int k = 0; k < W; ++k )
		{
			M2[j][k] = getDirection(M, M1, j, k);
		}
	}
}

void doGroups( vector< vector<int> > & M, vector< vector<int> > & M1, vector< vector<int> > & M2 )
{
	int aux = 0;
	for ( int j = 0; j < H; ++j )
	{
		for ( int k = 0; k < W; ++k )
		{
			if ( M1[j][k] == 1 )
			{
				fillFlood(M, M2, j, k, aux);
				aux++;
			}
		}
	}	
}

void fixNames( vector< vector<int> > & M, vector< vector<char> > & M3 )
{
	map<int, char> table;
	char c = 'a';
	for ( int j = 0; j < H; ++j )
	{
		for ( int k = 0; k < W; ++k )
		{
			if( table.find(M[j][k]) != table.end() )
			{
				M3[j][k] = table[M[j][k]];
			}
			else
			{
				table[M[j][k]] = c;
				M3[j][k] = c;
				++c;
			}
		}
	}	
}

int main()
{
	int T;
	
	cin >> T;
	
	for ( int i = 0; i < T; ++i )
	{
		cin >> H >> W;
		vector< vector<int> > M(H, vector<int>(W)); // original
		vector< vector<int> > M1(H, vector<int>(W, 0)); // sinks
		vector< vector<int> > M2(H, vector<int>(W, 0)); // directions
		vector< vector<char> > M3(H, vector<char>(W, '*')); // final
		
		for ( int j = 0; j < H; ++j )
		{
			for ( int k = 0; k < W; ++k )
			{
				cin >> M[j][k];
			}
		}
		
		markSinks(M, M1);
		markDirections(M, M1, M2);
		doGroups(M, M1, M2);
		fixNames(M, M3);
		
		cout << "Case #" << i+1 << ":" << endl;  
		
		for ( int j = 0; j < H; ++j )
		{
			for ( int k = 0; k < W-1; ++k )
			{
				cout << M3[j][k] << " ";
			}
			cout << M3[j][M3[j].size()-1] << endl;
		}
	}

	
	return 0;
}
