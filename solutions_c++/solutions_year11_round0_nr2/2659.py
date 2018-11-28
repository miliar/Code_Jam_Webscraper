#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

ifstream in;
ofstream out;
string ans;
void work();
int main()
{
	in.open("smallb.in");
	out.open("out.out");
	int t;
	in>>t;
	for (int i = 0; i < t; i++) {
		out << "Case #" << i + 1 << ": ";
		ans = string("");
		work();
		out<< ans <<endl;
	}
	return 0;
}
void work()
{
	map <string, string> comb;
	set <string> oppo;
	int cn, on;
	string tmp;
	in >> cn;
	for (int i = 0; i < cn; i++) {
		in>>tmp;
		string front = tmp.substr(0,2);
		string end = tmp.substr(2,1);
		comb[front] = end;
	}
	in >> on;
	for (int i = 0; i < on; i++) {
		in>>tmp;
		oppo.insert(tmp);
	}
	in>>cn;
	in>>tmp;
	for (int i = 1; i < tmp.size();) {
		string s1,s2,s3;
		s1 = tmp.substr(i-1,2);
		s2 = tmp.substr(i,1) + tmp.substr(i-1,1);
		if (comb.count(s1) || comb.count(s2)) {
			if(comb.count(s1)){
				cout<<s1<<" ";
				tmp.replace(i-1,2, comb[s1]);
				cout<<tmp<<endl;
			} else if (comb.count(s2)) {
				cout<<s2<<" ";
				tmp.replace(i-1,2, comb[s2]);
				cout<<tmp<<endl;
			}
			i = 1;
			continue;
		} 
		s1 = tmp.substr(i,1);
		for (int j = i - 1; j >= 0; j--) {
			s2 = tmp.substr(j, 1);
			s3 = s1 + s2;
			string s4 = s2 + s1;
			if (oppo.count(s3) || oppo.count(s4)) {				
				//tmp.erase(j, i - j + 1);
				tmp.erase(0, i+1);
				i = 0;
				break;
			}
			
		}
		i++;
	}
	ans = string("[");
	for (int i = 0; i + 1< tmp.size(); i++) {
		ans += tmp[i];
		ans += string(", ");
	}
	if(tmp.size() != 0)
		ans += tmp[tmp.size() - 1];
	ans += string("]");
}

