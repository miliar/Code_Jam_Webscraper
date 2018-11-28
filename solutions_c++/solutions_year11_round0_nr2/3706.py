#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <list>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

void main2(void){

	map<string, char> combineMap;
	map<char, char> opposMap;
	list<char> output;
	list<char>::iterator iterOut;
	int C,D,N, i;
	cin >> C;
	string combine, temp, input;
	REP(i, C) {
		cin >> combine;
		temp.clear();
		temp += combine[0];
		temp += combine[1];
		combineMap[temp] = combine[2];
		temp.clear();
		temp += combine[1];
		temp += combine[0];
		combineMap[temp] = combine[2];
	}
	cin >> D;
	string oppos;
	REP(i, D) {
		cin >> oppos;
		opposMap[oppos[0]] = oppos[1];
		opposMap[oppos[1]] = oppos[0];
	}
	cin >> N;
	if(N > 0) {
		cin >> input;
		output.push_back(input[0]);
		for(i=1;i<N;i++) {
			temp.clear();
			temp += output.back();
			temp += input[i];
			if(combineMap.find(temp) != combineMap.end()) {
				output.pop_back();
				output.push_back(combineMap[temp]);
			}
			else {
				bool found = false;
				for(iterOut=output.begin();iterOut!=output.end();iterOut++) {
					if(*iterOut == opposMap[input[i]]) {
						found = true;
						output.clear();
						break;
					}
				}
				if(!found) output.push_back(input[i]);
			}
		}
		gout << "[";
		int count = output.size();
		int num = 0;
		for(iterOut=output.begin();iterOut!=output.end();iterOut++) {
			num++;
			cout << *iterOut;
			if(num != count)
				cout << ", ";
		}
		cout << "]\n";
	}
	else {
		gout << "[]\n";
	}
}

int main(void){
	int number_of_test_cases,i;
	cin >> number_of_test_cases;
	REP(i,number_of_test_cases) main2();
	return 0;
}
