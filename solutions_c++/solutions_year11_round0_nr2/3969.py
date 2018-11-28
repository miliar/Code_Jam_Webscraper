#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

int C, D, N;
char comb[40][4], dele[30][3], data[102];

void Input() {
    scanf("%d", &C);
    for (int i=0; i<C; ++i) {
	scanf("%s", comb[i]);
    }
    scanf("%d", &D);
    for (int i=0; i<D; ++i) {
	scanf("%s", dele[i]);
    }
    scanf("%d", &N);
    scanf("%s", data);

    /*
    cout << "C:" << endl;
    for (int i=0; i<C; ++i)
	printf("%s\n", comb[i]);
    cout << "D:" << endl;
    for (int i=0; i<D; ++i)
	printf("%s\n", dele[i]);
    cout << "N:" << endl;
    printf("%s\n", data);
    */
}

int FindComb(char a, char b) {
    for (int i=0; i<C; ++i) {
	if ((comb[i][0] == a && comb[i][1] == b) ||
	    (comb[i][0] == b && comb[i][1] == a))
	    return i;
    }
    return -1;
}

bool FindDele(char a, char b) {
    for (int i=0; i<D; ++i)
	if ((dele[i][0] == a && dele[i][1] == b) ||
	    (dele[i][0] == b && dele[i][1] == a))
	    return true;
    return false;
}

void Proc() {
    for (int i=0; i<N; ++i) {
	for (int j=i-1; j>=0; --j) {
	    int result;
	    if (j == i-1) {
		result = FindComb(data[j], data[i]);
		if (result != -1) {
		    data[j] = comb[result][2];
		    data[i] = -1;
		}
	    }
	    if (FindDele(data[j], data[i]))
		for (int k=0; k<=i; ++k)
		    data[k] = -1;
	}
    }
}

void Output(int index) {
    printf("Case #%d: [", index);
    bool flag = false;
    for (int i=0; i<N; ++i) {
	if (data[i] == -1) continue;
	if (flag) printf(", ");
	printf("%c", data[i]);
	flag = true;
    }
    printf("]\n");
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int t;
    cin >> t;
    for (int i=0; i<t; ++i) {
	memset(comb, 0, sizeof(comb));
	memset(dele, 0, sizeof(dele));
	Input();
	Proc();
	Output(i+1);
    }
    return 0;
}
