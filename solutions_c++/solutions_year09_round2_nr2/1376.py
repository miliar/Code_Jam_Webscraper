#include<iostream>
using namespace std;

int main()
{
	int cases = 0;
	cin >> cases;
	char* digits = (char *)malloc(100 * sizeof(char));
	
	for(int t = 0; t < cases; t++)
	{
		int input;
		
		cin >> input;
		sprintf(digits, "%d%d", 0, input);
		
		int i = 0;
		for(i = 0; digits[i] != '\0'; i++)
			;
		//cout << i;
		next_permutation(digits, digits + i);
		
		cout << "Case #" << t + 1 << ": ";
		for(int i = digits[0] == '0' ? 1 : 0; digits[i] != '\0'; i++)
			cout << digits[i];
		cout << endl;
	}
	
	return 0;
}