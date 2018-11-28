#include <iostream>
#include <string>

using namespace std;

int arr[102][1002] = {0};
string s[101];

int main()
{
	int N,S,Q;
	string q;
	string dummy;
	char c;
	cin >> N;getline(cin, dummy);
	for(int i = 0;i < 101;i++)
		s[i] = "";
	for(int i = 0;i < N;i++) {
		cin >> S;getline(cin, dummy);
		for(int j = 0;j < S;j++) {
			getline(cin,s[j]);
//			cout << s[j] << endl;
		}

		cin >> Q;getline(cin, dummy);
		for(int j = 0;j <= S;j++)
			for(int k = 0;k <= Q;k++)
				arr[j][k] = 0;
		int j,k;
		for(k = 1;k <= Q;k++) {
			getline(cin,q);
			for(j = 0;j < S;j++) {
				if(q == s[j]) {
					int mn = 1000000;
					for(int l = 0;l < S;l++)
						if(l == j)
							continue;
						else
							mn = ((mn < arr[l][k-1])?mn:arr[l][k-1]);
					arr[j][k] = mn + 1;
				} else {
					arr[j][k] = arr[j][k-1];
				}
			}
		}
		
//		cout << N << " " << S << " " << Q << endl;
		int mn = 1000000;
		for(j = 0;j < S;j++)
			if(mn > arr[j][Q])
				mn = arr[j][Q];

		cout << "Case #" << (i+1) << ": " << mn << endl;
	}
}
