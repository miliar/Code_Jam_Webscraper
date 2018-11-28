#include <iostream>
#include <stdlib.h>
#include <algorithm>

using namespace std;


int max(int a, int b) { return (a>b)?a:b;}
int main()
{
	int T;
	cin>>T;
	//int T,v;
	//cin>>T>>v;
	//cout<<(v^T)<<endl;
	//return 0;
	for (int t = 0; t < T; t++) {
		int bar[1000];
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin>>bar[i];
		}

		int p = 1<<n;
		bool possible = false;
		int mx = 0;
		for (int i = 0; i < p; i++) {
			int one[1000];
			int two[1000];
			int oM = 0;
			int tM = 0;
			
			int a = i;
			int x = 0;
			while(x<n){
				if(a%2 == 0)
					one[oM++] = bar[x++];
			    else
					two[tM++] = bar[x++];
				a/=2;	
			}

			
			int oS = 0;
			int oRS = 0;
			int tS = 0;
			int tRS = 0;
			for (int j = 0; j < oM; j++) {
				oS ^= one[j];
				oRS += one[j];
			}
			for (int j = 0; j < tM; j++) {
				tS ^= two[j];
				tRS += two[j];
			}
			
			if(tS == oS && oS!=0){
				possible = true;
				if(max(tRS,oRS) > mx)
					mx = max(tRS,oRS);
			}
		}

		cout<<"Case #"<<t+1<<": ";
		if(!possible)
			cout<<"NO"<<endl;
		else
			cout<<mx<<endl;
	}

}

