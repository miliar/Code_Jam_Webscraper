#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>
#include <map>

using namespace std;

const int MAX_DEPTH = 50000;

struct Node
{
	map<string, Node*> fs;
	
	~Node()
	{
		for (map<string, Node*>::iterator pos = fs.begin(); pos != fs.end(); ++pos)
			delete pos->second;
	}
	
	Node* getNext(const string& s)
	{
		map<string, Node*>::iterator pos = fs.find(s);
		if (pos != fs.end()) return pos->second;
		Node* n = new Node();
		fs[s] = n;
		return n;
	}
	
	Node* getNext(const string& s, int& addCount)
	{
		map<string, Node*>::iterator pos = fs.find(s);
		if (pos != fs.end()) return pos->second;
		Node* n = new Node();
		fs[s] = n;
		addCount++;
		return n;
	}
};

int solve()
{
	int created, toCreate;
	int solution = 0;
	string s;
	
	cin >> created >> toCreate;
	
	Node* radix = new Node();
	for (int i = 0; i < created; i++)
	{
		cin >> s;
		for (int j = 0; j < s.length(); j++)
			if (s.c_str()[j] == '/') s[j] = ' ';
		istringstream is(s);

		Node* p = radix;
		while (is >> s)
			p = p->getNext(s);		
	}
	for (int i = 0; i < toCreate; i++)
	{
		cin >> s;
		for (int j = 0; j < s.length(); j++)
			if (s.c_str()[j] == '/') s[j] = ' ';
		istringstream is(s);
		
		Node* p = radix;
		while (is >> s)
		{
			p = p->getNext(s, solution);
		}		
	}
	delete radix;
	return solution;
}

int main()
{
	int testCase;
	cin >> testCase;
	for (int i = 1; i <= testCase; i++)
	   cout << "Case #" << i << ": " << solve() << endl;
	return 0;
}

