#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
using std::vector;
using std::string;
using std::stringstream;

/*
#################################################################
#################################################################
LEXICAL ANALIZER
#################################################################
#################################################################
*/

#define TKN_NAME 'n'
#define TKN_WEIGHT 'w'

inline static bool IsAlpha(char c)
{   return (('a'<= c && c <= 'z') || ('A' <= c && c <= 'Z')); }

inline static bool IsIntDigit(char c)
{   return ('0' <= c && c <= '9'); }

inline static bool IsDigit(char c)
{   return (IsIntDigit(c) || c == '.'); }

inline static bool IsWhiteSpace(char c)
{   return (c == ' ' || c == '\t' || c == '\n' || c == '\r'); }

class TLex
{
	private:
		void SkipSpaces()
		{
			while (IsWhiteSpace(in.peek()))
				in.get();
		}

		stringstream in;
		string value;
		char token;

	public:
		TLex(const string &ss) : in(ss) {}
		~TLex() {};

		void Next()
		{
		char c;

			SkipSpaces();
			c = in.peek();
			value = "";

			if (IsIntDigit(c))
			{
				token = TKN_WEIGHT;
				while (IsDigit(in.peek()))
					value.push_back(in.get());

			}
			else if (IsAlpha(c))
			{
				token = TKN_NAME;
				while (IsAlpha(in.peek()))
					value.push_back(in.get());
			}
			else
			{
				token = in.get();
				value.push_back(token);
			}
		}

		void Match(const string &ss)
		{
			if (value == ss)
				Next();
			else
			{
				std::cerr << "expected: " << ss << " but: " << value << " found." << std::endl;
				exit(1);
			}
		}


		string Value() const
			{ return value; }
		char Token() const
			{ return token; }
};

/*
#################################################################
#################################################################
TREE
#################################################################
#################################################################
*/

template<class T>
T FromString(const string &ss)
{
stringstream strm(ss);
T t;

	strm >> t;
	return t;
}

typedef struct DTree_t
{
	string feature;
	float weight;
	struct DTree_t *first;
	struct DTree_t *second;
} DTree;

void CreateTree(DTree *&curr, TLex &l)
{
	curr = new DTree;
	curr->first = NULL;
	curr->second = NULL;

	curr->weight = FromString<float>(l.Value());
	l.Next();

	if (l.Token() == TKN_NAME)
	{
		curr->feature = l.Value();
		l.Next();
		l.Match("(");
		CreateTree(curr->first, l);
		l.Match(")");
		l.Match("(");
		CreateTree(curr->second, l);
		l.Match(")");
	}
}

void LoadTreeFromString(DTree *&root, const string &ss)
{
TLex l(ss);
int pCount;

	l.Next();
	l.Match("(");
	CreateTree(root, l);
	l.Match(")");
}

void FreeTree(DTree *&root)
{
	if (root == NULL)
		return;
	else
	{
		FreeTree(root->first);
		FreeTree(root->second);
		delete root;
	}
}

/*
#################################################################
#################################################################
ANIMAL
#################################################################
#################################################################
*/

typedef struct Animal_t
{
	float p;
	vector<string> features;

	Animal_t() { p = 1; }
} Animal;

bool AnimalHasFeature(Animal &a, const string &feature)
{
int i;

	for (i=0; i<a.features.size(); i++)
		if (a.features[i] == feature)
			return true;

	return false;
}

void CheckAnimalP(Animal &a, DTree *tree)
{
	a.p *= tree->weight;

	if ((tree->first == NULL) && (tree->second == NULL))
		return;

	if (AnimalHasFeature(a, tree->feature))
		CheckAnimalP(a, tree->first);
	else
		CheckAnimalP(a, tree->second);
}

/*
#################################################################
#################################################################
MAIN
#################################################################
#################################################################
*/

int main(int argc, char *argv[])
{
std::ifstream file;
int nCases, i;
DTree *tree;

	file.open("Ainput");
	if (!file.is_open())
	{
		std::cerr << "Error opening file Ainput" << std::endl;
		return 1;
	}

	//take the number of cases
	file >> nCases;

	for (i = 1; i <= nCases; i++)
	{
	int aux;
	string tmpLines="";

		//load the tree!
		file >> aux; //dummy
		for (; aux >= 0; aux--)
		{
		string sAux;

			std::getline(file, sAux);
			tmpLines += sAux;

		}

		LoadTreeFromString(tree, tmpLines);
        file >> aux; //number of animals;

        std::cout << "Case #"<< i <<":\n";
        for (; aux > 0; aux--)
        {
        Animal a;
        string sAux;
        int pCount;

            file >> sAux; //animal name.
            file >> pCount;
            for (; pCount > 0; pCount--)
            {
                file >> sAux;
                a.features.push_back(sAux);
            }

            CheckAnimalP(a, tree);
            printf("%.7f\n", a.p);
        }

		FreeTree(tree);
	}
	return 0;
}

