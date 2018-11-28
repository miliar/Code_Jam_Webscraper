#include <fstream>
using namespace std;

char repl[8][8];
char traps[28][2];

ifstream input("input.txt");
ofstream output("output.txt");

int trans(char c)
{
	switch (c)
	{
	case 'Q': return 0;
	case 'W': return 1;
	case 'E': return 2;
	case 'R': return 3;
	case 'A': return 4;
	case 'S': return 5;
	case 'D': return 6;
	case 'F': return 7;
	default: return -1;
	}
}

void solve(int ix, int c, int d, int n, char *w)
{
	char res[128]; int rp=0;
	for (int i=0;i<n;++i)
	{
		bool add = true;
		if (rp>0)
		{
			int t = trans(res[rp-1]);
			if (t!=-1 && repl[t][trans(w[i])])
			{
				add = false;
				res[rp-1] = repl[t][trans(w[i])];
			}
			else
			{
				for (int j=0;j<d;++j)
				{
					char o=0xff;
					if (traps[j][0]==w[i]) o=traps[j][1];
					if (traps[j][1]==w[i]) o=traps[j][0];
					if (o!=0xff)
						for (int k=0;k<rp;++k)
							if (res[k]==o)
							{
								rp = 0; add=false; j=d; break;
							}
				}
			}
		}
		if (add) res[rp++] = w[i];
	}
	res[rp]=0;
	output << "Case #" << ix << ": [";
	for (int i=0;i<rp;++i)
	{
		output << res[i];
		if (i < rp-1) output << ", ";
	}
	output << "]" << endl;
}

int main()
{
	int t, c, d, n;
	char buf[110];
	input >> t;
	for (int i=0;i<t;++i)
	{
		memset(repl, 0, sizeof(repl));		
		input >> c;
		for (int j=0;j<c;++j)
		{
			input >> buf;
			repl[trans(buf[0])][trans(buf[1])]=buf[2];
			repl[trans(buf[1])][trans(buf[0])]=buf[2];
		}
		input >> d;
		for (int j=0;j<d;++j)
		{
			input >> buf;
			traps[j][0]=buf[0]; traps[j][1]=buf[1];
		}
		input >> n;
		input >> buf;
		solve(i+1,c,d,n,buf);
	}
	return 0;
}