#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int gcd(const int m, const int n)
{
	if (m == n) return m;
	else {
		int a,b,c;
		if (m>n) {
			a = m;
			b = n;
		}
		else {
			a = n;
			b = m;
		}
		while (b != 0) {
			c = a-int(a/b)*b;
			a = b;
			b = c;
		}
		return a;
	} 
}

bool Awin(int A, int B)
{
	if(A==B)
		return false;

	if(B > A) {
		int tmp;
		tmp = B;
		B = A;
		A = tmp;
	}

	int d = gcd(A, B);
	A = A/d;
	B = B/d;

	// now A>B, and coprime
	if(B==1)
		return true;

	if(A==B+1)
		return false;

	int r = A % B;
	if(r==1 || r==B-1)
		return true;
	else {
		int k = (A-r)/B;
		if (k==1)
			return !Awin(B,r);
		if(Awin(B, r))
			return true;
		else {
			for(int i=1; i<=k; i++) {
				if(Awin(A-i*B,B))
					return true;
			}
			return false;
		}

	}
}

int countwin(int A1, int A2, int B1, int B2)
{
	int t = 0;
	for(int i=A1; i<=A2; i++) {
		for(int j=B1; j<=B2; j++) {
			if(Awin(i, j))
				t++;
		}
	}
	return t;
}

int main()
{
	//freopen("D:\\tmp\\test.txt","r",stdin);freopen("D:\\tmp\\test.out","w",stdout);
	freopen("D:\\tmp\\C-small.in","r",stdin);freopen("D:\\tmp\\C-small.out","w",stdout);
	//freopen("D:\\tmp\\A-large.in","r",stdin);freopen("D:\\tmp\\A-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;
		int result = countwin(A1, A2, B1, B2);
		printf("Case #%d: ",caseId);
		printf("%d", result);
		printf("\n");
	}

	return 0;
}