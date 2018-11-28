#include <iostream>
#include <ios>
#include <tr1/unordered_map>
#include <vector>
using namespace std;
using namespace std::tr1;

istream& in = cin;
ostream& out = cout;


int main(int argc, char** argv)
{
	int N;
	in >> N;
	for(int cas = 0; cas < N; ++cas)
	{
		int n, A, B, C, D, x0, y0, M;
		
		in >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		int x = x0;
		int y = y0;

		vector<pair<int, int> > pt;		
		long long cnt[3][3];
		memset(cnt, 0, sizeof(cnt));

		++cnt[x % 3][y % 3];
		pt.push_back(make_pair(x, y));
//		if(n < 16)
//			out << endl << "N = " << n << endl << endl;
//		if(n < 16)
//			out << x << ' ' << y << endl;
		
		for(int i = 1; i < n; ++i)
		{
			x = ((long long)A * (long long)x + (long long)B) % (long long)M;
			y = ((long long)C * (long long)y + (long long)D) % (long long)M;
//			if(n < 16)
//				out << x << ' ' << y << endl;
			++cnt[x % 3][y % 3];
			pt.push_back(make_pair(x, y));
		}

/*
		long long tres = 0;
		long long tresabc[3][3][3][3];
		memset(tresabc, 0, sizeof(tresabc));
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
			{
				if(i == j)
					continue;
					
				for(int k = 0; k < n; ++k)
				{
					if(k == j || k == i)
						continue;
						
					if((((pt[i].first % 3) + (pt[j].first % 3) + (pt[k].first % 3)) % 3) == 0)
					{
						if((((pt[i].second % 3) + (pt[j].second % 3) + (pt[k].second % 3)) % 3) == 0)
						{
							++tresabc[pt[i].first % 3][pt[i].second % 3][pt[j].first % 3][pt[j].second % 3];
							++tres;
						}
					}
				}
			}
		}
		*/
					
		long long res = 0;		
		for(int x1 = 0; x1 < 3; ++x1)
		{
			for(int y1 = 0; y1 < 3; ++y1)
			{
				for(int x2 = 0; x2 < 3; ++x2)
				{
					for(int y2 = 0; y2 < 3; ++y2)
					{
						int x3 = (6 - x1 - x2) % 3;
						int y3 = (6 - y1 - y2) % 3;
						
						long long a = cnt[x1][y1];
						long long b = cnt[x2][y2];
						long long c = cnt[x3][y3];
						
						long long v;
						if(x1 == x2 && y1 == y2 && x2 == x3 && y2 == y3)
							v = a * (b - 1) * (c - 2);
						else if(x1 == x2 && y1 == y2)
							v = a * (b - 1) * c; 
						else if(x2 == x3 && y2 == y3)
							v = a * b * (c - 1);
						else if(x3 == x1 && y3 == y1)
							v = (a - 1) * b * c;
						else
							v = a * b * c;
						
						res += v;
						
//						cerr << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << ' ' << v << ' ' << tresabc[x1][y1][x2][y2] << endl;
					}
				}
			}
		}
//		cerr << cnt[1][0] << endl;

//		if(res % 6)
//			out << "AARGH" << endl;		
		out << "Case #" << (cas + 1) << ": " << (res / 6) << ' ' << endl;
	}
}

