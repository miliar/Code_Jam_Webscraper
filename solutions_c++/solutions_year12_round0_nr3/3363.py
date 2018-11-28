#include <iostream>
#include <set>
#include <vector>

using namespace std;

int rotate(int x, int size)
{

	int digit = x%10;
	int res1 = x/10;
	while (size>1) {
		digit *= 10;
		size--;
	}
	return digit + res1;
}

int countdigit(int x)
{
	int cnt = 0;
	while(x) {
		cnt++; x/=10;
	}
	return cnt;
}
int process(int A, int B)
{
	int cnt = 0;
	for(int i=A; i<=B; i++)
	{
		int num1 = i;
		int j=0;
		int sz = countdigit(i);
		set<int> s;
		do
		{
			
			num1 = rotate(num1, sz);
			if (i<num1 && num1 <= B && s.count(num1)==0) {
				cnt++;
				s.insert(num1);
			}
			j++;
		}while (j<3);
	}
	return cnt;
}

int main (int argc, char * const argv[]) {
    // insert code here...
	int T;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		int A, B;
		cin >> A >> B;
		
		int res = process(A, B);
		cout << "Case #" << i+1 << ": " << res << endl;
	}
    return 0;
}
