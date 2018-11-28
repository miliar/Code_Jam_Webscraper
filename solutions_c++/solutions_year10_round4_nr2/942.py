#include <iostream>
#include <vector>
#include <algorithm>
using std::cin;
using std::cout;
using std::cerr;
using std::vector;
using std::min;
using std::max;

typedef vector<int> VI;
typedef vector<VI> VVI;

typedef vector<bool> VB;
typedef vector<VB> VVB;


void cevi(const VI & v)
{
	for(unsigned i=0; i < v.size(); i++)
		cerr << v[i] << ' ';
	cerr << "\n\n";
}

class node
{
	int min;
	int max;
	bool buy;
	node *left;
	node *right;

	node(int mi, int ma) : buy(false), left(NULL), right(NULL)
	{
		min = mi;
		max = ma;

		int r = ma-mi;
		if(r!=1)
		{

			r=(r+1)/2 - 1;
			left = new node(mi, mi+r);
			right = new node(mi+r+1, mi+r+1+r);
		}
	}

	public:
		static node* make(int n)
		{
			return new node(0, n);
		}

		int count() const
		{
			int r = buy;
			if(left != NULL)
			{
				r+=left->count();
				r+=right->count();
			}
			return r;
		}

		void solve(VI & wants)
		{
			//int n = wants.size();
			for(int i = min; i <=max;i++)
			{
				if(wants[i] > 1)
				{
					wants[i]--;
					buy=true;
				}
			}
			if(left != NULL)
			{
				left->solve(wants);
				right->solve(wants);
			}
		}
};

int main()
{
	int c;
	cin >> c;
	for(int ccc = 0; ccc < c; ccc++)
	{
		int p;
		cin >> p;
		int tm = 1<<p;
		VI prefs(tm);
		for(int i = 0; i < tm;i++)
		{
			int t;
			cin >> t;
			prefs[i] = p-t+1;
		}

		//price
		for(int i = 0; i < tm-1;i++)
		{
			int t;
			cin >> t;
		}

		node *mm = node::make(tm-1);

	//	cevi(prefs);
		mm->solve(prefs);


		cout << "Case #" << (ccc+1) << ": " << mm->count() <<  "\n";
	}
	return 0;
}
