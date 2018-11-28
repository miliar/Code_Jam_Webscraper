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

void sollution()
{
	For(irl())
	{
		int ms = irl();
		typedef vector<vector<int>> m_t; // [x,y]
		vector<int> counts(ms, 0);
		vector<double> wp(ms, .0);
		m_t mp(ms, vector<int>(ms, 0));
		For(ms)
		{
			For(ms)
			{
				switch(cr())
				{
				case '1':
					mp[i_outer][i] = 1;
					counts[i_outer]++;
					wp[i_outer]++;
					break;
				case '0':
					mp[i_outer][i] = -1;
					counts[i_outer]++;
					break;
				}
			}
			wp[i] /= (double)counts[i];
			rl();
		}
		vector<double> owp(ms, .0);
		For(ms)
		{
			bool tg = false;
			For(ms)
			{
				double d = wp[i];
				switch(mp[i_outer][i])
				{
					case 1:
						d = (d * counts[i]) / (double)(counts[i] - 1);
						break;
					case -1:
						d = (d * counts[i] - 1) / (double)(counts[i] - 1);
						break;
					default:
						d = .0;
						break;
				}
				owp[i_outer]+=d;
			}
			owp[i] /= (double)counts[i];			
		}
		vector<double> oowp(ms, .0);
		wresult(i+1);
		For(ms)
		{
			For(ms)
			{
				if (mp[i_outer][i])
				{
					oowp[i_outer]+=owp[i];
				}
			}
			oowp[i] /= (double)counts[i];
			// 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
			cout << endl << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
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

