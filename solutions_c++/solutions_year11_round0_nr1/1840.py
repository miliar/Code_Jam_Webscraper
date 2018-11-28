#include <iostream>

struct Robot
{
	unsigned int p;
	unsigned int t;

	Robot()
	{
		p = 1;
		t = 0;
	}
};

int abs(int a)
{
	if(a < 0)
		return -a;
}

void move(Robot& me, Robot& you)
{
	unsigned int np;
	std::cin >> np;

	me.t += abs(np - me.p);
	me.t = std::max(me.t, you.t);
	me.t++;

	me.p = np;
}

void solve()
{
	Robot o;
	Robot b;
	unsigned int n;
	std::cin >> n;

	for(unsigned int i=0; i < n; i++)
	{
		while(std::cin.peek() == ' ')
			std::cin.get();

		if(std::cin.get() == 'O')
			move(o,b);
		else
			move(b,o);
	}

	while(std::cin.peek() == ' ')
		std::cin.get();
	std::cin.get();

	std::cout << (o.t > b.t ? o.t : b.t);
}


int main()
{
	int n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(unsigned int i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
		solve();
		std::cout << std::endl;
	}
}

