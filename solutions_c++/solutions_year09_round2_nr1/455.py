#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
using namespace std;

class ProblemA
{
	struct Node
	{
		Node()   { p1 = p2 = 0; }
		~Node()  { delete p1;  delete p2; }

		double w;
		string feature;
		Node *p1, *p2;

		void read(istream &is)
		{
			char c;
			is >> c;	// '('
			is >> w;	// weight
			is >> c;	// ')' or feature
			if (c==')')  return;			// no feature
			cin.putback(c);  is >> feature;	// feature name
			p1 = new Node();  p1->read(is);
			p2 = new Node();  p2->read(is);
			is >> c;	// ')'
		}
		double getp(double p, const set<string> &animal)
		{
			p *= w;
			if (feature.empty())  return p;
			return (animal.count(feature) ? p1 : p2) -> getp(p, animal);
		}
	};

	int L;
	int A;
	Node *pTree;
	vector<set<string> > animals;

public:
	ProblemA() : pTree(0) {}
	void ReadData()
	{
		int L;  cin >> L;
		delete pTree;  pTree = new Node();  pTree->read(cin);
		int A;  cin >> A;
		animals.assign(A, set<string>());
		for (int i=0; i<A; ++i)
		{
			string s;  cin >> s;	// animal name
			int N;  cin >> N;		// number of features
			for (int j=0; j<N; ++j)  { cin >> s;  animals[i].insert(s); }
		}
	}
	void Solve(int nCase)
	{
		ReadData();

		cout << "Case #" << nCase << ":" << endl;
		for (int i=0; i<animals.size(); ++i)
			cout << pTree->getp(1.0, animals[i]) << endl;
	}
};

int main()
{
	int N;  cin >> N;
	ProblemA sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}