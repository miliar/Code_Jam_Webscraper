#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin>>nt;
	for (int t = 1; t <= nt; ++t) {
		string str;
		cin>>str;
		cout<<"Case #"<<t<<": ";
		
		//int need[10];
		//memset(need, 0, sizeof(need));
		//for (int i = 0; i < str.size(); need[str[i++] - '0']++);
		//int start;
		//sscanf (str.c_str(), "%d", &start);
		//for (++start; ; ++start) {
		//	int got[10];
		//	memset(got, 0, sizeof(got));
		//	int cp = start;
		//	while (cp) {got[cp % 10]++; cp /= 10;}
		//	int i;
		//	for (i = 1; i < 10; ++i)
		//		if (got[i] != need[i]) break;
		//	if (i == 10)
		//		break;
		//}
	

		if (!next_permutation(str.begin(), str.end()))
		{
			string str2;
			sort(str.begin(), str.end());
			int i, li;
			for (i = 0; i < str.size() && str[i] == '0'; ++i);
			li = i;
			str2 += str[li];
			for (int j = 0; j <= li; ++j)
				str2 += '0';
			for (i = li + 1; i < str.size(); str2 += str[i++]);
			str = str2;
		}
		cout<<str<<endl;
	/*	int cool;
		sscanf (str.c_str(), "%d", &cool);
		if (cool != start) {
			printf ("t = %d brute = %d smart = %d", nt, start, cool);
			return 0;
		} else {
			printf ("t %d ok\n", t);
		}*/
	}
	return 0;
}