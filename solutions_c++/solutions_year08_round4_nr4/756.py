#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int maxN = 2048;

char s[maxN], s1[maxN];
int p[1000];

void doit(){
	int i, j, k, sl, mn = 100000000, id, nn, pr;
	scanf("%d %s", &k, s);
	sl = strlen(s);
	id = sl / k;
	for(i = 0; i < k; i++) p[i] = i;

	do{
		for(i = 0; i < id; i++){
			for(j = 0; j < k; j++) s1[k*i + j] = s[k*i + p[j]];
		}
		
		pr = 0;
		nn = 1;
		for(i = 1; i < sl; i++)
			if(s1[i] != s1[pr]){
				nn++;
				pr = i;
			}
		//cout << s1 << ' ' << nn << endl;
		mn = min(mn, nn);


	}while(next_permutation(p, p + k));
	cout << mn;
	return;
}

int main(){
	int tst, tc;
	cin >> tst;
	for(tc = 1; tc <= tst; tc++){
		cout << "Case #" << tc << ": ";
		doit();
		cout << endl;
	}
	//system("pause");
	return 0;
}