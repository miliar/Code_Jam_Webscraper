#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

#define linelength 2000

struct tree
{
	double weight;
	string feature;
	vector<tree> subs;
};

struct animal
{
	string name;
	vector<string> features;
};

#define remws() do { while(input[pos] == ' ') pos++; } while(0)

double getweight(int& pos, string input)
{
	remws();
	
	double w = 0;
	while (input[pos] >= '0' && input[pos] <= '9')
	{
		w *= 10.0;
		w += (double)(input[pos] - '0');
		pos++;
	}
	
	if (input[pos] == '.')
	{
		pos++;
		
		double mult = 0.1;
		while (input[pos] >= '0' && input[pos] <= '9')
		{
			w += (double)(input[pos] - '0') * mult;
			mult /= 10.0;
			pos++;
		}
	}
	
	return w;
}

string getfeature(int& pos, string input)
{
	string rv;
	while (input[pos] >= 'a' && input[pos] <= 'z')
	{
		rv += input[pos];
		pos++;
	}
	
	return rv;
}

double recurse(tree& t, animal& a, double val)
{
	val *= t.weight;
	
	if (t.feature == "")
	{
		return val;
	}
	
	if (find(a.features.begin(), a.features.end(), t.feature) != a.features.end())
	{
		return recurse(t.subs[0], a, val);
	}
	else
	{
		return recurse(t.subs[1], a, val);
	}
}

void parsetree(tree* t, int& pos, string input)
{
	remws();
		
	if (input[pos] == '(')
	{
		pos++;
		t->weight = getweight(pos, input);
		
		//cerr << "weight " << t->weight << endl;
		
		remws();
		
		if (input[pos] == ')')
		{
			//cerr << "no subtree" << endl;
			pos++;
			return;
		}
		
		t->feature = getfeature(pos, input);
	
		//cerr << "feature " << t->feature << endl;
		
		tree a, b;
		t->subs.push_back(a);
		t->subs.push_back(b);
		
		parsetree(&t->subs[0], pos, input);
		parsetree(&t->subs[1], pos, input);
		
		remws();
		
		if (input[pos++] == ')')
		{
		}
		else
		{
			cerr << "parse err" << endl;
		}
	
	}
							   
	return;
}

int main(int argc, char** argv)
{
	char temp[linelength];
	
	cin.getline(temp, linelength);

	int ncases;
	sscanf(temp, "%d", &ncases);
	
	for (int i = 0; i < ncases; i++)
	{
		
		cin.getline(temp, linelength);
		int L;
		sscanf(temp, "%d", &L);
		
		string treestr;
		for (int j = 0; j < L; j++)
		{
			cin.getline(temp, linelength);
			treestr += temp;
		}
		
		//cerr << treestr << endl;
		
		tree t;
		int pos = 0;
		parsetree(&t, pos, treestr);
		
		cin.getline(temp, linelength);
		int A;
		sscanf(temp, "%d", &A);
		
		vector<animal> animals;
		for (int j = 0; j < A; j++)
		{
			animal a;
			cin.getline(temp, linelength);
			istringstream iss(temp, istringstream::in);
			iss >> a.name;
			int numfeat;
			iss >> numfeat;
			for (int k = 0; k < numfeat; k++)
			{
				string feat;
				iss >> feat;
				a.features.push_back(feat);
			}
			animals.push_back(a);
		}
		
		printf("Case #%d: \n", i+1);
		for (int j = 0; j < A; j++)
		{
			double val = 1.0;
			double res = recurse(t, animals[j], val);
			
			//cerr << "res " << res << endl;
			
			printf("%f\n", res);
		}
		
	}


}