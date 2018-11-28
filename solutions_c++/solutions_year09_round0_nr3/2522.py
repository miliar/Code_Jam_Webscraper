/*welcome to code jam*/
#include <stdio.h>
#include <string>
using namespace std;

int main() {
	int i,N;
	string codejam = "welcome to code jam";
	scanf ("%d\n", &N);
	for (int i=1;i<=N;i++) {
		char temp;
		int idx = 0;
		int count=1, countemp = 0;
		scanf ("%c", &temp);

		while (temp!='\n') {
			if (temp==codejam[idx]) {
				countemp++;
			}
			else if (idx<codejam.length()-1) {
				if ((temp==codejam[idx+1])&&(countemp!=0)) {
					count= (count*countemp) % 10000;
					idx++;
					countemp = 1;
				}
			}
		
		scanf ("%c", &temp);
		}
	
		if (idx==codejam.length()-1) count= (count*countemp) % 10000;
		else count=0;
		if (count >= 1000) printf ("Case #%d: %d\n", i,count);
		else if (count >= 100) printf ("Case #%d: 0%d\n", i,count);
		else if (count >= 10) printf ("Case #%d: 00%d\n", i,count);
		else if (count >= 1) printf ("Case #%d: 000%d\n", i,count);
		else printf ("Case #%d: 0000\n", i);
	}
return 0;
}
