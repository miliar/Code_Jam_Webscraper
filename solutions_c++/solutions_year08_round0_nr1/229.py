#include <iostream>
#include <string>
using namespace std;

void do_case(int n);
char skip[100];
int  work_tbl[1001][101];

int  solve_it();
void deb_print();

int main(int , char **)
{
	int  ncases;
	cin >> ncases;
	cin.getline(skip,100);

	for (int i=0; i<ncases; i++)
		do_case(i);

	return 0; 
}

int  in_s;
int  in_q;		
const int WK_MAX = 99999;

void do_case(int n)
{
	//
	// input
	//
	cin >> in_s;
	cin.getline(skip,100);

	char  sch_eng[101][110];
	for (int i=1; i<=in_s; i++)
		cin.getline(sch_eng[i],110);

	cin >> in_q;
	cin.getline(skip,100);

	char  query[1001][110];
	for (int i=1; i<=in_q; i++)
		cin.getline(query[i],110);

	//
	// process
	//

	
	//  work table initialization
	for (int i=0; i<in_q; i++)
		for (int j=1; j<=in_s; j++)
			work_tbl[i][j] = 0;
	for (int j=1; j<=in_s; j++)
		work_tbl[in_q][j] = WK_MAX;

	//  build query matrix in numeric
	for (int i=1; i<=in_q; i++)
	{
		int j;
		for (j=1; j<=in_s; j++)
			if ( strcmp(query[i], sch_eng[j]) == 0 )
				break;
		if ( j<=in_s )
			work_tbl[i][j] = i;
	}

	//  fill with next query position
	for (int j=1; j<=in_s; j++)
	{
		int copy = work_tbl[in_q][j];
		for (int i=in_q-1; i>=0; i--)
		{
			if ( work_tbl[i][j] == 0 )
				work_tbl[i][j] = copy;
			else
				copy = work_tbl[i][j];
		}
	}
	
	int nSwitch = solve_it();
	
		
	//
	// output
	//
	cout << "Case #" << n+1 << ": " << nSwitch << endl;
/*
	cout << in_s << " search engines" << endl;
	for (int i=1; i<=in_s; i++)
		cout << "[" << sch_eng[i] << "]" << endl;

	cout << in_q << " queries" << endl;
	for (int i=1; i<=in_q; i++)
		cout << "[" << query[i] << "]"  << endl;
*/
}


int  solve_it()
{
	
	
	
	//  alternated dijkstra algorithm
	
	for (int i=1; i<=in_q; i++)
		work_tbl[i][0] = WK_MAX;
	work_tbl[0][0] = 0;

//deb_print();
	for (int cur_val = 0; cur_val<=in_q; cur_val++)
	{
		for (int cur_pos=0; cur_pos<=in_q; cur_pos++)
		if ( work_tbl[cur_pos][0] == cur_val )
			for (int j=1; j<=in_s; j++)
			{
				int next_pos = work_tbl[cur_pos][j];
				if ( next_pos == cur_pos )
					continue;
				if ( next_pos == WK_MAX )
					return  cur_val; // found short path
				if ( work_tbl[next_pos][0] > cur_val + 1 )
					work_tbl[next_pos][0] = cur_val + 1;
			}
//deb_print();

	}
	
	return  WK_MAX;
}


void deb_print()
{
	for (int i=1; i<=in_q; i++)
	{
		for (int j=0; j<=in_s; j++)
			if ( work_tbl[i][j] == WK_MAX )
				cout << "* ";
			else
				cout << work_tbl[i][j] <<" ";	
		cout << endl;
	}
}