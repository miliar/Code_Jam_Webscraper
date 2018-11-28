#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <tr1/array>
using namespace std;
using namespace std::tr1;

ifstream in;
ofstream out;

int K, n, d;
int nlets[8];
array<char, 4> lets[8];
array<char, 32> words[128];

#define MOD % 10009
//#define MOD

int main(int argc, char** argv)
{
        in.open(argv[1]);
        out.open(argv[2]);

        int T;
        in >> T;

        for(int test = 1; test <= T; ++test)
        {
        	string p;

        	in >> skipws >> p;
        	in >> K;
        	in >> n;

        	memset(words, 0, sizeof(words));
        	memset(lets, 0, sizeof(lets));
        	memset(nlets, 0, sizeof(nlets));

        	d = 0;
        	for(unsigned i = 0; i < p.size(); ++i)
        	{
        		char c = p[i];
        		if(c == '+')
        			++d;
        		else if(c >= 'a' && c <= 'z')
        			lets[d][nlets[d]++] = c - 'a';
        	}
        	++d;

        	for(int i = 0; i < n; ++i)
        	{
        		string w;
        		in >> skipws >> w;

        		for(unsigned j = 0; j < w.size(); ++j)
        		{
        			char c = w[j];
        			if(c >= 'a' && c <= 'z')
        			{
        				++words[i][c - 'a'];
        			}
        		}
        	}

        	out << "Case #" << test << ':';
        	for(int c = 1; c <= K; ++c)
        	{
        		int res = 0;
			int bres = 0;
        		for(int t = 0; t < d; ++t)
        		{
        			int tres = 0;
        			int sel[4];
        			int lim[4];
        			int nletst = nlets[t];
        			lim[0] = 0;
        			sel[0] = 0;
        			lim[1] = (nletst > 1) ? (sel[0] + 1) : 0;
        			for(sel[1] = 0; sel[1] <= lim[1]; ++sel[1])
        			{
        				lim[2] = (nletst > 2) ? (sel[1] + 1) : 0;
        				for(sel[2] = 0; sel[2] <= lim[2]; ++sel[2])
        				{
        					lim[3] = (nletst > 3) ? (max(sel[1], sel[2]) + 1) : 0;
        					for(sel[3] = 0; sel[3] <= lim[3]; ++sel[3])
        					{
        						int v = 1;
        						int groups = 0;
        						for(int i = 0; i < 4; ++i)
        						{
        							int elems = 0;
        							for(int j = 0; j < nletst; ++j)
        							{
        								if(sel[j] == i)
        									++elems;
        							}
        							if(!elems)
        								break;

        							++groups;
        							v = v * (c - i) MOD;

        							int sum = 0;
								for(int w = 0; w < n; ++w)
								{
									int wprod = 1;
									for(int j = 0; j < nletst; ++j)
									{
										if(sel[j] != i)
											continue;

										wprod = (wprod * words[w][lets[t][j]]) MOD;
//										cout << "mul " << (int)words[w][lets[t][j]] << endl;
									}
									sum = (sum + wprod) MOD;
//									cout << "wprod = " << wprod << endl;
								}
								sum = sum MOD;

								v = (v * sum) MOD;
								//cout << "Case " << test << " c = " << c << " term " << t << ' ' << sel[0] << sel[1] << sel[2] << sel[3] << " group " << i << " -> sum = " << sum << " v = " << v << endl;
        						}

        						if(groups > c)
        							v = 0;
        						else
        						{
        							for(int i = groups; i < c; ++i)
        							{
        								v = (v * n) MOD;
        							}
        						}

        						//cout << "Case " << test << " c = " << c << " term " << t << ' ' << sel[0] << sel[1] << sel[2] << sel[3] << " -> v = " << v << endl;

        						tres = (tres + v) MOD;
        					}
        				}
        			}
        			res = (res + tres) MOD;
        			/*
        			//cout << "TERM " << tres << endl;
        			if(c == 3)
        			{
					int w[3];
					int btres = 0;
					for(w[0] = 0; w[0] < n; ++w[0])
						for(w[1] = 0; w[1] < n; ++w[1])
							for(w[2] = 0; w[2] < n; ++w[2])
							{
								int prod = 1;
								for(int j = 0; j < nletst; ++j)
								{
									int sum = 0;
									for(int wi = 0; wi < c; ++wi)
										sum += words[w[wi]][lets[t][j]];
									prod = (prod * sum);
								}
								btres = (btres + prod);
							}
					bres = bres + btres;
					cout << "BTERM " << btres << endl;
        			}
        			*/
        		}
        		//if(c == 3)
        		//	cout << "BRES " << bres << endl;
        		out << ' ' << res;
        	}
        	out << endl;
        }
        return 0;
}
