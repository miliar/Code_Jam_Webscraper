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

long long maxA = -1, total;
int N, levelNow = 0;
long cValue[1001];
long temp[1000];

void main3(int level, int start, int end) {

	if(level != -1) {
		for(int i=start;i<end;i++) {
			temp[level] = cValue[i];
			main3(level-1, i+1, end);
		}
	}
	else {
		long long sumA = 0, sumB = 0;
		long exA = 0, exB = 0;
		int j = 0, k;
		for(k=N-1;k>=0;k--) {
			if(j==levelNow) break;
			if(temp[j] == cValue[k]) {
				sumA += cValue[k];
				exA ^= cValue[k];
				j++;
			}
			else
				exB ^= cValue[k];
		}
		for(;k>=0;k--) exB ^= cValue[k];
		sumB = total - sumA;
		if(sumB > sumA)
			if(sumA == (long)exB)
				if(maxA < sumB)
					maxA = sumB;
		if(sumB <= sumA)
			if(sumB == (long)exA)
				if(maxA < sumA)
					maxA = sumA;
	}
}

void main2(void){

	int i;
	maxA = -1;
	total = 0;
	levelNow = 0;
	cin >> N;
	REP(i, N) {
		cin >> cValue[i];
		total += cValue[i];
	}
	REP(i, N/2) {
		levelNow++;
		main3(i, 0, N);
	}
	if(maxA == -1) gout << "NO\n";
	else gout << maxA << "\n";
}

int main(void){
	int number_of_test_cases,i;
	cin >> number_of_test_cases;
	REP(i,number_of_test_cases) main2();
	return 0;
}
