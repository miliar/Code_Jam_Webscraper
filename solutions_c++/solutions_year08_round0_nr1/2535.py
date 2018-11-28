#include <iostream>
#include <vector>
#include <string>
#include <cstring>

#define SE 101
#define INP 1001

using namespace std;

int main () {

	string se[SE];
	string inp;
	bool checked[SE];
	int i,j,k;

	char temp[101];

	int n;
	int m;
	int ans, flag, special;
	int case_no=0;


	int t;
	cin >> t;

	while (t--) {

		case_no++;

		ans = 0;
	
		cin >> n;

		cin.getline (temp, 100, '\n');

		for (i=0;i<n;i++){ 
			checked[i]=0;
			cin.getline (temp, 100, '\n');
			se[i].assign(temp);
		}

		cin >> m;

		cin.getline (temp, 100, '\n');
	
		for (i=0;i<m;i++) {
			cin.getline (temp, 100, '\n');
			inp.assign(temp);
			for (j=0;j<n;j++) {
				if (checked[j]==1)
					continue;
				if (se[j]==inp) {
					checked[j]=1;
          special=j;
					break;
				}
			}
	
      flag=0;
      
			for (j=0;j<n;j++) {
				if (checked[j]==0) {
					flag=1;
				}
			}
		 
			// none of them is zero therefore we need to increment answer 
			 
			if (flag==0) {
				ans++;
				for (j=0;j<n;j++) {
					checked[j]=0;
				}
        checked[special]=1;
			}
		}

		cout << "Case #" << case_no << ": " << ans << "\n";
	}

	return 0;
}
