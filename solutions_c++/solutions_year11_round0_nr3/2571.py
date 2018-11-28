#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

void dostep(int t) {
	int n;
	cin >> n;
	int c[1005];
	int sum = 0;
	int x = 0;
	for(int i=0;i<n;i++){cin >> c[i];sum+=c[i];x^=c[i];}
	if (x != 0) {
		cout << "Case #" << t << ": NO" << endl;
		return;
	}
	int best=0;
	for(int i=0;i<n;i++) {
		if(c[i]<c[best])best=i;
	}
	int max_val = sum-c[best];
	/*
	for (int i=0;i<n;i++) {
		if ((x^c[i]) != 0) continue;
		int best=-1;
		for (int j=0;j<n;j++) {
			if (i==j)continue;
			if (best==-1||c[j]<c[best])best=j;
		}
		if (sum-c[i]-c[best]>max_val)max_val=sum-c[i]-c[best];
	}*/

        cout << "Case #" << t << ": " << max_val << endl;
}

int main() {
        int n;
        cin>>n;
        for (int i=1;i<=n;i++)dostep(i);
        return 0;
}
