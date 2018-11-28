#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

#define gout case_number++, printf("Case #%d: ", case_number), cout
#define REP(i,n) for(i=0;i<n;i++)

int case_number;

int rol (int n, int p, int d)
{
	// n - number
	// p - positions
	int powX = (int) pow (10, p);
	int left = n%powX;
	int right = n/powX;
	powX = (int) pow (10, d-p);
	return (left*powX + right);
}
	
void main2 ()
{
	int a, b, i, j, count = 0; //ans divided by 2
	int d; //number of digits
	scanf ("%d %d", &a, &b);
	
	int temp = a;
	d = 0;
	while (temp)
	{
		d++;
		temp/=10;
	}
	
	//
	//cout << d << endl;
	for (i = a; i <= b; i++){
		for (j = 1; j < d; j++){
			int n = rol (i, j, d);
			if (n >= a && n <= b && n > i){
				count++;
	//			cout << i << " " << n << endl;
			}

		}
	}
	gout << count << endl;
}
int main()
{
	int test_case, i;
	scanf ("%d", &test_case);

	REP(i,test_case) main2 ();
	return 0;
}

