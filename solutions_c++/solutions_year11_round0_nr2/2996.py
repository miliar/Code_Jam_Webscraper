#include <stdio.h>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int test_count = 0;
    cin >> test_count;

    for (int test_index = 1; test_index <= test_count; test_index++) {
        
		string c_count_s;
		cin >> c_count_s;
		int c_count = atoi(c_count_s.c_str());
		string c[111];
		for (int i = 0; i < c_count; i++) cin >> c[i];
		
		string d_count_s;
		cin >> d_count_s;
		int d_count = atoi(d_count_s.c_str());
		string d[111];
		for (int i = 0; i < d_count; i++) cin >> d[i];

		
		string n_count_s;
		cin >> n_count_s;
		int n_count = atoi(n_count_s.c_str());
		string n;
		cin >> n;


		string ans;
		for (int i = 0; i < n_count; i++) {
			ans.append(n.substr(i, 1));

			for (int j = 0; j < c_count; j++) {
				char first = c[j][0];
				char second = c[j][1];
				char result = c[j][2];
				
				int len = ans.length();
				if (len > 1 && ((ans[len-1] == first && ans[len-2] == second) || (ans[len-2] == first && ans[len-1] == second))) {
					ans = ans.substr(0, len - 2);
					ans.append(c[j].substr(2, 1));
				}
			}
			
			for (int j = 0; j < d_count; j++) {
				char first = d[j][0];
				char second = d[j][1];

				int pos_first = ans.rfind(first);
				int pos_second = ans.rfind(second);

				if (pos_first != -1 && pos_second != -1) {
					ans.clear();
				}
			}

		}

        cout << "Case #" << test_index << ": [";
		for (int i = 0; i < ans.length(); i++)
			cout << ans[i] << ((ans.length()-1 == i) ? "" : ", ");
		cout << "]" << endl;
    }

	return 0;
}
