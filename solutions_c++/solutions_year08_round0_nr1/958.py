// test.cpp : Defines the entry point for the console application.
//
//
#include "stdafx.h"

#include "iostream"
#include "math.h"
#include "string"

#include <algorithm> 
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <climits>

using namespace std;

short casenum;
short caseindex;

int s,q;
map<string,int> srvlist;
string srvname;
short searchlist[1001];
short res[1001][101];

const short maxvalue = 2000;

void doing()
{
	int i,i1,j;
	int temp;
	for (i=1; i<=s; ++i) {
		res[0][i] = 0;
	}
	for (j=1; j<=q; ++j) {
		for (i=1; i<=s; ++i) {
			res[j][i] = maxvalue;
			if (i == searchlist[j]) {
				continue;
			}
			for (i1=1; i1<=s; ++i1) {
				temp = (i1==i)? res[j-1][i1] : res[j-1][i1]+1;
				if (res[j][i] > temp) {
					res[j][i] = temp;
				}
			}			
		}
	}

	int returnvalue = maxvalue;
	for (i=1; i<=s; ++i) {
		if (returnvalue > res[q][i]) {
			returnvalue = res[q][i];
		}
	}
	cout << "Case #" << caseindex << ": " << returnvalue << endl;
}


int main()
{
	int i;

	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	while (cin>>casenum) {
		for (caseindex = 1; caseindex <= casenum; ++caseindex) {
			srvlist.clear();
			cin >> s;
			for (i = 1; i<=s; ++i) {
				getline(cin, srvname, '\n');
				while (srvname.length() == 0) {
					getline(cin, srvname, '\n');
				}
				srvlist[srvname] = i;
			}
			cin >> q;
			searchlist[0] = 0;
			for (i = 1; i<=q; ++i) {
				getline(cin, srvname, '\n');
				while (srvname.length() == 0) {
					getline(cin, srvname, '\n');
				}
				searchlist[i] = srvlist[srvname];
			}

			doing();
		}
	}

	return 0;
}
