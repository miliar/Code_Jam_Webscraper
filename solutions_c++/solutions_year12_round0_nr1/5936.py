#include <iostream>

using namespace std;

char a['z' - 'a'];


int main () {

a[0]='y';	a[1]='h'; a[2]='e'; a[3]='s';a[4]='o';a[5]='c';a[6]='v'; a[7]='x';a[8]='d';
a[9]='u'; a[10]='i'; a[11]='g'; a[12]='l'; a[13]='b'; a[14]='k'; a[15]='r'; a[16]='z';
a[17]='t'; a[18]='n'; a[19]='w'; a[20]='j'; a[21]='p'; a[22]='f'; a[23]='m';
a[24]='a'; a[25]='q';


	int s; string w;
	cin >> s;
	cin.ignore();

	for (int i=1; i <= s; i++) {
		getline(cin, w);


		cout << "Case #" << i << ": ";
		for (unsigned j = 0; j < w.size(); j++) {
			if (isalpha(w[j])) {
				cout << a[w[j]-'a'];
			}
			else {
				cout << w[j];
			}
		}
		cout << "\n";

	}
	return 0;	
}
