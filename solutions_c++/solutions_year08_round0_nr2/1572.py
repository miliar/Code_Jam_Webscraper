// B.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

std::ifstream in ("B.in");
std::ofstream out ("B.out");

struct time
{
	int t;
	int st;
	int type;
	time()
	{
		t = 0;
		st = 0;
		type = 0;
	}
	time(int t1, int st1, int type1)
	{
		t = t1;
		st = st1;
		type = type1;
	}
	bool operator < (time t1)
	{
		if (t < t1.t)
			return true;
		if (t == t1.t)
		{
			return (type > t1.type);
		}
		return false;
	}
};

int N;
int NA, NB;
int T;
int TA = 0;
int TB = 0;
int resA = 0;
int resB = 0;

std::vector <std::string> A1;
std::vector <std::string> A2;
std::vector <std::string> B1;
std::vector <std::string> B2;

std::vector <time> X;

int getMinutes(std::string s)
{
	int result = 0;
	std::string h = "";
	std::string m = "";
	h += s[0]; h+= s[1];
	m += s[3]; m+= s[4];

	result += atoi(h.c_str());
	result*=60;
	result += atoi(m.c_str());
	return result;
}

void input()
{
	A1.clear();
	A2.clear();
	B1.clear();
	B2.clear();
	X.clear();

	in >> T;
	in >> NA >> NB;
	for (int i=0; i<NA; i++)
	{
		std::string str = "";
		in >> str;
		A1.push_back (str);
		in >> str;
		B2.push_back (str);
	}

	for (int i=0; i<NB; i++)
	{
		std::string str = "";
		in >> str;
		B1.push_back (str);
		in >> str;
		A2.push_back (str);
	}
}

void solve()
{
	TA = 0;
	TB = 0;
	resA = 0;
	resB = 0;
	for (int i=0; i<A1.size(); i++)
	{
		X.push_back(time(getMinutes(A1[i]), 0, 0));
		X.push_back(time(getMinutes(B2[i]) + T, 1, 1));
	}

	for (int i=0; i<B1.size(); i++)
	{
		X.push_back(time(getMinutes(B1[i]), 1, 0));
		X.push_back(time(getMinutes(A2[i]) + T, 0, 1));
	}

	std::sort (X.begin(), X.end());

	for (int i=0; i<X.size(); i++)
	{
		if (X[i].st == 0)
		{
			if (X[i].type == 0)
			{
				if (TA>0)
					TA--;
				else
					resA++;
			}
			else
			{
				TA++;
			}
		}
		else
		{
			if (X[i].type == 0)
			{
				if (TB>0)
					TB--;
				else
					resB++;
			}
			else
			{
				TB++;
			}
		}
	}
}

int main()
{
	in >> N;
	for (int k=0; k<N; k++)
	{
		input();
		solve();
		out << "Case #" << k+1 << ": " << resA << " " << resB << "\n";
	}
	return 0;
}

