#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	char normal[28] = "abcdefghijklmnopqrstuvwxyz ";
	char coded[28]= "ynficwlbkuomxsevzpdrjgthaq ";

	int times; cin >> times;

	cin.get();
	for(int iii=0;iii<times;iii++)
	{
		char string[102];
		cin.getline(string, 101);
		for(int j=0; j<strlen(string); j++)
		{
			char* it = find(coded, coded+27, string[j]);
			int index = it - coded;
			string[j]=normal[index];
		}
		cout << "Case #" << iii+1 <<": " << string << endl;
	}
	return 0;
}