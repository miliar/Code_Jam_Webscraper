//Grzegorz Prusak: problem "Decision Tree"
#include <iostream>
#include <string>
#include <set>
#include <iomanip>

//loops
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

const int N_max = 100;
const int L_max = 100;
const int A_max = 100;
const int n_max = 100;

struct Node
{
	double p;
	std::string name;
	Node *l,*r;
};

Node S[10000]; int ss;

Node * read_tree()
{
	Node &n = S[ss++];
	std::cin >> std::ws; std::cin.get(); std::cin >> n.p >> std::ws; 
	int c = std::cin.peek(); //std::cout << "[" << n.p << "]";
	
	if(c==')') n.l = 0; else
	{
		std::cin >> std::ws >> n.name;
		n.l = read_tree();
		n.r = read_tree();
		std::cin >> std::ws;
	}
	std::cin.get();
	return &n;
}

int main()
{
	int N; std::cin >> N; FOR(x,1,N)
	{
		//input tree
		int L; std::cin >> L;
		ss = 0; Node *root = read_tree();
		
		//output header
		std::cout << "Case #" << x << ":\n";
		
		//process animals
		int A; std::cin >> A; REP(i,A)
		{
			//input features
			std::set<std::string> fm;
			std::string name,feature; int n; std::cin >> name >> n;
			while(n--){ std::cin >> feature; fm.insert(feature); }
			
			//trace tree
			double res = 1; Node *t = root;
			while(t->l){ res *= t->p; if(fm.find(t->name)!=fm.end()) t = t->l; else t = t->r; }
			res *= t->p;
			
			//output
			std::cout.precision(7);
			std::cout << std::fixed << res << "\n";
		}
	}

	return 0;
}

