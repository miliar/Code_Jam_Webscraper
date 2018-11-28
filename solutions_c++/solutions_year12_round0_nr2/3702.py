#include<iostream>
#include<string>
#include<cstdlib>
#include<cctype>
#include<vector>
#include<map>
using namespace std;


int main() {
	int t;
	int n, s, p;
	int result, t1,t2;
	cin >> t;
	for (int count=0; count<t; count++) {
		cout << "Case #" << count+1 << ": ";
		
		cin >> n >> s >> p;
		result = 0;
		t1 = (p-1)*3+1;
		t2 = (p-2)*3+2;
		if (p==1) t2=1;
		int temp;
		for (int i=0; i<n; i++) {
			cin >> temp;
			if (temp>=t1) result++;
			else if (temp>=t2 && s>0) {
				result++;
				s--;
			}
		}
		cout << result << endl;
	}
	return 0;
}
