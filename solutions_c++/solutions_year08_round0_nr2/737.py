#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
#include <fstream>
using namespace std;

#define INFILE "B-large.in"
#define OUTFILE "B-large.out"

int main()
{
    int N, T, NA, NB;
	list<int> S_a, A_a, S_b, A_b;
	int icase,i;
	int nsa,nsb;
	int t_S,t_A;
	list<int>::iterator it_S,it_A;
	string s;

	ifstream in;
	ofstream out;
	in.open(INFILE);
	out.open(OUTFILE);

	if (!in || !out)
		return 0;
	
	in >> N;
	for(icase=0; icase<N; icase++)
	{
		in >> T;
		in >>NA>>NB;
		S_a.clear(); A_a.clear();
		S_b.clear(); A_b.clear();

		nsa=0; nsb=0;

		for(i=0; i<NA; i++)
		{
			s="";
			while(s.length()==0)
				getline(in, s);
			t_S = ((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+(s[4]-'0');
			t_A = ((s[6]-'0')*10+(s[7]-'0'))*60+(s[9]-'0')*10+(s[10]-'0');
			t_A += T;
			S_a.push_back(t_S);
			A_a.push_back(t_A);
		}
		S_a.sort();
		A_a.sort();

		for(i=0; i<NB; i++)
		{
			s="";
			while(s.length()==0)
				getline(in, s);
			t_S = ((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+(s[4]-'0');
			t_A = ((s[6]-'0')*10+(s[7]-'0'))*60+(s[9]-'0')*10+(s[10]-'0');
			t_A += T;
			S_b.push_back(t_S);
			A_b.push_back(t_A);
		}
		S_b.sort();
		A_b.sort();

		it_A = A_b.begin();
		for (it_S=S_a.begin(); it_S!=S_a.end(); it_S++)
		{
			if (it_A!=A_b.end() && *it_S >= *it_A)
			{
				it_A++;
			}
			else
			{
				nsa++;
			}
		}

		it_A = A_a.begin();
		for (it_S=S_b.begin(); it_S!=S_b.end(); it_S++)
		{
			if (it_A!=A_a.end() && *it_S >= *it_A)
			{
				it_A++;
			}
			else
			{
				nsb++;
			}
		}
		out << "Case #"<<icase+1<<": "<<nsa<<" "<<nsb<<endl;

	}

	in.close();
	out.close();
	return 0;
}

