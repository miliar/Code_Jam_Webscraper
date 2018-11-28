#include <stdio.h>
#include <vector>
using namespace std;

int main () {
	FILE *input, *output;
	input = fopen("input.in","r");
	output = fopen("output.txt","w");
	int i, count, j;
	int a, b, c, res, temp;
	vector <int> r, k, n ;
	fscanf(input, "%d", &count);
	for (i=0;i<count;i++) {
		temp = 0;
		fscanf(input, "%d %d %d", &a, &b, &c);
		r.push_back(a);
		k.push_back(b);
		for (j=0;j<c;j++) {
			fscanf(input, "%d", &a);
			n.push_back(a);
			temp = temp + a;
		}
		a = 0;
		b = 0;
		res = 0;
		if (temp<=k[i]) {
			res = temp * r[i];
		}
		else {
		do {
			a = a + n.at(0);
			if (a <=k[i]) {
				n.push_back(n.at(0));
				n.erase(n.begin());
			}
			else {
				res = res + a - n.at(0);
				b++;
				a = 0;
			}
		} while (b!=r[i]);
		}
		fprintf(output, "Case #%d: %d\n",i+1,res);
		n.clear();
	}

	return 0;
}