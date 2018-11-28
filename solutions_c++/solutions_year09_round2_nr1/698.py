
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <map>
#include <iostream>
using namespace std;

#define FILENAME_IN "A-large.in"
#define FILENAME_OUT "A-large.out"

struct Node
{
	float f_weight;
	std::string sFeature;

	Node* left;
	Node* right;
};

Node* main_root = NULL;
std::string sTree;

std::string::size_type iter = 0;
void ReadTree( Node*& current_root )
{
	while ( sTree[iter] == ' ' )
	{
		++iter;
	}

	std::stringstream ssWeight;
	while ( sTree[iter] != ' ' && sTree[iter] != ')' )
	{
		ssWeight << sTree[iter];

		++iter;
	}

	ssWeight >> current_root->f_weight;

	current_root->left = NULL;
	current_root->right = NULL;

	while ( sTree[iter] == ' ' )
	{
		sTree[iter];
		++iter;
	}

	if ( sTree[iter] == ')' )
	{
		++iter;
		return;
	}
	else
	{
		std::string sFeature;
		while ( (sTree[iter] != ' ') && (sTree[iter] != '(') && (sTree[iter] != ')') )
		{
			sFeature += sTree[iter];
			++iter;
		}

		current_root->sFeature = sFeature;
		current_root->left = new Node();
		current_root->right = new Node();

		while ( sTree[iter] != '(' )
		{
			++iter;
		}
		++iter;

		ReadTree( current_root->left );

		while ( sTree[iter] != '(' )
		{
			++iter;
		}
		++iter;

		ReadTree( current_root->right );
	}
}

void DeleteTree( Node*& root )
{
	if ( root == NULL )
	{
		return;
	}

	DeleteTree( root->left );
	DeleteTree( root->right );

	delete root;
	root = NULL;
}

typedef std::map< std::string, int > Features;

float Probability( float fProb, Node* root, Features mapFeatures )
{
	if ( root == NULL )
	{
		fProb;
	}

	if ( root->sFeature.empty() )
	{
		return fProb * root->f_weight;
	}

	if ( mapFeatures.find( root->sFeature ) != mapFeatures.end() )
	{
		return Probability( fProb * root->f_weight, root->left, mapFeatures );
	}
	else
	{
		return Probability( fProb * root->f_weight, root->right, mapFeatures );
	}
}

int main()
{
	ifstream fin( FILENAME_IN );
	if ( !fin )
	{
		return 1;
	}

	ofstream fout( FILENAME_OUT );
	if ( !fout )
	{
		return 1;
	}


	int N = 0;
	fin >> N;
	fin.ignore();

	std::string sBuffer;
	sBuffer.reserve( 90 );
	for ( int i = 0; i < N; ++i )
	{
		fout << "Case #" << (i+1) << ":" << std::endl;

		int L = 0;
		fin >> L;
		fin.ignore();

		sTree.clear();
		main_root = new Node();
		for( int j = 0; j < L; ++j )
		{
			getline( fin, sBuffer );
			sTree += sBuffer;
		}

		iter = 0;
		while ( sTree[iter] != '(' )
		{
			++iter;
		}
		++iter;
		while ( sTree[iter] == ' ' )
		{
			++iter;
		}

		ReadTree( main_root );

		int A = 0;
		fin >> A;
		fin.ignore();

		for ( int k = 0; k < A; ++k )
		{
			Features mapFeatures;

			std::string sAnimal;
			int n = 0;
			std::string sFeature;

			fin >> sAnimal;
			fin >> n;

			for ( int k = 0; k < n; ++k )
			{
				fin >> sFeature;
				mapFeatures.insert( std::make_pair( sFeature, 1  ) );
			}

			float fProb = Probability( (float)1.0, main_root, mapFeatures );

			fout << setprecision( 7 ) << fixed << fProb << std::endl;
		}

		DeleteTree( main_root );
	}


	fout.close();
	fin.close();

	return 0;
}
