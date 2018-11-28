#include <iostream>
#include <string>
using namespace std;

void do_case(int n);
char skip[100];
int  work_tbl[1001][101];

int  solve_it();
void deb_print();
int  conv_to_min( const char *time_str );

int main(int , char **)
{
	int  ncases;
	cin >> ncases;
	cin.getline(skip,100);

	for (int i=0; i<ncases; i++)
		do_case(i);

	return 0; 
}

int  in_turnarnd;
int  in_na, in_nb;		
const int WK_MAX = 99999;

void do_case(int n)
{
	//
	// input
	//
	cin >> in_turnarnd;
	cin.getline(skip,100);

	cin >> in_na >> in_nb;
	cin.getline(skip,100);

	char  timetbl_na[101][3][10];
	char  timetbl_nb[101][3][10];
	for (int i=1; i<=in_na; i++)
	{
		cin >> timetbl_na[i][1] >> timetbl_na[i][2];
		cin.getline(skip,110);
	}
	for (int i=1; i<=in_nb; i++)
	{
		cin >> timetbl_nb[i][1] >> timetbl_nb[i][2];
		cin.getline(skip,110);
	}

	//
	// process
	//
	
	//  work table initialization
	int  worktbl_na[1440+100], worktbl_nb[1440+100];
	for (int i=0; i<1440; i++)
		worktbl_na[i] = 0;
	for (int i=0; i<1440; i++)
		worktbl_nb[i] = 0;

	//  A station
	for (int i=1; i<=in_na; i++)
	{
		int min = conv_to_min(timetbl_na[i][1]);
		worktbl_na[min] --;
	}
	for (int i=1; i<=in_nb; i++)
	{
		int min = conv_to_min(timetbl_nb[i][2]);
		min += in_turnarnd;
		worktbl_na[min] ++;
	}

	int  min = WK_MAX;	
	int  sum = 0;
	for (int i=0; i<1440; i++)
	{
		sum += worktbl_na[i];
		if ( min > sum )
			min = sum;
	}
	
	int  ans_A = -min;
	
	//  B station
	for (int i=1; i<=in_nb; i++)
	{
		int min = conv_to_min(timetbl_nb[i][1]);
		worktbl_nb[min] --;
	}
	for (int i=1; i<=in_na; i++)
	{
		int min = conv_to_min(timetbl_na[i][2]);
		min += in_turnarnd;
		worktbl_nb[min] ++;
	}

	min = WK_MAX;	
	sum = 0;
	for (int i=0; i<1440; i++)
	{
		sum += worktbl_nb[i];
		if ( min > sum )
			min = sum;
	}
	
	int  ans_B = -min;

		
			

		
	//
	// output
	//
	cout << "Case #" << n+1 << ": " << ans_A << " " << ans_B << endl;

/*
	cout << "turn arround " << in_turnarnd << endl;
	for (int i=1; i<=in_na; i++)
	{
		cout << timetbl_na[i][1] << " " << timetbl_na[i][2] << endl;
	}
	for (int i=1; i<=in_nb; i++)
	{
		cout << timetbl_nb[i][1] << " " << timetbl_nb[i][2] << endl;
	}
*/
}

int  solve_it()
{
	return  0;
}

void deb_print()
{
	
}

int  conv_to_min( const char *time_str )
{
	int min = atoi(time_str+3);
	int hour = (time_str[0]-'0')*10 + (time_str[1]-'0');
	return  hour*60 + min;
}
