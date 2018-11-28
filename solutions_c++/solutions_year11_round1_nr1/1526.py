// GJam.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <algorithm>
#include <set>
#include <assert.h>

#define MAX_STRING_LENGTH 1024

using namespace std;

FILE * oStream =  0, * iStream =0;

ostream& wresult(int i) {return cout << (i == 1?"":"\n") << "Case #" << i <<": ";}
ostream& wtrace() { return cerr << endl << "Trace: ";}
void rl() {fscanf(iStream, "\n");}
void rs() {fscanf(iStream, " ");}
int ir() {int i;	fscanf(iStream, "%d", &i); return i;}
int irl() {int i;	fscanf(iStream, "%d\n", &i); return i;}
string __declspec(noinline) sr(size_t l) { char * s = (char *)alloca(l + 1); s[l] = '\0'; rs(); fread(s, 1, l, iStream); return s;}
string srl(size_t l) {string r(sr(l)); rl(); return r;}
string sr() { static char s[MAX_STRING_LENGTH] = {0}; fscanf(iStream, "%s", s); return s;}
string srl() { static char s[MAX_STRING_LENGTH] = {0}; fscanf(iStream, "%s\n", s); return s;}
char cr() { char c; rs(); fscanf(iStream, "%c", &c); return c;}
char crl() { char c; rs(); fscanf(iStream, "%c\n", &c); return c;}
float fr() { float f; fscanf(iStream, "%f", &f); return f;}
float frl() { float f; fscanf(iStream, "%f\n", &f); return f;}


int i = -1;
#define For(cnt) for (int &i_outer = i, i = 0, i_count = (cnt); i < i_count; ++i)
#define length_of(arr) sizeof(arr) / sizeof(arr[0])

#define it_t iterator
#define cit_t const_iterator

#define zero(arr) memset(&(arr), 0, sizeof(arr))

//#include "big_num.h"
//decimal::type dr() { return decimal::make(sr().c_str()); }
//decimal::type drl() { return decimal::make(srl().c_str()); }

void sollution()
{
	int nums[] ={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
	For(irl())
	{
		int n = ir();
		int pd = ir(); 
		int pg = irl();
		if (pd < 100 && pg == 100)
		{
			wresult(i+1) << "Broken";
			continue;
		}
		if (pd > 0 && pg == 0)
		{
			wresult(i+1) << "Broken";
			continue;
		}
		if (pd == 0)
		{
			wresult(i+1) << "Possible";
			continue;
		}
		int pd1 = pd;
		int pg1 = 100;
		For(4)
		{
			while(pd1 % (nums[i]) == 0 &&
				pg1 % (nums[i]) == 0)
			{
				pd1 /= nums[i];
				pg1 /= nums[i];
			}
		}
		if (pg1 > n) 
		{
			wresult(i+1) << "Broken";
			continue;
		}

		wresult(i+1) << "Possible";
	}
}

int main(int argc, char* argv[])
{
	if (argc > 2)
	{
		oStream = freopen(argv[2], "w", stdout);
	}
	iStream = fopen(argv[1], "r");

	sollution();
	cout << endl;

	if (oStream)
		fclose(oStream);
	if (iStream)
		fclose(iStream);
	return 0;
}

