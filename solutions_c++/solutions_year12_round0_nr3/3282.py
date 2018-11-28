#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
using namespace  std;
int A, B;
int res = 0;
int l[2000001];
void Recycled ()
{
	//FILE * fp_open, * fp_out;
	freopen(".\\C-small-attempt0.in","r", stdin);
	freopen(".\\C-samll-attempt0.out", "w", stdout);
//	freopen(".\\C-large.in","r", stdin);
//  freopen(".\\C-large.out", "r", stdout);
	int ten[7] = {1,10, 100, 1000, 10000, 100000, 1000000};
	for(int i = 1; i <= 2000000; ++i) {
		if(i < 10) l[i] = 1;
		else if(i < 100) l[i] = 2;
		else if(i < 1000) l[i] = 3;
		else if(i < 10000) l[i] = 4;
		else if(i < 100000) l[i] = 5;
		else if(i < 1000000) l[i] = 6;
		else l[i] = 7;
	}
	int t, n, casid = 0, next;
	char str[1000];

	scanf( "%d", &t);
	while(t--) {
		scanf("%d %d", &A, &B);
		res = 0;
		for(int i = A; i <= B; ++i) {
			for(int j = 1; j < l[i]; ++j) {
				next = i / ten[j] + (i % ten[j]) * ten[l[i] - j];
				if(next > i && next <=B)
					res ++;
			}
		}
		printf("Case #%d: %d\n", ++casid, res);
		//cout<<str<<endl;
	}
}
int main()
{
	
	Recycled();
}