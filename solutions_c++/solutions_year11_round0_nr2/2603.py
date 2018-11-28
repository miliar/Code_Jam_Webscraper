#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct Combination
{
	char f[2], t;
};

struct Opposition
{
	char a[2];
};
vector<Combination> combinations;
vector<Opposition> oppositions;
std::string outputVector(vector<char> vec) {
	string out = "[";
	for (int i = 0; i < vec.size(); ++i) {
		out += vec[i];
		if (i != vec.size() - 1)
			out += ", ";
	}
	out += "]";
	return out;
}

char Combine(char a, char b)
{
	for (int i = 0; i < combinations.size(); ++i) {
		char *c = combinations[i].f;
		if ((c[0] == a && c[1] == b) || (c[0] == b && c[1] == a))
			return combinations[i].t;
	}
	return 0;
}

bool Oppose(char a, vector<char> vec)
{
	for (int i = 0; i < vec.size(); ++i) {
		for (int x = 0; x < oppositions.size(); ++x) {
			char *c = oppositions[x].a;
			char b = vec[i];
			if ((c[0] == a && c[1] == b) || (c[0] == b && c[1] == a))
				return true;
		}
	}
	return false;
}
int main() {
	fstream file("b.in");
	if (!file.is_open()) {
		cout<<"nofile";
		return 0;
	}
	int numcases = 0;
	file >> numcases;
	for (int i = 0; i < numcases; ++i) {
		vector<char> result;
		combinations.clear();
		oppositions.clear();
		int numoppoistions = 0, numcombinations = 0, numchars = 0;
		file >> numcombinations;
		for (int x = 0; x < numcombinations; ++x) {
			std::string combo;
			file >> combo;
			Combination com;
			com.f[0] = combo[0];
			com.f[1] = combo[1];
			com.t = combo[2];
			combinations.push_back(com);
		}

		file >> numoppoistions;
		for (int x = 0; x < numoppoistions; ++x) {
			std::string oppose;
			file >> oppose;
			Opposition opp;
			opp.a[0] = oppose[0];
			opp.a[1] = oppose[1];
			oppositions.push_back(opp);
		}
		file >> numchars;
		string stuff;
		file >> stuff;
		for (int x = 0; x < stuff.length(); ++x) {
			if (result.empty()) {
				result.push_back(stuff[x]);
				continue;
			}
			char c = stuff[x];
			char l = result.back();
			char o = Combine(c, l);
			if (o != 0) {
				result.pop_back();
				c = o;
			}
			result.push_back(c);
			if (o == 0 && Oppose(c, result))
				result.clear();


		}

		cout << "Case #"<<i+1<<": "<<outputVector(result) << endl;
	}
}