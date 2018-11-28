#include <cstdlib>
#include <iomanip>
#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

ifstream fin;
ofstream fout;

string tree;
string inp;

vector<string> tokens;
vector<string> chars;

double getResult()
{
	double p = 1.0;
	for(int i = 0; i < tokens.size(); i++)
	{
		if(tokens[i] == "(")
		{
			p *= atof(tokens[i+1].c_str());
			if(tokens[i+2] == ")")
				return p;
			i++;
		}
		else
		{
			bool ok = false;
			for(int j = 0; j < chars.size(); j++)
				if(tokens[i] == chars[j])
					ok = true;
			if(ok)
				continue;
			else
			{
				int l = 1;
				int r = 0;
				int x = i + 2;
				while(l != r)
				{
					if(tokens[x] == "(")
						l++;
					else if(tokens[x] == ")")
						r++;
					x++;
				}
				i = x-1;
			}
		}
	}
	return p;
}

void push(string s)
{
	if(s.size() != 0)
		tokens.push_back(s);
}

void buildTree()
{
	string s = "";
	tree += " ";
	tokens.clear();
	for(int i = 0; i < tree.size(); i++)
	{
		if(tree[i] == ' ')
		{
			push(s);
			s = "";
		}
		else if(tree[i] == '(')
		{
			push(s);
			push("(");
			s = "";
		}
		else if(tree[i] == ')')
		{
			push(s);
			push(")");
			s = "";
		}
		else
			s += tree[i];
	}
}


int main()
{
	int N,L,A,n;
	fin.open("a_large.in");
	fout.open("a_large.out");
	
	fin >> N;
	getline(fin, inp);
	for(int t = 1; t <= N; t++)
	{
		tree = "";
		fin >> L;
		getline(fin,inp);
		while(L--)
		{
			getline(fin,inp);
			tree += " " + inp;
		}
		buildTree();
		fout << "Case #" << t << ": " << endl;
		
		fin >> A;
		while(A--)
		{
			chars.clear();
			fin >> inp >> n;
			while(n--)
			{
				fin >> inp;
				chars.push_back(inp);
			}
			fout << fixed << setprecision(7) << getResult() << endl;
		}
	}
	fout.close();
	fin.close();
	return 0;
}
