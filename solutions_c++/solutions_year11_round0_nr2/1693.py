//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <assert.h>
#include <list>

using namespace std;
typedef unsigned char uchar;

struct ElementsTable
{
	struct Element
	{
		char non_base;
		bool opposite;
		Element() : non_base(0), opposite(false){}
	};

	Element table[256][256];

	void register_non_base(uchar a, uchar b, uchar c)
	{
		table[b][a].non_base = table[a][b].non_base = c;
	}

	void register_opposite(uchar a, uchar b)
	{
		table[b][a].opposite = table[a][b].opposite = true;
	}

	uchar form_non_base(uchar a, uchar b) const { return table[a][b].non_base; }
	bool has_opposite(const list<uchar> &elements, uchar ch)
	{
		for (list<uchar>::const_iterator it = elements.begin(); it!=elements.end(); it++)
			if (table[*it][ch].opposite)
				return true;
		return false;
	}
};

void main()
{
	ifstream f;
	f.open("in.txt");
	if (f.fail())
	{
		cout << "cannot open file" << endl;
		return;
	}

	int cases = 0;
	f >> cases;
	for (int _case=1; _case<=cases; _case++)
	{
		ElementsTable table;

		{
			int nonbase_count = 0;
			f >> nonbase_count;

			for (int i=0; i<nonbase_count; i++)
			{
				uchar a, b, c;
				f >> a;
				f >> b;
				f >> c;
				table.register_non_base(a, b, c); // a + b = c todo: register b + a too
			}
		}

		{
			int opposite_count = 0;
			f >> opposite_count;

			for (int i=0; i<opposite_count; i++)
			{
				uchar a, b;
				f >> a;
				f >> b;
				table.register_opposite(a, b);
			}
		}

			list<uchar> elements;
			int count;
			f >> count;
			for (int i=0; i<count; i++)
			{
				uchar ch;
				f >> ch;
				if (elements.empty())
					elements.push_back(ch);
				else
					if (char non_base = table.form_non_base(ch, *elements.rbegin()))
						*elements.rbegin() = non_base;
					else
						if (table.has_opposite(elements, ch))
							elements.clear();
						else
							elements.push_back(ch);
			}

		cout << "Case #" << _case << ": ";
		cout << "[";
		for (list<uchar>::const_iterator it = elements.begin(); it!=elements.end(); it++)
		{
			if (it != elements.begin())
				cout << ", ";

			cout << *it;
		}

		cout << "]" << endl;
	}
}
