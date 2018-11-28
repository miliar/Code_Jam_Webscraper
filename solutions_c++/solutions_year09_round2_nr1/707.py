#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>

using namespace std;

class DTree
{
public:
	DTree *left;
	DTree *right;

	string prop;
	float prob;

	~DTree()
	{
		delete left;
		delete right;
	}

	float getProb( const map<string, int>& props )
	{
		if ( prop == "" )
		{
			return prob;
		} else {
			map<string, int>::const_iterator cit;
			cit = props.find(prop);

			if (cit == props.end())
			{
				return right->getProb(props) * prob;
			} else {
				return left->getProb(props) * prob;
			}
		}
		
		return 0;
	}
};

DTree* createTree( string treeStr )
{
	DTree *node = new DTree();
	
	node->left = 0;
	node->right = 0;

	int parCount = 0;
	int start = 0;

	int child = 0;

	string in;

	for (int i = 0; i < treeStr.length(); i++)
	{
		if ( treeStr[i] == '(' )
		{
			parCount++;
			if (parCount == 2)
			{
				start = i;
				child++;
			}
		} else if (treeStr[i] == ')') {
			parCount--;

			if (parCount == 1)
			{
				DTree *nodeChild = createTree( treeStr.substr(start, i - start+1) );

				if (child == 1)
				{
					node->left = nodeChild;
				} else if (child == 2) {
					node->right = nodeChild;
				}
			}
		} else if ( parCount == 1 ) {
			in += treeStr[i];
		}
	}

	stringstream ss(in);
	
	
	ss >> node->prob;
	ss >> node->prop;


	return node;
}

int main( int argc, char** argv )
{
	ifstream fin;

	fin.open( argv[1] );

	stringstream line;

	int N;
	
	char tmp[1024];
	fin.getline(&tmp[0], 1024);
	line.str(tmp);
	line >> N;

	

	for (int caseNumber = 0; caseNumber < N; caseNumber++)
	{
		cout << "Case #" << (caseNumber + 1) << ":" << endl;

		fin.getline(&tmp[0], 1024);	

		int L;
		line.str(tmp);
		line.seekg(0);
		line >> L;

		string treeStr;

		for (int i = 0; i < L; i++)
		{
			fin.getline(&tmp[0], 1024);
			treeStr = treeStr + tmp;
		}

		DTree *tree = createTree( treeStr );
		
		
		fin.getline(&tmp[0], 1024);
		
		int A;
		line.str(tmp);
		line.seekg(0);
		line >> A;

		for (int i = 0; i < A; i++)
		{
			fin.getline(&tmp[0], 1024);
			line.str(tmp);
			line.seekg(0);

			string name;
			line >> name;

			int n;
			line >> n;

			map<string, int> props;

			for (int j = 0; j < n; j++)
			{
				string prop;
				line >> prop;

				props[ prop ] = 1;
			}
			
			float prob = tree->getProb(props);
			cout.precision(7);
			cout.setf(ios::showpoint | ios::fixed);
			//cout.setf(ios::showpos);
			cout << prob << endl;
		}

		delete tree;

		//return 0;
		//cout << tree << endl;
	}

	fin.close();

	return 0;


}