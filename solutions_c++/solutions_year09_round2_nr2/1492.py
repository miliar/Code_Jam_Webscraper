#include <cstdio>
#include <deque>
#include <set>
#include <algorithm>
using namespace::std;

void getDigits(int n, deque<int> &l)
{
	int i,j;
	while (n > 0) {
		i = n%10;
		l.push_back(i);
		n/=10;
	}
}

int changeIntoNumber(deque<int> l)
{
	int i,num, d;
	num = 0;

	while (!l.empty()) {
		
		i = l.front();
		l.pop_front();
		num = num*10 + i; 	
	}
	return num;
}

int main() {
	int n,t,i,j,k;
	set <int> A;
	set <int> ::iterator it;
	deque <int> ::iterator iter;
	deque <int> l;

	scanf("%d", &t);
	for(i=0;i<t;i++) {
		scanf("%d",&n);
		l.clear();
		A.clear();
		getDigits(n, l);

		A.insert(n);
		while(next_permutation(l.begin(), l.end())) {
				k =  changeIntoNumber(l);
				A.insert(k);
		}
		while(next_permutation(l.begin(), l.end())) {
				k =  changeIntoNumber(l);
				A.insert(k);
		}
		it = A.find(n);
		it++;
		if (it == A.end() ) {
			l.push_back(0);

			while (next_permutation(l.begin(), l.end())) {
				k = changeIntoNumber(l);
				A.insert(k);
			}

			while (next_permutation(l.begin(), l.end())) {
				k = changeIntoNumber(l);
				A.insert(k);
			}
	
			it = A.find(n);
			it++;
		}

		printf("Case #%d: %d\n",i + 1,*it);
		it++;
	}


	return 0;
}

