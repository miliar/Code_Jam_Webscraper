#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "in.txt"
#define OUTPUT "out.txt"

struct line
{
	int x1,y1,x2,y2;
};

line l[11111];
int el=0;
int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int r=0; r<t; r++) {
		int wsum=0;
		int n; cin >> n;
		char s[32];
		int d;
		int x=0, y=0;
		char dir = 'u';
		int x1=inf, y1=inf, x2=-1, y2=-1;
		el=0;
		int sum=0;
		for (int i=0; i<n; i++) {
			cin >> s >> d;
			for (int u=0; u<d; u++) {
				for (int e=0; e<strlen(s); e++) {
					if (s[e] == 'F') sum++;
					else {
						if (s[e] == 'R') {
							if (sum) {
								l[el].x1 = x;
								l[el].y1 = y;

								if (x < x1) x1 = x;
								if (x > x2) x2 = x;

								if (y < y1) y1 = y;
								if (y > y2) y2 = y;
								switch (dir)
								{
								case 'u': y += sum; break;
								case 'd': y -= sum; break;
								case 'r': x += sum; break;
								case 'l': x -= sum; break;
								}
								l[el].x2 = x;
								l[el].y2 = y;
								el++;

								if (x < x1) x1 = x;
								if (x > x2) x2 = x;

								if (y < y1) y1 = y;
								if (y > y2) y2 = y;

								switch (dir) 
								{
								case 'u': dir = 'r'; break;
								case 'd': dir = 'l'; break;
								case 'r': dir = 'd'; break;
								case 'l': dir = 'u'; break;
								}
								sum=0;
							}
						}
						else {
							if (sum) {
								l[el].x1 = x;
								l[el].y1 = y;

								if (x < x1) x1 = x;
								if (x > x2) x2 = x;

								if (y < y1) y1 = y;
								if (y > y2) y2 = y;
								switch (dir)
								{
								case 'u': y += sum; break;
								case 'd': y -= sum; break;
								case 'r': x += sum; break;
								case 'l': x -= sum; break;
								}
								l[el].x2 = x;
								l[el].y2 = y;
								el++;

								if (x < x1) x1 = x;
								if (x > x2) x2 = x;

								if (y < y1) y1 = y;
								if (y > y2) y2 = y;

								switch (dir) 
								{
								case 'u': dir = 'l'; break;
								case 'd': dir = 'r'; break;
								case 'r': dir = 'u'; break;
								case 'l': dir = 'd'; break;
								}
								sum=0;
							}
						}


					}
				}
			}
		}

		if (sum) {
		l[el].x1 = x;
		l[el].y1 = y;

		if (x < x1) x1 = x;
		if (x > x2) x2 = x;

		if (y < y1) y1 = y;
		if (y > y2) y2 = y;
		switch (dir)
		{
		case 'u': y += sum; break;
		case 'd': y -= sum; break;
		case 'r': x += sum; break;
		case 'l': x -= sum; break;
		}
		l[el].x2 = x;
		l[el].y2 = y;
		el++;

		if (x < x1) x1 = x;
		if (x > x2) x2 = x;

		if (y < y1) y1 = y;
		if (y > y2) y2 = y;

		switch (dir) 
		{
		case 'u': dir = 'r'; break;
		case 'd': dir = 'l'; break;
		case 'r': dir = 'd'; break;
		case 'l': dir = 'u'; break;
		}
		sum=0;
	}


	for (int i=x1; i<x2; i++) {
			for (int u=y1; u<y2; u++) {
				double xx = i+0.5;
				double yy = u+0.5;

				int sum=0;
				for (int e=0; e<el; e++) {
					if (l[e].y1 == l[e].y2 && l[e].y1 > yy) 
						if ((l[e].x1 > xx && l[e].x2 < xx) || (l[e].x1 < xx && l[e].x2 > xx))
						sum++;
				}

				if (sum % 2 == 0) {
					// OutSide
					bool r=false;
					bool ll=false;
			
					for (int ee=0; ee<el; ee++) {
						if (l[ee].y1 == l[ee].y2 && l[ee].y1 > yy &&
							((l[ee].x1 > xx && l[ee].x2 < xx) || (l[ee].x1 < xx && l[ee].x2 > xx))) {
								r = true;
								break;
							}
					}
					for (int e=0; e<el; e++) {
						if (l[e].y1 == l[e].y2 && l[e].y1 < yy && 
							((l[e].x1 > xx && l[e].x2 < xx) || (l[e].x1 < xx && l[e].x2 > xx))) {
								ll = true;
								break;
						}
					}
					if (ll&&r) wsum++;
					else {
						bool u=false;
						bool d=false;
				
						for (int e=0; e<el; e++) {
							if (l[e].x1 == l[e].x2 && l[e].x1 > xx &&
								((l[e].y1 > yy && l[e].y2 < yy) || (l[e].y1 < yy && l[e].y2 > yy))) {
									d = true;
									break;
							}
						}
						for (int e=0; e<el; e++) {
							if (l[e].x1 == l[e].x2 && l[e].x1 < xx && 
								((l[e].y1 > yy && l[e].y2 < yy) || (l[e].y1 < yy && l[e].y2 > yy))) {
									u = true;
									break;
							}
						}

						if (u&&d) wsum++;
					}
				}
			}
		}

		cout << "Case #" << r+1 << ": " << wsum << endl;
	}
	return 0;
}
