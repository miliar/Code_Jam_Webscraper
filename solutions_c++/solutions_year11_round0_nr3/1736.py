#include<iostream>
using namespace std;


void run();
void qsort(int[],int,int);
int sean[1001];
int part[1001];
int candy[1001];

int main () {
    freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int credits;
	cin >> credits;
	for (int i = 0; i < credits; ++ i) {
		cout <<"Case #"<<i+1<<": ";
		run();
	}
	return 0;
}

void run() {
	int N;
	cin >> N;
	for (int i = 0; i < 1002; ++ i) {
		part[i] = candy[i] = -1;
	}
	for (int i =0; i < N; ++ i) 
		cin >> candy[i];
	qsort(candy, 0, N - 1);
	int sw = 0, pw = 0;
	int sf = 0, pf = 0;
	for (int i = 0; i < N; ++ i) {
		sw += candy[i];
		sf ^= candy[i];
	}
	if (sf != 0) {
		cout << "NO" << endl;
		return;	
	}
	sw -= candy[0];
	sf ^= candy[0];
	pf ^= candy[0];
	//int half = sw/2;
	int ptop = 0;
	int pcur = 0, scur = 0;
	while (sw != 0) {
		if (sf == pf) {
			cout << sw << endl;
			return;
		}
		for (pcur = part[ptop] + 1; pcur < N; ++ pcur) {
			pf ^= candy[pcur];
			sf ^= candy[pcur];
			if (pf == sf) {
				sw -= candy[pcur];
				cout << sw << endl;
				return;
			}
			pf ^= candy[pcur];
			sf ^= candy[pcur];
		}
		++ part[ptop];
		if (part[ptop] == N) {
			if (ptop != 0)
				part[ptop] = part[ptop - 1] + 1;
			else
				part[0] = 0;
			sw -= candy[part[ptop]];
			pf ^= candy[part[ptop]];
			sf ^= candy[part[ptop]];
			++ ptop;
			part[ptop] = part[ptop - 1] + 1;
		}
	}
	cout << "NO" << endl;
}


void qsort(int s[],int begin,int end) {//quick sort for int array
	if (begin == end)
		return;
	int i = begin, j = end;
	int x = s[rand() % (end - begin + 1) + begin];
	do {
		while (x < s[j]) -- j;
		while (s[i] < x) ++ i;
		if (i <= j) {
			int t = s[i];
			s[i] = s[j];
			s[j] = t;
			++ i;
			-- j;
		}
	} while (i <= j);
	if (begin < j) qsort(s,begin,j);
	if (i < end) qsort(s,i,end);
}
