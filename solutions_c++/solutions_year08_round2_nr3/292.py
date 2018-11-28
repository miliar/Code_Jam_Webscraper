

#include <iostream>
#include <fstream>
#include <vector>


using namespace std;

void calc_perfect_deck(vector<int> &perfect_deck, int ncards)
{
	
	vector<int> remaining_indices(ncards);
	for( int i = 0; i < ncards; i++ )
	{
		remaining_indices[i] = i;
	}
	
	vector<int>::iterator iter = remaining_indices.begin();
	
	for( int count = 0; count < ncards; count++ )
	{
		for( int y = 0; y < count; y++ )
		{
			++iter;
			if( iter == remaining_indices.end() )
				iter = remaining_indices.begin();
		}
		perfect_deck[*iter] = count + 1; //count+1?
		iter = remaining_indices.erase(iter);
		//int que = *iter;
		if( iter == remaining_indices.end() )
			iter = remaining_indices.begin();
	}
	
	
}

int main()
{
	ifstream inf( "C:\\Documents and Settings\\Natxo\\Escritorio\\C-small-attempt2.in", ifstream::in );
	ofstream ouf( "C:\\Documents and Settings\\Natxo\\Escritorio\\C-small.out", ofstream::out );
	
	float ncases;
	inf >> ncases;
	
	for( int n = 0; n < ncases; n++ )
	{
		
		vector<int> indices_to_output;
		
		int ncards;
		inf >> ncards;
		
		int nindices;
		inf >> nindices;
		
		int index;
		
		for( int i = 0; i < nindices; i++ )
		{
			inf >> index;
			indices_to_output.push_back(index);
		}
		
		vector<int> perfect_deck(ncards);
		
		calc_perfect_deck(perfect_deck, ncards);
		
		/*if( n+1 == 48)
		{
			cout << nindices << endl;
			for( int i = 0; i < nindices; i++ )
				cout << indices_to_output[i] << " ";
		}*/
		
		//cout << "Case #" << n+1 << ": ";
		ouf << "Case #" << n+1 << ": ";
		
		for( int i = 0; i < nindices; i++ )
		{
			//cout << perfect_deck[indices_to_output[i]-1]<< " ";
			ouf << perfect_deck[indices_to_output[i]-1]<< " ";
		}
		
		//cout << endl;
		ouf << endl;
	}
	
	cout << "lito" << endl;
	inf.close();
	ouf.close();
	
	return 0;
}





