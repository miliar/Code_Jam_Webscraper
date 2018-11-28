#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	char buff[24];
	cin.getline(buff, 24);

	int i,j,tmp;
	int highestIndex, nextHighestIndex;
	for (int t=1; t<=T; ++t) {
		cin.getline(buff, 24);
		string number(buff);
		/*for (i=0, j=0; i<number.length()-1; ++i) {
			if (number[i] == '0') continue;
			buff[j++] = number[i];
		}
		buff[j] = '\0';
		string newnum(buff);*/ string newnum(number);
		highestIndex = -1;
		for (i=0; i<newnum.length()-1; ++i) {
			if (newnum[i] < newnum[i+1]) {
				highestIndex = i;
				nextHighestIndex = i+1;
			}
		}
		if (highestIndex != -1) {
			i = highestIndex;
			for (j=nextHighestIndex; j<newnum.length(); ++j) {
				if (newnum[j] > newnum[i]) {
					nextHighestIndex = j;
				}
			}
			j = nextHighestIndex;
			tmp = newnum[i];
			newnum[i] = newnum[j];
			newnum[j] = tmp;
			++i; j = newnum.length()-1;
			while (i < j) {
				tmp = newnum[i];
				newnum[i] = newnum[j];
				newnum[j] = tmp;
				++i; --j;
			}
			/*for (i=0; i<number.length(); ++i) {
				if (number[i] == '0') buff[i] = '0';
				else buff[i] = 'a';
			}*/
			for (i=0, j=0; i<number.length(); ++i) {
				//if (buff[i] == '0') continue;
				buff[i] = newnum[j++];
			}
			buff[i] = '\0';
			cout << "Case #" << t << ": " << string(buff) << endl;
		} else {
			vector<char> vect;
			for (i=0; i<newnum.length(); ++i) {
				if (newnum[i] != '0') vect.push_back(newnum[i]);
			}
			sort(vect.begin(), vect.end());
			cout << "Case #" << t << ": "<< vect[0];
			for (i=0; i<=(number.length() - vect.size()); ++i) {
				cout << '0';
			}
			for (i=1; i<vect.size(); ++i) {
				cout << vect[i];
			}
			cout << endl;
		}
	}

	return 0;
}
