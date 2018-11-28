#include <cstdio>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <cstring>
#include <ctype.h>

#define inputfilename "a.in"
#define outputfilename "a.out"

using namespace std;

void num2Perm(int n, int * p, int t) {
for (int i = n - 1; i >= 0; i--) {
p[i] = t % (n - i);
t /= n - i;
}
for (int i = n - 1; i; i--) {
for (int j = i - 1; j >= 0; j--) {
if (p[j] <= p[i]) {
p[i]++;
}
}
}
}

int main ()
{
	freopen(inputfilename , "r" , stdin);
	freopen(outputfilename , "w" , stdout);

	int number, times;
	cin >> number;
	int a[1000];
	for (times = 0 ; times < number ; times++)
	{
		int k;
		string s;
		int l;
		cin >>k;
		cin >>s;
		l = s.length();
		int num;
		int i, j , p ;
		char temp[1000];
		num = 1;
		for (i =2; i <= k ; i++) num *= i;
		int result = l+10;
		for (i = 0; i < num; i++)
		{
			num2Perm(k , a , i);
			for (j = 0 ; j < l /k ; j++)
			{
				int b= j * k;
				for (p = 0 ; p < k ; p++)
				temp[b+p] = s[b+a[p]];
			}
			int count = 0 ;
			for (j = 1 ; j < l ; j++)
			{
				if (temp[j] != temp[j-1]) count++;
			}
			result = min (result, count);
		}
		printf("Case #%d: %d\n" , times+1, result+1);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}

 
