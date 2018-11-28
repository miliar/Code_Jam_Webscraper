#include <iostream>
#include <fstream>

using namespace std;
unsigned long long int rs[100000000];
int g[10000000];
int main (int argc, char * const argv[]) {
	
	int t,test,r,k,n,i;
	unsigned long long int sum,rez;
	ifstream in("C.in");
	ofstream out("C.out");
	in >> t;
	
	for (test = 0; test < t; test++) {
		
		
		in >> r >> k >> n;
		//cout << "r = " << r << " k = " << k << " n = " << n << endl;
		
		
		for (i=0; i<n; i++) {
			in >> g[i];
		}
		
		
		int group=0;
		int oneTime = 0;
		//unsigned long long sum = 0;
		sum = 0;
		for (i=1; i<=r; i++) {
			oneTime = 0;
			int countGroupsRiding = 0;
			while (oneTime + g[group] <= k) {
				oneTime += g[group];
				group++;
				group %= n;
				countGroupsRiding++;
				if(countGroupsRiding == n){
					break;
				}
			}
			
			sum += (unsigned long long int)oneTime;
			//cout << " add to sum " << oneTime << endl;
			
			rs[i] = sum;
			//cout << "group = " << group << " i = " << i << " n = " << n << endl;			
			/*if(group == n-1){
				//cout << "inside " << "group = " << group << " i = " << i << " n = " << n << endl;
				//We've found preiod
				//Result will be (r / i) * rs[i] + rs[r%i]
				sum *= r/i;
				if(r%i > 0){
					sum += rs[r%i];	
				}
				break;
			}*/
			 
			 
		}
		
		out << "Case #" << test+1 << ": " << sum << endl; 
		cout << "Case #" << test+1 << ": " << sum << endl; 
	}
	
	
	
	return 0;
}
