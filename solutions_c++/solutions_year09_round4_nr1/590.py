#include <iostream>
using namespace std;

#define SWAP(a,b) ( l[(a)]^=l[(b)],l[(b)]^=l[(a)],l[(a)]^=l[(b)],CANT++ )

int main() {

int N, i, j, l[64], CANT, k, K;
char tmp;

cin >> K;

for (k=1; k<=K; k++) {

cin >> N;
for (i=0; i<N; i++) {
	l[i] = -1;
   for (j=0; j<N; j++) {
	   cin >> tmp;
		if (tmp == '1') l[i] = j;
	}
}

CANT = 0;
for (i=0; i<N; i++) {
   if (l[i] > i) {
	   for (j=i+1; j<N && l[j] > i; j++);
		while (j > i) {
		   SWAP(j, j-1);
			j--;
		}
	}
}

cout << "Case #" << k << ": " << CANT << endl;

}

return 0;
}
