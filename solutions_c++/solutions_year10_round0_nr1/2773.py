#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int caseNumber;
	cin >> caseNumber;
	for (int i = 0; i < caseNumber; i++)
	{
		int SnapperNo;
		cin >> SnapperNo;
		long flip;
		cin >> flip;
		cout << "Case #" << i+1 << ": ";
		if (flip == 0) {
			cout<<"OFF"<<endl;
			continue;
		}
		long base = pow((double)2, SnapperNo) -1;
		if (flip > base)
		{
			flip %= (base+1);
		}
		if (flip == base)
		{
			cout<<"ON"<<endl;
		} else
		{
			cout<<"OFF"<<endl;
		}
	}
}
