
#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<sstream>

using namespace std;



int basin[102][102];
long res[102][102];
long ch = 'a';

void display_output(int r, int c)
{
	// display output
	for(int i = 1; i <= r; i++)
	{
		for(int j = 1; j <= c; j++)
		{
			if(j > 1)
				cout << " ";
			cout << (char)res[i][j];
		}
		cout << endl;
	}
}

bool iamasink(int r, int c)
{
	// if i cannot flow i am a sink
	bool rv = false;
	int me = basin[r][c];
//	printf("checking if sink[%d][%d]\n", r, c);

	if( (me <= basin[r-1][c]) && (me <= basin[r][c-1]) && (me <= basin[r+1][c]) && (me <= basin[r][c+1]) )
		rv = true;
//	if(rv)
//		printf("sink[%d][%d]\n", r, c);
	return rv;
}

void resolve_conflict(long l1, long l2)
{
	long ll = min(l1,l2);
	long lh = max(l1,l2);
	ch--;
	//printf("conflict between <%c> && <%c>\n", ll, lh);
	for(int i = 1; i < 102; i++)
		for(int j = 1; j < 102; j++)
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

	if('0' == res[nr][nc])
		res[nr][nc] = res[r][c];
	else
		resolve_conflict(res[nr][nc], res[r][c]);

	//printf("[%d][%d] flows into [%d][%d]\n", r,c,nr,nc);
}

void process_testcase(int r, int c)
{
	//res[1][1] = 'a';
	//flow(1,1);
	//printf(" processing %d rows and %d cols\n", r, c);
	// process input and generate output
	for(int i = 1; i <= r; i++)
	{
		for(int j = 1; j <= c; j++)
		{
			//printf(" now[%d][%d]\n", i, j);

			// only 2 things to do
			// 1st get my basin label
			// 2nd. flow on

			if('0' == res[i][j])// no label? get new
			{
				res[i][j] = ch;
				ch++; // create a new basin label
			}
			flow(i,j);
			//display_output(r, c);
		}
	}
}

int main(int argc, const char *argv[])
{
	//cout << "Hello World\n";

	int tc = 0;
	//bool new_tc = true;
	ifstream is;
	is.open("c:\\users\\viv.NORTHAMERICA\\Downloads\\b-large.in");

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
		for(int m = 0; m < 102; m++)
			for(int n = 0; n < 102; n++)
			{
				basin[m][n] = 12000;
				res[m][n] = '0';
			}
		ch = 'a';

		// find number of lines for this testcase
		int linespertc = 0;
		int colspertc = 0;
		getline(is,s); 
		istringstream iss(s);
		iss >> linespertc >> colspertc;
		int rows = linespertc;
		int r = 1;
		//printf("%s lies %d, cols %d\n", s.c_str(), linespertc, colspertc);
		do
		{
			getline(is,s);
			istringstream iss(s); // every line manipulated with ease as iss
			//cout << s << endl;
			for(int c = 1; c <= colspertc; c++)
			{
				iss >> basin[r][c];
			//	 printf("(%d) ", basin[r][c]);
			}
			r++;
			 //cout << "\n";

		}while( --linespertc  ) ;
		process_testcase(rows, colspertc);
		display_output(rows, colspertc);
	}
	is.close();
	return 0;
}