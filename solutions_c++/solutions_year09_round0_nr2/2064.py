#include <iostream>
#include <cstring>
#include <queue>

//#define DEBUG
#define D 100
#define MAX 2000000000

using namespace std;


long r, c;
long t[D+2][D+2];
long bd[D+2][D+2];
long ban[D+2][D+2];
char ans[D+2][D+2];
class pt
{
public:
	long r;
	long c;
	pt() {;}
	pt(long a, long b) : r(a), c(b) {;}
	pt operator+ (long a)
	{
		pt arg = *this;
		if (a == 1) 	 {arg.r--;}
		else if (a == 2) {arg.c--;}
		else if (a == 3) {arg.c++;}
		else 		 {arg.r++;}
		return arg;
	}
	long at() {return t[this->r][this->c];}
	long& _ban() {return ban[this->r][this->c];}
	char& _ans() {return ans[this->r][this->c];}
	long& _bd()  {return bd[this->r][this->c];}
};
void print_bd()
{
	long y, j;
	for(y = 1; y <= r; y++)
	{
		for(j = 1; j <= c; j++)
		{
			cout << bd[y][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n\n";
	
}
void init()
{
	cin >> r >> c;
	long y, j;
	for(y = 1; y <= r; y++)
	{
		t[y][0] = t[y][c+1] = MAX;
		for(j = 1; j <= c; j++)
		{
			cin >> t[y][j];
		}
	}
	for(y = 1; y <= c; y++)
	{
		t[0][y] = t[r+1][y] = MAX;
	}	
	memset(bd, 0, sizeof(bd));
	memset(ans, 0, sizeof(ans));
	memset(ban, 0, sizeof(ban));
}
void make_bd()
{
	pt cur;
	long y;
	long bla;
	pt tmp;
	pt next;
	char last = 'a' - 1;
	for(cur.r = 1; cur.r <= r; cur.r++)
	{
		for(cur.c = 1; cur.c <= c; cur.c++)
		{			
			if (cur._ban()) {continue;}
			cur._ban() = 1;
			tmp = cur;
			for(; ;)
			{
#ifdef DEBUG
				cout << "(" << tmp.r << "," << tmp.c << ") ";
#endif
				bla = tmp.at();
				long best_dir = -1;
				for(y = 1; y <= 4; y++)
				{
					next = tmp + y;
					if (next.at() < bla)
					{
						bla = next.at();
						best_dir = y;
					}		
				}
				if (best_dir == -1)
				{
					// tmp = den
					last++;
					tmp._ans() = last;
					tmp._ban() = 1;
					tmp._bd() = -1;
					break;	
				}
				else
				{
					tmp._bd() = best_dir;
					tmp = tmp + best_dir;
					if (tmp._ban()) {break;}
					tmp._ban() = 1;
				}
			}
		}
	}
}
void bfs(pt be)
{
	char mark = be._ans();
	queue<pt> qu;
	qu.push(be);
	pt jo;
	pt bla;
	for(; !qu.empty(); )
	{
		jo = qu.front();
		qu.pop();
		jo._ans() = mark;
		long dir;
		for(dir = 1; dir <= 4; dir++)
		{	
			bla = jo + dir;
			if (bla._bd() == (5 - dir))
			{
				qu.push(bla);
			}
		}
	}
}
void make_ans()
{
	long rr, cc;
	for(rr = 1; rr <= r; rr++)
	{
		for(cc = 1; cc <= c; cc++)
		{
			if (bd[rr][cc] == -1)
			{
				bfs(pt(rr, cc));
			}
		}
	}
}
void print_ans()
{
#ifdef DEBUG
	cerr << "print_ans working\n";
#endif
	long y, j;
	for(y = 1; y <= r; y++)
	{
		for(j = 1; j <= c; j++)
		{
			cout << ans[y][j] << " ";
		}
		cout << "\n";
	}
}
void print_t()
{
	long y, j;
	for(y = 0; y <= r+1; y++)
	{
		for(j = 0; j <= c+1; j++)
		{
			if (t[y][j] == MAX) {cout << "X "; continue;}
			cout << t[y][j] << " ";
		}
		cout << "\n";
	}
}
void logic()
{
	init();
#ifdef DEBUG
	print_t();
#endif
	make_bd();
#ifdef DEBUG
	print_bd();
	cerr << "before make_ans\n";
#endif
	make_ans();
	print_ans();
}
int main()
{
	long tt;
	long y;
	cin >> tt;
	for(y = 1; y <= tt; y++)
	{
		cout << "Case #" << y << ":\n";
		logic();
	}
}