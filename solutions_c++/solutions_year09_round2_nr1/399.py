#include<cstdlib>
#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<cctype>
using namespace std;

//============================================================
// Cute
//============================================================
class Cute
{
public:
	Cute(string dtree) {
		dt = dtree;
		idx = 0;
		root = ReadTree();
	}
	double Solve(vector<string> features)
	{
		mf.clear();
		for(int i = 0;i < (int)features.size();++i)
			mf.insert(features[i]);
		return RSolve(1.0,root);
	}
private:
	set<string> mf;
	double RSolve(double p,int vidx)
	{
		const vert &v = vertices[vidx];
		p *= v.weight;
		if(v.left == -1) return p;

		if(mf.find(v.feature) != mf.end())
			return RSolve(p,v.left);
		return RSolve(p,v.right);
	}

	string dt;
	int idx;
	struct vert{
		vert():left(-1),right(-1){}
		double weight;
		string feature;

		int left,right;
	};

	vector<vert> vertices;
	int root;

	int ReadTree()
	{
		while(isspace(dt[idx])) ++idx;
		if(dt[idx] != '(') throw string();
		++idx;
		while(isspace(dt[idx])) ++idx;
		int start = idx;
		while(isdigit(dt[idx]) || dt[idx] == '.') ++idx;

		double weight;
		{istringstream iss(dt.substr(start,idx-start)); iss >> weight;}
		while(isspace(dt[idx])) ++idx;
		if(dt[idx] == ')') {
			// Leaf.
			++idx;
			vertices.push_back(vert());
			vertices.back().weight = weight;
			return vertices.size()-1;
		}

		start = idx;
		while(isalpha(dt[idx])) ++idx;
		string feature = dt.substr(start,idx-start);

		vertices.push_back(vert());
		int v = vertices.size()-1;
		vertices[v].weight = weight;
		vertices[v].feature = feature;
		int left = ReadTree();
		int right = ReadTree();
		vertices[v].left = left;
		vertices[v].right = right;
		while(isspace(dt[idx])) ++idx;
		if(dt[idx] != ')') throw string();
		++idx;
		return v;
	}

};
//============================================================

int main()
{
	string s;
	int N;
	{getline(cin,s); istringstream iss(s); iss >> N;}
	for(int ca = 1;ca <= N;++ca) {
		int L;
		{getline(cin,s); istringstream iss(s); iss >> L;}
		string dtree_str;
		for(int l = 0;l < L;++l) {
			getline(cin,s);
			dtree_str += s;
		}

		Cute problem(dtree_str);

		int A;
		{getline(cin,s); istringstream iss(s); iss >> A;}

		cout << "Case #" << ca << ":\n";
		for(int a = 0;a < A;++a) {
			getline(cin,s);
			istringstream iss(s);
			string animal;
			int n;
			iss >> animal >> n;
			vector<string> features;
			for(int i = 0;i < n;++i){
				if(!(iss >> s)) throw string();
				features.push_back(s);
			}
			cout << problem.Solve(features) << '\n';
		}
	}
}
