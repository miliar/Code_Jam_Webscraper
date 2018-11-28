#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

unsigned long long int prime[1000000];
int main()
{
	long long int T,n,ans;
	long long int Pnum,temp,tempAns;

	Pnum=1; prime[1]=2;
	for(int i = 3; i < 100;i++) {
		int j;
		for(j = 1; j <= Pnum; j++) if( i%prime[j]==0) break;

		if(j==Pnum+1) {
			Pnum++;
			prime[Pnum]=i;
		}
	}

	cin >> T;
	for(int t = 1; t <= T; t++) {
	
		cin >> n;
		if( n == 1 ) {
			ans = 0;
		}
		else {
			ans = 1;
			for(int i = 1; true; i++) {
				temp=1;
				tempAns=0;
				while(1) {
					tempAns++;
					temp = temp*prime[i];
					if(n < temp) break;
				}
				tempAns--;
				
				if(tempAns <= 1) break;
				
				ans += tempAns-1;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}


