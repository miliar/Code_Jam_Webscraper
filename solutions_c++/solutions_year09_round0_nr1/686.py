#include<iostream>
#include<vector>
using namespace std;

class node_class
{
public:
	bool exists[26];
	char letter;
	node_class* pointers[26];
	node_class()
	{
		for(int i=0;i<26;i++)
			exists[i]=false;
		letter = ' ';
	}
};

void deltree(node_class* ptr)
{
	for(int i=0;i<26;i++) {
		if ( ptr->exists[i] )
			deltree(ptr->pointers[i]);
	}
	delete ptr;
}

node_class* root;
int L,D,N;
int counter ;
vector< vector<char> > word;

void calc(node_class* ptr, int letter)
{
	if ( letter == L ) {
		counter++;
		return ;
	}
	int nsize = word[letter].size();
	for(int i=0; i<nsize;i++) {
		if ( ptr->exists[ word[letter][i] - 'a' ] )
			calc(ptr->pointers[ word[letter][i] - 'a' ],letter+1);
	}
}

int main()
{
	cin >> L >> D >> N;
	root = new node_class();

	for(int i=0;i<D;i++) {
		node_class* ptr = root;
		char input[1000];
		cin >> input ;
		for(int j=0;j<L;j++) {
			if ( ptr->exists[ input[j] - 'a' ] ) {

			}
			else {
				ptr->exists[ input[j] - 'a' ] = true;
				ptr->pointers[ input[j] - 'a' ] = new node_class();
				ptr->pointers[ input[j] - 'a' ]-> letter = input[j] ;
			}
			ptr = ptr->pointers[ input[j] - 'a' ];
		}
	}


	for(int i=0;i<N;i++) {
		word = vector< vector<char>>(L);
		char input[3000];
		cin >> input;
		int j=0;
		int inputsize = strlen(input);
		for(int k=0; k<inputsize; k++) {
			if ( input[k] == '(' ) {
				k++;
				while( input[k] != ')' ) {
					word[j].push_back(input[k]);
					k++;
				}
			}
			else {
				word[j].push_back(input[k]);
			}
			j++;
		}
		counter = 0;
		calc(root,0);
		cout << "Case #"<<i+1<<": "<<counter <<endl;


	}

	deltree(root);
}