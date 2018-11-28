#include <iostream>
#include <boost/format.hpp>
#include <queue>

struct Tree
{
	Tree() : missed(0), remain(0), bought(false), cost(0), parent(NULL), left(NULL), right(NULL) {};
	int missed;
	int remain;
	int cost;
	bool bought;

	Tree *parent;
	Tree *left;
	Tree *right;
};

Tree* hang_tree(Tree *ts, size_t n)
{
	bool first = true;
	while(n > 0)
	{
		for(int i = 0; i < n; ++i)
		{
			if(!first)
			{
				std::cin >> ts[i].cost;
			}
			ts[i].parent = ts+n+i/2;
			if(i % 2)
			{
				ts[i].parent->right = ts+i;
			}
			else
			{
				ts[i].parent->left = ts+i;
			}	
		}
		first = false;
		ts += n;
		n /= 2;
	}

	return --ts;
}

void update_tree(Tree *p)
{
	int left = p->left->remain - p->left->missed;
	int right = p->right->remain - p->right->missed;

	if(left < right)
	{
		p->remain = p->left->remain;
		p->missed = p->left->missed+1;
	}
	else
	{
		p->remain = p->right->remain;
		p->missed = p->right->missed+1;
	}
}

int buy_tickets(Tree *p)
{
	if(!p->left)
	{
		return 0;
	}
	int tickets = buy_tickets(p->left)+buy_tickets(p->right);
	update_tree(p);
	if(p->remain < p->missed)
	{
		tickets++;
		--p->missed;
	}

	return tickets;
}

int main(int argc, char *argv[])
{
	int T;

	std::cin >> T;

	for(int t = 0; t < T; ++t)
	{
		int P;

		std::cin >> P;

		int M[1024] = {};
		Tree ts[2048];
		int nM = (2 << (P-1));

		for(int i = 0; i < nM; ++i)
		{
			std::cin >> ts[i].remain;
		}
		Tree * top = hang_tree(ts, nM);

		int cost = buy_tickets(top);
		
		std::cout << boost::format("Case #%d: %ld\n") % (t+1) % cost;
	}
}