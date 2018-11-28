// solution for 

#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <cassert>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#include <cstdio>
#include <map>
#include <deque>
#include <vector>
#include <set>
#include <cstring>
#include <algorithm>
#include <iomanip>

using namespace std;

// setiosflags(ios¡Ëscientific)
// setw()
// setfill('x')
// setioflags(ios::showpos)
// setiosflags(ios¡Ëright)

#define COUT_HEX(x) hex << x
#define COUT_F_PRE(n,f) setiosflags(ios::fixed)<<setprecision(n)<<f
#define ZERO(n) memset(n,0,sizeof(n))
#define M1SET(n) memset(n,-1,sizeof(n))
#define MIN(m,n) ((m<n)?m:n)
#define MAX(m,n) ((m>n)?m:n)

#define UL unsigned long long
#define UI unsigned int
#define LL long long

#define FOR(i,a,b)   for(LL(i) = (LL)(a);(i) < (LL)(b);(i)++)
#define FOREQ(i,a,b) for(LL(i) = (LL)(a);(i) <= (LL)(b);(i)++)
#define RFOR(i,a,b)  for(LL(i) = (a), _b(b);(i) >= _b; --(i))
//#define FOREACH(c,itr) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end();itr++)
#define ALL(a)   (a).begin(),(a).end()
#define SZ(a)	 ((int)(a).size())

#define MO 1000000007UL

#define MOD(i) (i = ((i >= MO) ? i%MO : i))

string s[4];

bool check(char c)
{
	FOR(i,0,4)
	{
		if((s[i][0] == c || s[i][0] == 'T') &&
			(s[i][1] == c || s[i][1] == 'T') && 
			(s[i][2] == c || s[i][2] == 'T') &&
			(s[i][3] == c || s[i][3] == 'T')
			)
			return true;
		else if((s[0][i] == c || s[0][i]  == 'T') &&
			(s[1][i] == c || s[1][i]  == 'T')&&
			(s[2][i] == c || s[2][i]  == 'T')&&
			(s[3][i] == c || s[3][i]  == 'T'))
			return true;
	}

	if((s[0][0] == c || s[0][0]  == 'T')&&
		(s[1][1] == c || s[1][1]  == 'T')&&
		(s[2][2] == c || s[2][2]  == 'T')&&
		(s[3][3] == c || s[3][3]  == 'T'))
		return true;

		if((s[0][3] == c || s[0][3]  == 'T')&&
		(s[1][2] == c || s[1][2]  == 'T')&&
		(s[2][1] == c || s[2][1]  == 'T')&&
		(s[3][0] == c || s[3][0]  == 'T'))
		return true;

	return false;
}

bool checkComp( void)
{
	FOR(i,0,4)
		FOR(j,0,4)
	{
		if(s[i][j] == '.')
		{
			return true;
		}
	}
	return false;
}

bool solve(istream &in,ostream &out)
{
	LL T;
	in >> T;


	FOR(i,0,T)
	{
		
		int outCome = 0;
		in >> s[0]>>s[1]>>s[2]>>s[3];

		if(check('X'))
			outCome = 1;
		else if(check('O'))
			outCome = 2;
		else if(checkComp())
			outCome = 4;
		else
			outCome = 3;


		out << "Case #"<<i+1<<": ";
		switch(outCome)
		{
			case 1:
				out << "X won";
				break;
			case 2:
				out << "O won";
				break;
			case 3:
				out << "Draw";
				break;
			case 4:
				out << "Game has not completed";
				break;
		}
		out << endl;
	}

	return true;
}


int main()
{
	bool bSolved;
	time_t timeBegin = time(NULL);

	#ifndef ONLINE_JUDGE
	ifstream in("in.txt");
	ofstream out("out.txt");
	bSolved = solve(in,out);
	#else
	bSolved = solve(cin,cout);
	#endif
	

	#ifndef ONLINE_JUDGE
	in.close();
	if(!bSolved)
		cout << "not solved Time: " << time(NULL) - timeBegin << endl;
	else
		cout << "solved Time:" << time(NULL) - timeBegin <<endl;
	system("pause");
	#endif
	
	return 0;
}
