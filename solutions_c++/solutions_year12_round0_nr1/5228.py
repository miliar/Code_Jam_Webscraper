#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <vector>
#define MAX_N 50010
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
using namespace std;

char T[MAX_N];
int n;
int RA[MAX_N], tempRA[MAX_N];
int SA[MAX_N], tempSA[MAX_N];
int c[MAX_N];
int Phi[MAX_N], PLCP[MAX_N], LCP[MAX_N];

char getC(char a)
{
	switch (a) {		
		case 'a':
			return 'y';
		case 'b':
			return 'h';
		case 'c':
			return 'e';
		case 'd':
			return 's';
		case 'e':
			return 'o';
		case 'f':
			return 'c';
		case 'g':
			return 'v';
		case 'h':
			return 'x';
		case 'i':
			return 'd';
		case 'j':
			return 'u';
		case 'k':
			return 'i';
		case 'l':
			return 'g';
		case 'm':
			return 'l';
		case 'n':
			return 'b';
		case 'o':
			return 'k';
		case 'p':
			return 'r';
		case 'q':
			return 'z';
		case 'r':
			return 't';
		case 's':
			return 'n';
		case 't':
			return 'w';
		case 'u':
			return 'j';
		case 'v':
			return 'p';			
		case 'w':
			return 'f';
		case 'x':
			return 'm';
		case 'y':
			return 'a';
		case 'z':
			return 'q';
	}
	return a;

}

int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);  
	string str="";
	cin >> n;
	FR(j,n)
	{
	while(str=="")getline(cin,str);
	cout << "Case #" << j+1 << ": ";
		FR(i,str.length()) cout << getC(str[i]);
		cout << endl;
	str="";
	}
    return 0;
}
