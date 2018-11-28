#include <iostream>

using namespace std;

struct cell
{
	int height;
	cell* drain;
	char label;

	cell()
	{
		height = 0;
		drain = NULL;
		label = '\0';
	}

	~cell()
	{
	}

	char getLabel()
	{
		if(label == '\0' && drain != NULL)
		{
			return (label = drain->getLabel());
		}
		else
		{
			return label;
		}
	}

	void setLabel(char c)
	{
		label = c;
		if(drain != NULL)
		{
			drain->setLabel(c);
		}
	}

	bool betterDrain(cell& other)
	{
		if( (drain != NULL && other.height < drain->height)
			|| (drain == NULL && other.height < height))
		{
			drain = &other;
		}
	}
};

istream& operator>>(istream& i, cell& me)
{
	new(&me) cell();
	i >> me.height;
	return i;
}

ostream& operator<<(ostream& o, const cell& me)
{
	o << me.label;
	return o;
}

int main()
{
	size_t count;
	cin >> count;

	for(size_t i = 1; i <= count; i++)
	{
		size_t h, w;
		cin >> h >> w;

		cell grid[100][100];
		for(size_t j = 0; j < h; j++)
		{
			for(int k = 0; k < w; k++)
			{
				cin >> grid[j][k];
				if(j > 0)
				{
					grid[j][k].betterDrain(grid[j-1][k]);
					grid[j-1][k].betterDrain(grid[j][k]);
				}

				if(k > 0)
				{
					grid[j][k].betterDrain(grid[j][k-1]);
					grid[j][k-1].betterDrain(grid[j][k]);
				}
			}
		}

		cout << "Case #" << i << ":" << endl;
		char c = 'a';
		for(size_t j = 0; j < h; j++)
		{
			for(size_t k = 0; k < w; k++)
			{
				if(grid[j][k].getLabel() == '\0')
				{
					grid[j][k].setLabel(c);
					++c;
				}

				if(k != 0)
				{
					cout << " ";
				}

				cout << grid[j][k];
			}

			cout << endl;
		}
	}

	return 0;
}