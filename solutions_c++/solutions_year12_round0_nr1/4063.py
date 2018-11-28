#include <iostream>
#include <string>
using namespace std;

void initialize(char arr[]){
	arr[0] = 'y';
	arr[1] = 'h';
	arr[2] = 'e';
	arr[3] = 's';
	arr[4] = 'o';
	arr[5] = 'c';
	arr[6] = 'v';
	arr[7] = 'x';
	arr[8] = 'd';	
	arr[9] = 'u';
	arr[10] = 'i';
	arr[11] = 'g';
	arr[12] = 'l';
	arr[13] = 'b';
	arr[14] = 'k';
	arr[15] = 'r';
	arr[16] = 'z';
	arr[17] = 't';
	arr[18] = 'n';
	arr[19] = 'w';
	arr[20] = 'j';
	arr[21] = 'p';
	arr[22] = 'f';
	arr[23] = 'm';
	arr[24] = 'a';
	arr[25] = 'q';
}

int main()
{
	char arr[26];
	initialize(arr);
	int N;
	cin >> N;
	string mystr;
	string ans = "";
	getline(cin,mystr);
	for(int i = 0; i < N ; i++)
	{
		getline(cin,mystr);
		for(int k = 0; k < mystr.length(); k++)
		{
			if(mystr[k] == ' ')
			{
				ans = ans+ " ";
			}
			else
			{
				ans = ans + arr[mystr[k]-'a'];
			}
		}
	cout << "Case #"<< i+1 <<": "<<ans<<endl;	
	ans = "";
	}	
	return 0;
}
