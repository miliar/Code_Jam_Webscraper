#include <iostream>

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	for(int no=1;no<=t;no++) {
		//Combine
		int c, d;
		char combine[256][256];
		char oppose[256][256];
		
		for(int i=0;i<256;i++) {
			for(int j=0;j<256;j++) {
				combine[i][j] = '\0';
				oppose[i][j] = 0;
			}
		}
		cin >> c;
		for(int i=0;i<c;i++) {
			string str;
			cin >> str;
			combine[str[0]][str[1]] = str[2];
			combine[str[1]][str[0]] = str[2];
		}
		
		//Oppose
		cin >> d;
		for(int i=0;i<d;i++) {
			string str;
			cin >> str;
			oppose[str[0]][str[1]] = 1;
			oppose[str[1]][str[0]] = 1;
		}
		
		int n;
		string str, list;
		cin >> n;
		cin >> str;
		for(int i=0;i<n;i++) {
			list += str[i];
			char c1 = '\0', c2 = '\0';
			if(list.size()>=1) c1 = list[list.size()-1];
			if(list.size()>=2) c2 = list[list.size()-2];

			if(combine[c1][c2]) {
				list.resize(list.size()-2);
				list += combine[c1][c2];
			} else {
				for(int j=0;j<list.size()-1;j++) {
					//cout << c1 << list[j] << " ";
					if(!oppose[c1][list[j]]) continue;
					list.resize(0);
					break;
				}
				//cout << endl;
			}
		}
		
		cout << "Case #" << no << ": [";
		for(int i=0;i<list.size();i++) {
			cout << list[i];
			if(i<list.size()-1) cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
