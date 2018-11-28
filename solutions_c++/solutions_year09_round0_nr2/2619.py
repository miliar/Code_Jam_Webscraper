#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<sstream>

using namespace std;
#define SZLIM 150
int basin[SZLIM][SZLIM];
long  res[SZLIM][SZLIM];
int ch = 1;

void display_output(int r, int c)
{
	// display output
	for(int i = 1; i <= r; i++)
	{
		for(int j = 1; j <= c; j++)
		{
			//if(j > 1)
				cout << " ";
			cout << (char)('a'-1+res[i][j]);
		}
		cout << endl;
	}
}

bool iamasink(int r, int c)
{
	// if i cannot flow i am a sink
	bool rv = false;
	int me = basin[r][c];

	if( (me <= basin[r-1][c]) && (me <= basin[r][c-1]) && (me <= basin[r+1][c]) && (me <= basin[r][c+1]) )
		rv = true;

	return rv;
}

void resolve_conflict(long l1, long l2)
{
	if(l1 == l2)
		return;

	long ll = min(l1,l2);
	long lh = max(l1,l2);
	ch--;

	for(int i = 1; i < SZLIM; i++)
		for(int j = 1; j < SZLIM; j++)
		{
			if(res[i][j] == 0)
				continue;
			if(res[i][j] == lh)
				res[i][j] = ll;
			if(res[i][j] > lh)
				res[i][j]--;
		}
}
void flow(int r, int c)
{
	int nr, nc, n;
	n = 12000;
	if(iamasink(r,c))
		return;
	// n>w>e>s
	int zr,zc;
	// n
	zr = r-1;
	zc = c;
	if(basin[zr][zc] < n){nr = zr;nc = zc; n = basin[zr][zc]; }
	//cout << n << endl;

	// w
	zr = r;
	zc = c-1;
	if(basin[zr][zc] < n){nr = zr;nc = zc; n = basin[zr][zc]; }

	// e
	zr = r;
	zc = c+1;
	if(basin[zr][zc] < n){nr = zr;nc = zc; n = basin[zr][zc]; }

	// s
	zr = r+1;
	zc = c;
	if(basin[zr][zc] < n){nr = zr;nc = zc; n = basin[zr][zc]; }

	if(0 == res[nr][nc])
		res[nr][nc] = res[r][c];
	else
		resolve_conflict(res[nr][nc], res[r][c]);
}

void process_testcase(int r, int c)
{
	for(int i = 1; i <= r; i++)
	{
		for(int j = 1; j <= c; j++)
		{
			// only 2 things to do
			// 1st get my basin label
			// 2nd. flow on
			if(0 == res[i][j])// no label? get new
			{
				res[i][j] = ch;
				ch++; // create a new basin label
			}
			flow(i,j);
		}
	}
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("C:\\Users\\viv.NORTHAMERICA\\Downloads\\ipfile.txt");
	else
		is.open(argv[1]);


	// find total number of testcases
	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;
	//printf("num tc == %d\n", tc);

	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d:\n",i);
		for(int m = 0; m < SZLIM; m++)
			for(int n = 0; n < SZLIM; n++)
			{
				basin[m][n] = 12000;
				res[m][n] = 0;
			}
		ch = 1;

		// find number of lines for this testcase
		int linespertc = 0;
		int colspertc = 0;
		getline(is,s); 
		istringstream iss(s);
		iss >> linespertc >> colspertc;
		int rows = linespertc;
		int r = 1;
		do
		{
			getline(is,s);
			istringstream iss(s); // every line manipulated with ease as iss
			//cout << s << endl;
			for(int c = 1; c <= colspertc; c++)
			{
				iss >> basin[r][c];
			}
			r++;

		}while( --linespertc  ) ;
		process_testcase(rows, colspertc);
		display_output(rows, colspertc);
	}
	is.close();
	return 0;
}