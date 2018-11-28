#include <iostream>
#include <vector>
#include <map>
#include <bitset>
using namespace std;

int main() {
	//read input from file...
	int noOfSnappers;
	int noOfClick;
	int noOfTest;

	cin >> noOfTest;
	for(int i=0; i < noOfTest; i++)
	{
//		int index = 0;
		cin >> noOfSnappers>> noOfClick;
		int even = 0;
		if(noOfClick % 2 == 0)
			even = 1;
		else
			even = 0;
		bitset<32> va((long)noOfClick);
		int temp = 0;

		for(int j=0 ; j < noOfSnappers; j++)
			temp += (int)va[j];

		if(temp == noOfSnappers)
			temp = 1;
		else
			temp = 0;

		//if(temp== 1 && (even == 0))
		//output to file
		cout <<"Case #" << i+1 <<": ";
		if(temp == 1)
		//if(temp== 1 && (even == 0))
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	return 0;
}
