
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))
#define ABS(a) ((a)>(0))?(a):(a)


class CSolver
{
public:
	bool  virtual ReadData()
	{
		return false;
		//reading data
	};
	void  virtual Solve()
	{
		if (!ReadData())
			printf("error");
		
		printf("%f ","something");

	};
	
};

class AA
{
public:
	 AA()
	{
		mtran[0]='y';//a
		mtran[1]='h';//b
		mtran[2]='e';//c
		mtran[3]='s';//d
		mtran[4]='o';//e
		mtran[5]='c';//f
		mtran[6]='v';//g
		mtran[7]='x';//h
		mtran[8]='d';//i
		mtran[9]='u';//j
		mtran[10]='i';//k
		mtran[11]='g';//l
		mtran[12]='l';//m
		mtran[13]='b';//n
		mtran[14]='k';//o
		mtran[15]='r';//p
		mtran[16]='z';//q
		mtran[17]='t';//r
		mtran[18]='n';//s
		mtran[19]='w';//t
		mtran[20]='j';//u
		mtran[21]='p';//v
		mtran[22]='f';//w
		mtran[23]='m';//x
		mtran[24]='a';//y
		mtran[25]='q';//z
	};
	bool  virtual ReadData()
	{
		return false;
		//reading data
	};
	void   Solve()
	{
		char ch;
		do 
		{
			scanf("%c", &ch);
			if (ch==char(10))
			{
				  printf("\n");
				break;
			}
			if (ch==32)
				  printf(" ");
			if ((ch>=97) && (ch<=122))
				  printf("%c", mtran[ch-97]);

		}while(true);
		
	};
	
	char mtran[26];
	
};


class CC
{
public:
	bool  virtual ReadData()
	{
		return false;
		//reading data
	};
	void   Solve()
	{
		ReadData();

	}
	int Perms(int a_m,int a_from,int a_to)
	{
		int perms=0;

	}

};
		

int main(int argc, char ** argv) {
   int t;
    char c;
	AA solver;
   char endofline;
   scanf("%d", &t);
   scanf("%c", &endofline);
   rep (i, t) {
       printf("Case #%d: ", i+1);
	 
	   
	    solver.Solve();

       printf("\n");
   }
   return 0;
}