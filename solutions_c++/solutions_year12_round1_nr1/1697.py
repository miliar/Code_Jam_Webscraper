#include <iostream>
#include <stdio.h>
using namespace std;
int main() {
	float cur=0, min=0;
	int T;
	int A, B;
	float p[100000];
	float right=0;
	cin>>T;
	for (int cases=1; cases<=T; cases++) {
		cin>>A>>B;
		for (int i=0; i<A; i++)
			cin>>p[i];
		min=(B+2<A+B+1)?B+2:A+B+1;
		right=0;
		for (int back=0; back<A; back++) {
			right=p[0];
			for (int i=1; i<A-back; i++)
				right*=p[i];
			cur=right*(B-A+back*2+1)+(1-right)*(B-A+back*2+1+B+1);
			min=cur<min?cur:min;
		}
		printf("Case #%d: %.6f\n", cases, min);
	}
	return 0;
}
