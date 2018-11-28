#include <fstream>

using namespace std;

int t;
int n;
bool q[100];
int o[100];
int b[100];
ofstream output("output.txt");

int dir (int from, int to)
{
	if (to-from>0) return 1;
	if (to-from<0) return -1;
	return 0;
}
int adv(int from, int to, int time)
{
	int d = to - from;
	if (abs(d)>time) 
		return from + time*dir(from,to);
	return to;
}

void run(int cs, int n, int no, int nb)
{
	int opos = 1, bpos = 1, onext, bnext;
	bool ofirst;
	int i=0, io=0, ib=0;
	int t = 0;
	for (i=0;i<n;++i)
	{
		if (io<no) onext = o[io];
		if (ib<nb) bnext = b[ib];
		ofirst = q[i];
		int lt = abs((ofirst)?(onext - opos):(bnext-bpos)) + 1;
		t+=lt;
		if (ofirst)
		{
			opos = onext; ++io;
			if (ib!=nb) bpos = adv(bpos, bnext, lt);
		}
		else
		{
			bpos = bnext; ++ib;
			if (io!=no) opos = adv(opos, onext, lt);
		}
	}
	output << "Case #" << cs << ": " << t << endl;
}

int main()
{
	ifstream input("input.txt");
	input >> t;
	for (int i=0;i<t;++i)
	{
		input >> n;
		char c; int p, qp = 0, op = 0, bp = 0;
		for (int j=0;j<n;++j)
		{
			input >> c >> p;
			q[qp++]=(c=='O');
			if (c=='O') o[op++]=p;
			else b[bp++]=p;
		}
		run(i+1, n, op, bp);
	}
	return 0;
}