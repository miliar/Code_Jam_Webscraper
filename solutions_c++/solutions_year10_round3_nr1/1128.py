#include <stdint.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <list>

using namespace std;

#define CJ_min(a,b) ((a > b)?a:b)
#define CJ_max(a,b) ((a > b)?b:a)

#define CJ_pow2(a) (1<<a)

#define CJ_Pos2d(arr,w,x,y) (arr[x*w+y])


#define CJ_foreach(it,container) for(it = container.begin();it != container.end(); ++it)

struct wire
{
	int a;
	int b;
	wire(int _a, int _b) {a = _a; b=_b;}
};

typedef list<wire> WireList;

int64_t ReadInt(std::ifstream& str)
{
	int64_t val;
	str >> val;
	return val;
}

std::string ReadString(std::ifstream& str)
{
	std::string val;
	str >> val;
	return val;
}

bool Intersects(int a1, int b1, int a2, int b2)
{
	cout << "t1 " << a1 << " " << b1 << ", " << a2 << " " << b2 << " " << endl;
//	if ((CJ_max(a1,b1) < CJ_min(a2,b2)) || (CJ_min(a1,b1) > CJ_max(a2,b2)))
	if (((a1 < a2) && (b1 < b2)) || ((a1 > a2) && (b1 > b2)))
		return false;
	cout << "t2" << endl;
	return true;
}

void DoTrial(std::ifstream& in, std::ofstream& out)
{
	WireList wires;
	int numWires = ReadInt(in);
	int res = 0;
	for (int i = 0; i < numWires; ++i)
	{
		wires.push_back(wire(ReadInt(in),ReadInt(in)));
	}
	WireList::iterator firstit;
	WireList::iterator secondit;
	CJ_foreach(firstit,wires)
	{
		secondit = firstit;
		for (secondit++;secondit != wires.end(); ++secondit)
		{
			if (Intersects((*firstit).a,(*firstit).b,(*secondit).a,(*secondit).b))
			{
				res++;
			}
		}
	}
	out << res;
}

int main(int argc, char **argv)
{
	std::ifstream infile(argc>2?argv[1]:"test.in");
	std::ofstream outfile(argc>2?argv[2]:"test.out");
	int64_t numTrials = ReadInt(infile);
	for (int64_t trial = 1; trial <= numTrials; ++trial)
	{
		outfile << "Case #" << trial << ": ";
		DoTrial(infile,outfile);
		outfile << std::endl;
	}
	return 0;
}
