#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Node
{
	double p;
	string feature;
	Node *yes, *no;
};

void parse(Node *n, ifstream &f)
{
	char q;
	f.read(&q,1);
	f >> n->p;
	n->feature = "";
	while(f.peek() == ' ' || f.peek() == '\n')
		f.read(&q,1);
	if(f.peek() != ')')
	{
		f >> n->feature;
		while(f.peek() == ' ' || f.peek() == '\n')
			f.read(&q,1);
		n->yes = new Node;
		parse(n->yes, f);
		while(f.peek() == ' ' || f.peek() == '\n')
			f.read(&q,1);
		n->no = new Node;
		parse(n->no, f);
		while(f.peek() == ' ' || f.peek() == '\n')
			f.read(&q,1);
	}
	f.read(&q,1);
}

double gogo(Node *n, const vector<string> &v)
{
	double ret = n->p;
	if(n->feature != "")
	{
		if(find(v.begin(), v.end(), n->feature) != v.end())
			ret *= gogo(n->yes, v); 
		else
			ret *= gogo(n->no, v); 
	}
	return ret;
}

int main()
{
	ifstream f;
	ofstream o;
	f.open("Asmall2.txt");
	o.open("Aout.txt");
	o.precision(10);
	int N;
	f >> N;
	for(int i = 0; i < N; i++)
	{
		o << "Case #" << (i+1) << ":" << endl;
		int L;
		Node *head = new Node;
		f >> L;
		char q;
		while(f.peek() == ' ' || f.peek() == '\n')
			f.read(&q,1);
		parse(head, f);
		int A;
		string name;
		f >> A;
		for(int j = 0; j < A; j++)
		{
			f >> name;
			int n;
			f >> n;
			vector<string> v(n);
			for(int k = 0; k < n; k++)
			{
				f >> v[k];
			}
			o << fixed << gogo(head, v) << endl;
		}
	}
	o.close();
	f.close();
}