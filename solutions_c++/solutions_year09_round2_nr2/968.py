#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cmath>
#define INF 21474836
using namespace std;

int H,W;
char now;
int board[102][102];

int main()
{
	//FILE *in  = fopen("B-small-attempt1.in","r");
	//FILE *out = fopen("B-small-attempt1.out","w");
	ifstream in("B-small-attempt1.in");
	ofstream out("B-small-attempt1.out");
	int tests;
	in >> tests;
	string num;
	for(int t = 0; t<tests; t++){
		vector<bool> tiene(12,false);
		printf("caso %d\n",t);
		in >> num;
		string now = num;
		next_permutation(now.begin(),now.end());
		if(now>num) 
			out << "Case #" << t+1 << ": " << now << endl;
		else{
			string ret;
			string nowTemp;
			int cantZeros = 0;
			for(int i =0 ; i<now.size(); i++) {
				if(now[i] == '0') cantZeros++;
				else nowTemp += now[i];
			}
			sort(nowTemp.begin(),nowTemp.end());
			ret += nowTemp[0];
			for(int j = 0; j<=cantZeros; j++)
				ret += '0';
			for(int i = 1; i<nowTemp.size(); i++) 
				ret += nowTemp[i];
			out << "Case #" << t+1 << ": " << ret << endl;
		}
	}
    return EXIT_SUCCESS;
}

