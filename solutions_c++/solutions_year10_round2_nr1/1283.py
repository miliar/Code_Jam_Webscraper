#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <string.h>

using namespace std;	

class Node
{
public:
	vector<Node> childs;
	string name;
	Node(const char* pName) { name = pName; }
	Node() { }
};

int mkdir(vector<char *> & tokens, int order, Node * pNode, int count)
{
	int i;

	if( order >= tokens.size() ) return count-1;
	
	for( i = 0; i < pNode->childs.size(); i++ )
		if( !strcmp(pNode->childs[i].name.c_str(), tokens[order]) ) // 이름이 같은 디렉토리가 있다면
			break;

	if( i == pNode->childs.size() )
	{
		// 이름이 같은 디렉토리가 없다면 만든다
		pNode->childs.push_back( Node(tokens[order]) );
		count++;
	}

	return mkdir(tokens, order+1, &(pNode->childs[i]), count);
}

int main(int argc, char * argv[])
{
	fstream infile, outfile;
	infile.open("A.in", ios_base::in);
	outfile.open("A.out", ios_base::out);

	int T, N, M;
	
	infile >> T; // problem size

	//

	for( int l = 0; l < T; l++)
	{
		// input 
		infile >> N >> M;

		char path[101] = "";
		
		Node root;
		root.name = "/";
		root.childs.clear();

		int sol = 0;

		for( int k = 1 ; k < N+M+1; k++ )
		{
			infile >> path;
			vector<char*> tokens;
			
			char* token = strtok(path, "/" );
			
			do
			{
				tokens.push_back( token );
				token = strtok(0, "/");
			}
			while( token );

			sol += mkdir(tokens, 0, &root, (k > N));
		}

		// output
		outfile << "Case #" << l+1 << ": " << sol << endl;
	}
	
	//

	infile.close();
	outfile.close();

	return 0;
}