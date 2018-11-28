#include <cstring>
#include <fstream>
#include <sstream>
#include <string>

using std::ifstream;
using std::ofstream;
using std::string;
using std::stringstream;

typedef unsigned int uint;

class CodeJamIO
{
private:

	string append(const char* a, const char* b)
	{
		string c(a);
		c += b;
		return c;
	}
public:

	CodeJamIO(const char* naam) : sc(append(naam, ".in").c_str()), ps(append(naam, ".out").c_str())
	{
		if (!sc.is_open() || !ps.is_open())
			throw "foutje";
		index = 0;
		sc >> size;
		//init
		next();
	}

	virtual ~CodeJamIO()
	{
	}

	void print()
	{
		ps << "Case #" << index << ": " << ss.str() << std::endl;
		ss.str("");
	}

	bool hasMore()const
	{
		return index < size;
	}

	void close()
	{
		sc.close();
		ps.close();
	}

private:
	ifstream sc;
	ofstream ps;
	stringstream ss;
	int index;
	int size;
	int X;
	int O;
	static uint a;
	static uint p[];
public:

	void next()
	{
		X = 0;
		O = 0;
		//data
		char buffer;
		for (uint i = 0; i < 4 * 4; i++)
		{
			sc >> buffer;
			if (buffer == 'X' || buffer == 'T')
				X |= (1 << i);
			if (buffer == 'O' || buffer == 'T')
				O |= (1 << i);
		}
		index++;
	}

	void solve()
	{
		bool xwon = false;
		bool owon = false;
		uint i = 0;
		while (i < a && !xwon && !owon)
		{
			xwon = (X & p[i]) == p[i];
			owon = (O & p[i]) == p[i];
			i++;
		}
		uint tussen = X|O;
		if (xwon)
			ss << "X won";
		else if (owon)
			ss << "O won";
		else if ((X | O) == 0xFFFF)
			ss << "Draw";
		else
			ss << "Game has not completed";
		print();
	}
private:
	//data
};

uint CodeJamIO::a = 10;
uint CodeJamIO::p[] = {0x000F, 0x00F0, 0x0F00, 0xF000,
	0x8888, 0x4444, 0x2222, 0x1111,
	0x8421, 0x1248};
using namespace std;

int main()
{
	CodeJamIO cd("A-large");//-large
	cd.solve();
	while (cd.hasMore())
	{
		cd.next();
		cd.solve();
	}
	cd.close();
	return 0;
}
