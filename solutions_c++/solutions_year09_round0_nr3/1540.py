#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <list>
#include <map>
#include <set>
using namespace std;

unsigned int TC, tc;
long long ans;
string str, welcome = "welcome to code jam";//"jam";
char str2[500], *welcome2 = "welcome to code jam";//"jam";
set<char> chars;
string zeros;
long long soln[19][500];

void trim(string &str){
	//trim in backward direction
	string::reverse_iterator ir = str.rbegin();
	string::reverse_iterator jr = welcome.rbegin();
	chars.clear();
	while(ir != str.rend()){
		while((ir != str.rend()) && (*ir != *jr)){
			if(chars.find(*ir) == chars.end())
				str.erase((ir+1).base());
			++ir;
		}
		if(ir != str.rend())//that is, *i == *j
		{
			chars.insert(*jr);
			++ir;
		}
		++jr;
		if(jr == welcome.rend())
			--jr;
	}
	
	//trim in forward direction
	string::iterator i = str.begin();
	string::iterator j = welcome.begin();
	chars.clear();
	while(i != str.end()){
		while((i != str.end()) && (*i != *j)){
			if(chars.find(*i) == chars.end())
				str.erase(i);
			else
				++i;
		}
		if(i != str.end())//that is, *i == *j
		{
			chars.insert(*j);
			++i;
		}
		++j;
		if(j == welcome.end())
			--j;
	}
}

void solve(int wi, int si){
	if(*(welcome2+wi) != *(str2+si))
		cout << endl << "ASSERT FAILED" << endl;

	if(strlen(str2+si) < strlen(welcome2+wi)){
		soln[wi][si] = 0;
		return;
	}

	if(strcmp(welcome2+wi, str2+si) == 0){
		soln[wi][si] = 1;
		return;
	}

	//call for solve(w, s+1)
	int s1 = si+1;
	long long sum = 0;
	while(*(str2 + s1) && (*(str2 + s1) == *(str2 + si))){//to optimize repetition of chars
		++s1;
	}
	while(*(str2 + s1) && (*(str2 + s1) != *(welcome2+wi)))
		s1++;
	if(*(str2 + s1)){
		if(soln[wi][s1] == -1)
			solve(wi, s1);
		sum = (sum+ soln[wi][s1]%10000)%10000;
	}

	s1 = si+1;
	int factor = 1;
	while(*(str2 + s1) && (*(str2 + s1) == *(str2 + si))){//to optimize repetition of chars
		++s1;
		++factor;
	}
	if(*(welcome2+wi+1) == 0)
		sum += factor;//last matching char
	else {//call for solve(w+1, s+1)
		while(*(str2 + s1) && (*(str2 + s1) != *(welcome2+wi+1)))
			s1++;
		if(*(str2 + s1)){
			if(soln[wi+1][s1] == -1)
				solve(wi+1, s1);
			sum = (sum + (soln[wi+1][s1] * factor)%10000 ) % 10000;
		}
	}

	soln[wi][si] = sum;
	return;
}

int main(){
	unsigned int i, j;
	cin >> TC;
	getline(cin, str);
	for(tc=0; tc<TC; ++tc){
		getline(cin, str);
		trim(str);
		str.copy(str2, str.size()+1);
		str2[str.size()]=0;
		ans = 0;
		soln[0][0] = -1;
		for(j=0; j < str.size(); j++){
			for(i=0; i<19; i++){
				soln[i][j] = -1;
			}
		}
		if(str.size()){
			solve(0, 0);
			ans = soln[0][0] % 10000;
		} else
			ans = 0;
		zeros = (ans > 999) ? "" : (ans > 99) ? "0" : (ans > 9) ? "00" : "000";
		cout << "Case #" << tc+1 << ": " << zeros << ans << endl;
	}
	return 0;
}
