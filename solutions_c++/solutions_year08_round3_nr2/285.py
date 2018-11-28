/*#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <strstream>
#include <cmath>
#include <bitset>

using namespace std;


int res(0);
void proc(string num, int curpos,string keep, int curValue)
{
	if(curpos == num.length())
	{
		int tmp = atoi(keep.c_str());
		curValue += tmp;
		if(curValue % 2 == 0 ||
			curValue % 3 == 0 ||
			curValue % 5 == 0 ||
			curValue % 7 == 0 )
			res++;
		return;
	}
	proc(num, curpos+1,keep+num[curpos],curValue);
	proc(num, curpos+1,num.substr(curpos,1),curValue+atoi(keep.c_str()));
	proc(num,curpos+1, (string)"-"+num[curpos], curValue+atoi(keep.c_str()));
}
int main()
{
	int casenum;
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	fin >> casenum;
	for(int ind = 1; ind <= casenum; ind++)
	{
		string number;
		fin >> number;
		res = 0;
		proc(number,1,number.substr(0,1),0);
		fout << "Case #" << ind << ": " << res << endl;;
	}
	return 0;
}
*/
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <vector>
#include <queue>
using namespace std;

fstream fin("B-small.in",ios::in);
fstream fout("B-small.out",ios::out);

string num;
__int64 str2int(int s, int e) {
	int i;
	__int64 res(0);
	for (i=s; i<=e; i++) {
		res = res*10+num[i]-'0';
	}
	return res;
}

int main() {
	int caseNum, caseNo;
	fin>>caseNum;
	for (caseNo=1; caseNo<=caseNum; caseNo++) {
		fout<<"Case #"<<caseNo<<": ";
		//add code here
		fin>>num;
		int op[100];
		int res(0), i;
		__int64 tmp;
		tmp = 0;
		int len = num.size()-1;
		int ugly[4] = {2,3,5,7};
		for (i=0; i<len; i++)
			op[i] = 0;
		bool out = true;
		while(out) {
			tmp = 0;
			int s(0), e(0);
			__int64 n;
			for (i=0; i<len; i++)
				if (op[i])
					break;
			e = i;
			tmp = str2int(s,e);
			s = e+1;
			int opp = op[i];
			for (; i<len; i++) {
				if ( !op[i] )
					continue;
				e = i;
				n = str2int(s,e);
				if ( opp == 1)
					tmp += n;
				else if ( opp == 2)
					tmp -= n;
				s = e+1;
				opp = op[i];
			}
			e = len;
			n = str2int(s,e);
			if ( s == 0 )
				tmp = n;
			else if ( opp == 1)
				tmp += n;
			else if ( opp == 2)
				tmp -= n;
			//	if ( !len )
			//		tmp = str2int(0,0);
			if ( tmp < 0 )
				tmp = -tmp;
			for (i=0; i<4; i++)
				if ( tmp%ugly[i] == 0 )
					break;

			if (i != 4) {

				res++;
			}

			out = false;
			for (i=0; i<len; i++)
				if ( op[i] != 2)
					out = true;
			for (i=0; i<len; i++) {

				if (op[i] == 2) {
					op[i] = 0;
				}else {
					op[i]++;
					break;
				}
			}
		}
		fout<<res<<endl;
	}
	return 0;
}
/*
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <strstream>
#include <cmath>
#include <bitset>

using namespace std;


int res(0);
void proc(string num, int curpos,string keep, int curValue)
{
if(curpos == num.length())
{
int tmp = atoi(keep.c_str());
curValue += tmp;
if(curValue % 2 == 0 ||
curValue % 3 == 0 ||
curValue % 5 == 0 ||
curValue % 7 == 0 )
res++;
return;
}
proc(num, curpos+1,keep+num[curpos],curValue);
proc(num, curpos+1,num.substr(curpos,1),curValue+atoi(keep.c_str()));
proc(num,curpos+1, (string)"-"+num[curpos], curValue+atoi(keep.c_str()));
}
int main()
{
int casenum;
ifstream fin("B-small.in");
ofstream fout("B-small.out");
fin >> casenum;
for(int ind = 1; ind <= casenum; ind++)
{
string number;
fin >> number;
res = 0;
proc(number,1,number.substr(0,1),0);
fout << "Case #" << ind << ": " << res << endl;;
}
return 0;
}*/

