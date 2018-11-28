
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
using namespace std;

long long RunTest(ifstream &in)
{
	typedef pair<long long, long long> vec;
	set<vec> pts;
	vector<vec> pv;
	vector<bool> used;
	long long n,  A, B, C, D, x0, y0, M;
	long long res = 0;
	long long x, y;

	in >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
	in.get();

	x = x0;
	y = y0;
//	cout << " " << x << " " << y << endl;
	vec p1 = vec(x, y);
	pts.insert(p1);
	pv.push_back(p1);
	used.push_back(false);
	
	for(long long i = 1; i < n; i++)
	{
		x = (A * x + B)%M;
		y = (C * y + D)%M;
//		cout << " " << x << " " << y << endl;
		pts.insert(vec(x, y));
		pv.push_back(vec(x, y));
		used.push_back(false);	
	}

//	cout << endl;

	for(long long i = 0; i < n; i++)
		for(long long j = i + 1; j < n; j++)
			for(long long k = j + 1; k < n; k++)
			{

				long long cx = (pv[i].first + pv[j].first + pv[k].first)/3;
				long long cy = (pv[i].second + pv[j].second + pv[k].second)/3;

				long long cm1 = (pv[i].first + pv[j].first + pv[k].first)%3;
				long long cm2 = (pv[i].second + pv[j].second + pv[k].second)%3;

				if(cm1 || cm2)
					continue;

//				cout << "    " << i << "  " << j << " " << k << " = " << cx << " " << cy << endl;

				vec cp = vec(cx, cy);

				//if(pts.find(cp) != pts.end())
					res++;
			}

	return res;
}

int main(int argc, char* argv[])
{
	if(argc != 2)	cout << "specify input file";
	ifstream in(argv[1]);

	long long n;
	in >> n;

	for(long long i = 0; i < n; i++)
		cout << "Case #" << (i + 1) << ": " << RunTest(in) << endl;

	return 0;
}

