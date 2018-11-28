#include <iostream>
#include <vector>
using namespace std;
const int MAX_LEN=10000;
char str[MAX_LEN];
char a[26];
int main()
{
a[0] = 'y';
a[1] = 'h';
a[2] = 'e';
a[3] = 's';
a[4] = 'o';
a[5] = 'c';
a[6] = 'v';
a[7] = 'x';
a[8] = 'd';
a[9] = 'u';
a[10] = 'i';
a[11] = 'g';
a[12] = 'l';
a[13] = 'b';
a[14] = 'k';
a[15] = 'r';
a[16] = 'z';
a[17] = 't';
a[18] = 'n';
a[19] = 'w';
a[20] = 'j';
a[21] = 'p';
a[22] = 'f';
a[23] = 'm';
a[24] = 'a';
a[25] = 'q';

	int n;
	cin>>n;
	cin.getline(str, MAX_LEN);
	for(int i=0;i<n;++i)
	{
		cin.getline(str, MAX_LEN);

		cout<<"Case #"<<i+1<<": "; 
		
		for(int j=0; str[j]; ++j)
			if(str[j] >='a' && str[j]<='z')
				cout<<a[str[j]-'a'];
			else
				cout<<" ";
		cout<<endl;
	}
	return 0;
}