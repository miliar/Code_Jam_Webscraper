#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

	
int main(){

	freopen("a_large.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int cases,N,a[1005],b[1005];
	
	cin >> cases; 

	for (int casenum=1;casenum<=cases;casenum++){
		cin >> N;
		for (int i=0;i<N;i++){
			int ha,hb;
			cin >> ha >> hb;
			a[i]=ha; b[i]=hb;
		}
		int c=0;
		for (int i=0;i<N;i++)
			for (int j=i+1;j<N;j++){
				int d1 = a[i]-a[j];
				if (d1>0) d1=1;
				else d1=-1;
				int d2 = b[i]-b[j];
				if (d2>0) d2=1;
				else d2=-1;
				if (d1*d2<0) c++;
			}
		cout << "Case #" << casenum << ": " << c << endl;
	}

	return 0;
}