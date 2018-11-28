#include <iostream>
using namespace std;

int n, m;
int f[2000][2000];

void input() {
	cin >> n >> m;
	
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
			f[i][j] = -1;
	
	for(int j=0;j<m;j++) {
		int fn;
		cin >> fn;
		for(int i=0;i<fn;i++) {
			int a,b;
			cin >> a >> b;
			f[j][a-1] = b;
		}
	}
}

int count1(int v) {
	int cnt = 0;
	for(int i=0;i<(1<<n);i++)
		if((v&(1<<i))>0)
			cnt++;
	return cnt;
}

int main() {
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		
		int mini = -1; 
		for(int i=0;i<(1<<n);i++) {
			bool failed = false;
			for(int j=0;j<m;j++) {
				bool found = false;
				for(int k=0;k<n;k++) {
					bool b = (i & (1<<k)) > 0;
					if(f[j][k] != -1 && f[j][k] == b)
						found = true;
				}
				if(!found)
					failed = true;
			}
			
			if(!failed && (mini==-1 || count1(mini) > count1(i))) {
				mini = i;								
			}
		}
		
		cout << "Case #" << casei << ": ";
		
		if(mini == -1)
			cout << "IMPOSSIBLE";
		else {
			for(int i=0;i<n;i++) {
				if((mini&(1<<i)) > 0)
					cout << 1;
				else
					cout << 0;
				cout << " ";
			}
		}
		cout << endl;
	}
	
	return 0;
}
