#define DATA_INPUT "A-large.in"
#define DATA_OUTPUT "A-large.out"

#include <fstream>
#include <iostream>
using namespace std;
class TreeList;
struct TreeNode;

struct TreeNode
{
	char value;
	TreeNode *next;
	TreeList *down;
};


class TreeList
{
public:
	TreeList()
		: m_size(0), m_first(NULL), m_last(NULL)
	{
	}
	
	~TreeList()
	{
		TreeNode *current, *current_t;
		current = m_first;
		while (current != NULL)
		{
			current_t = current->next;
			delete current;
			current = current_t;
		}
	}
	int CountSucc ( char **mask)
	{
		int locval = 0;
		TreeNode *tmp;
		if ( mask[1] != NULL)
		{
			char c;
			int t = 0;
			do
			{
				c = mask[0][t];
				tmp = FindSymbol ( c);
				if (tmp != NULL) 
					locval += tmp->down->CountSucc( mask + 1);
				t++;
			}
			while (mask[0][t] != '\0');
		}
		else
		{
			char c;
			int t = 0;
			do
			{
				c = mask[0][t];
				tmp = FindSymbol ( c);
				if (tmp != NULL) 
					locval ++;
				t++;
			}
			while (mask[0][t] != '\0');
		}
		return locval;
	}
	TreeNode * FindSymbol (char symbol)
	{
		TreeNode *current;
		current = m_first;
		while (current != NULL)
		{
			if (current->value == symbol) 
				return current;
			current = current->next;
		}
		return NULL;
	}

	TreeNode * AddSymbol ( char str)
	{
		if ( m_first == NULL)
			m_first = m_last = new TreeNode;
		else
		{
			m_last->next = new TreeNode;
			m_last = m_last->next;
		}
		m_last->next = NULL;
		m_last->down = new TreeList;
		m_last->value = str;
		m_size++;
		return m_last;
	}

	void AddString (char *str)
	{	
		TreeNode *temp = FindSymbol( str[0]);
		if ( temp == NULL)
			temp = AddSymbol ( str[0]);
		if ( temp != NULL && str[1] != '\0')
			temp->down->AddString (str + 1);
		return;
	}
private:
	TreeNode* m_first;
	TreeNode* m_last;
	int m_size;
};



int main()
{
	int L, D, N;
	TreeList root;
	fstream fstr;
	fstream fstrout;
	fstr.open( DATA_INPUT, fstream::in);
	if (fstr.fail ( )) cout << "fail\n"; 
	fstr >> L;
	fstr >> D;
	fstr >> N;
	char *buf = new char [ L + 1];
	fstr.getline(buf, 1);
	for (int i = 0; i < D; i++)
	{
		fstr.getline( buf, L + 1);
		root.AddString ( buf);
		//cout << buf << endl;
	}
	delete buf;
	buf = new char [ 25600];
	char **mask = new char *[L+1];
	mask [ L] = NULL;
	fstrout.open( DATA_OUTPUT, fstream::out);
	if (fstrout.fail ( )) cout << "fail\n"; 
	for (int i = 0; i < L; i++)
	{
		mask[i] = new char [27];
	}
	for (int i = 0; i < N; i++)
	{
		fstr.getline( buf, 25600);
		//cout << buf << endl;
		int cpos = 0;
		for (int j = 0; j < L; j++)
		{
			int lpos = 0;
			if ( buf[ cpos] == '(')
			{ 
				cpos++;
				while ( buf[ cpos] != ')')
				{
					mask [ j][ lpos] = buf[ cpos];
					lpos++;
					cpos++;
				}
				mask [ j][ lpos] = '\0';
				cpos++;
			}
			else
			{
				mask[j][0] = buf[ cpos];
				mask[j][1] = '\0';
				cpos++;
			}
			//cout << mask[j] << endl;			
		}
		fstrout << "Case #" << i + 1 << ": " << root.CountSucc(mask) << endl;
	}
	delete buf;
	for (int i = 0; i < L; i++)
	{
		delete [] mask[i];
	}
	delete [] mask;
	fstrout.close( );
	fstr.close( );

}