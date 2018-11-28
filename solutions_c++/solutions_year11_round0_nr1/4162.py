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

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
template <class T> inline string itos(T n) {return (n)<0?"-"+itos(-(n)):(n)<10?(string)("")+(char)('0'+(n)):itos((n)/10)+itos((n)%10);}

int case_number;
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

void main2(void){

	queue<char> order;
	queue<int> orange, blue;
	int pos, i;
	char ch;
	int number_buttons;
	cin >> number_buttons;
	REP(i, number_buttons) {

		cin >> ch;
		cin >> pos;
		order.push(ch);
		if(ch == 'O')
			orange.push(pos);
		else
			blue.push(pos);
	}

	char turn;
	int opos = 1;
	int bpos = 1;
	long timer=0;
	while(order.size() > 0) {

		turn = order.front();
		if(opos > orange.front())
			opos--;
		else if(opos < orange.front())
			opos++;
		else if(turn == 'O') {
			orange.pop();
			order.pop();
		}

		if(bpos > blue.front())
			bpos--;
		else if(bpos < blue.front())
			bpos++;
		else if(turn == 'B') {
			blue.pop();
			order.pop();
		}
		timer++;
	}
	gout << timer << "\n";
}

int main(void){
	int number_of_test_cases,i;
	cin >> number_of_test_cases;
	REP(i,number_of_test_cases) main2();
	return 0;
}
