#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int i;
	int p;
	int num_cases, ans;

	scanf("%d", &num_cases);
	cin.ignore(10, '\n');

	string line;
	string key(" welcome to code jam");



	for (p=1; p<=num_cases; p++){

		getline(cin, line, '\n');
		string::iterator lpointer;
		vector<int> count(100, 0);
		count[0] = 1;

		for (lpointer = line.begin(); lpointer != line.end(); lpointer++){

			for (i=1; i<key.length(); i++){
				if (*lpointer == key[i]){
					count[i] += count[i-1];
					count[i] = count[i] % 10000;
				}
			}

		}

		printf("Case #%d: ",p);

		ans = count[key.length()-1];
		if (ans < 10) printf("0");
		if (ans < 100) printf("0");
		if (ans < 1000) printf("0");

		printf("%d\n", ans);


	}
	return 0;
}
