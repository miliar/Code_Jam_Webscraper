#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
using namespace std;

int maxnum = -1;
int* candies = NULL;
bool state[1010];
// no carry
// less significant ones goes first
int binary_add(int a, int b) {
    unsigned char bina[25];
    unsigned char binb[25];
    unsigned char binresult[26];
    

    memset(bina, 0, 25);
    memset(binb, 0, 25);
    memset(binresult, 0, 26);

    int cur = 0;
    do {
	bina[cur++] = a & 1;
    } while (a >>= 1);

    cur = 0;
    do {
	binb[cur++] = b & 1;
    } while (b >>= 1);


    for (int i=0;i<25;i++) {
	binresult[i] = (bina[i] + binb[i]) % 2;
    }

    int result = (int) binresult[0];
    for (int i=1;i<26;i++) {
	result += (int) (binresult[i] << i);
    }

    return result;
}

bool valid_pile(int k, int n, int& amount) {
    if (k != n) return false;

    int pile1 = 0, pile2 = 0;
    amount = 0;
    for (int i=0;i<n;i++) {
	if (state[i+1]) {
	    amount += candies[i];
	    pile1 = binary_add(pile1, candies[i]);
	    //cout << "adding " << candies[i] << "to pile 1 = " << pile1 << endl;
	} else {
	    pile2 = binary_add(pile2, candies[i]);
	    //cout << "adding " << candies[i] << "to pile 2 = " << pile2 << endl;
	    
	}
    }

    return (pile1 == pile2 && pile1 != 0 && pile2 != 0);
}

void backtrack(int k, int n) {
    if (k > n) return;

    int amount = 0;
    if (valid_pile(k, n, amount)) {
	if (maxnum < amount)
	    maxnum = amount;
    } else {
	k++;

	state[k] = false;
	backtrack(k,n);

	state[k] = true;
	backtrack(k,n);
	
    }
}

int main() {
    freopen("out.txt", "w", stdout);
    
    /* tests
    cout << "5 + 4 = " << binary_add(5,4) << endl;
    cout << "7 + 9 = " << binary_add(7,9) << endl;
    cout << "50 + 10 = " << binary_add(50,10) << endl; */

    int cases;
    cin >> cases;

    for (int cas=1;cas<=cases;cas++) {
	int n;
	cin >> n;
	candies = new int[n];
	for (int i=0;i<n;i++) {
	    cin >> candies[i];
	}
	sort(candies, candies+n);

	maxnum = -1;
	memset(state, false, sizeof(state));

	backtrack(0, n);

	cout << "Case #" << cas << ": ";
	if (maxnum <= 0)
	    cout << "NO" << endl;
	else
	    cout << maxnum << endl;
    }
    return 0;
}
