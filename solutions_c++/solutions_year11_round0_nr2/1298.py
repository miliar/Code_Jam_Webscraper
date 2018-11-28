#include <iostream>
#include <vector>
using namespace std;

struct Oppose
{
	char a, b;
	friend istream &operator >>(istream &i, Oppose *o);
};

struct Combine
{
	char a, b, c;
	friend istream &operator>>(istream &i, Combine *c);
};

bool contains(vector<char> *v, char c);
bool contains(vector<Oppose*> *v, char a, char b);
vector<Combine*>::iterator contains(vector<Combine*> *v, char a, char b);
bool wipe(vector<Oppose*> *v, vector<char> *list, char a);


int main(int argc, char **args)
{
	int T = 0;
	cin >> T;
	for(int qwerty = 0; qwerty < T; qwerty++) {
		int c = 0;
		char t;
		vector<Oppose*> ops;
		vector<Combine*> comb;
		vector<char> list;
		Combine *curComb = NULL;
		Oppose *curOps = NULL;
		cin >> c;
		for(int i = 0; i < c; i++) {
			curComb = new Combine();
			cin >> curComb;
			comb.push_back(curComb);
		}
		cin >> c;
		for(int i = 0; i < c; i++) {
			curOps = new Oppose();
			cin >> curOps;
			ops.push_back(curOps);
		}
		cin >> c;
		if(c > 0 ) {
			cin >> t;
			list.push_back(t);
		}
		for(int i = 1; i < c; i++) {
			vector<Combine*>::iterator it;
			cin >> t;
			list.push_back(t);
			if(list.size() >= 2 && (it = contains(&comb, *(list.end()-2), *(list.end()-1))) != comb.end()) {
				list.pop_back();
				list.pop_back();
				list.push_back((*it)->c);
			}
			if(wipe(&ops, &list, *(list.end()-1))) {
				list.clear();
			}
		}
		cout << "Case #" << qwerty+1 << ": [";
		for(vector<char>::iterator it = list.begin(); it != list.end(); it++) {
			cout << *it;
			if(it + 1 != list.end()) {
				cout << ", ";
			}
		}
		cout << "]" << endl;
	}
	return 0;
}

istream &operator >>(istream &i, Oppose *o)
{
	i >> o->a >> o->b;
	return i;
}

istream &operator >>(istream &i, Combine *c)
{
	i >> c->a >> c->b >> c->c;
	return i;
}

bool contains(vector<char> *v, char c)
{
	for(vector<char>::iterator it = v->begin(); it != v->end(); v++) {
		if((*it) == c)
			return true;
	}
	return false;
}

bool contains(vector<Oppose*> *v, char a, char b)
{
	for(vector<Oppose*>::iterator it = v->begin(); it != v->end(); it++) {
		if(((*it)->a == a && (*it)->b == b) ||
			((*it)->b == a && (*it)->a == b)) {
				return true;
		}
	}
	return false;
}


vector<Combine*>::iterator contains(vector<Combine*> *v, char a, char b)
{
	for(vector<Combine*>::iterator it = v->begin(); it != v->end(); it++) {
		if(((*it)->a == a && (*it)->b == b) ||
			((*it)->b == a && (*it)->a == b)) {
				return it;
		}
	}
	return v->end();
}


bool wipe(vector<Oppose*> *v, vector<char> *c, char a)
{
	for(vector<char>::iterator it = c->begin(); it != c->end(); it++) {
		if(contains(v, a, (*it))) {
			return true;
		}
	}
	return false;
}