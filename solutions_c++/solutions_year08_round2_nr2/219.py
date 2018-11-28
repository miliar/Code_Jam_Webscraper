#include <iostream>
#include <stdio.h>
#include <set>
#include <vector>

using namespace std;

vector<int> f(int number)
{ 
	 vector<int> p;
	 for(int i = 2; i <= number; i++) {
		 if(number % i == 0)
		 {
			 bool prime = true;
			 for(int j = 2; j < i; j++) // Test for prime
			 {
				 if(i % j == 0) // It is not prime
					 prime = false;
			 }
			 if(prime) p.push_back(i);
		 }
	 }
	return p;
}

int main() {
	int C;
	cin >> C;
	for(int num=0;num<C;num++) {
		int s[1010];
		for(int i=1;i<=1000;i++) s[i] = i;
		int A,B,P;
		cin >> A >> B >> P;
		for(int i=A;i<=B;i++) for(int j=i+1;j<=B;j++) {
			vector<int> a(f(i)),b(f(j));
			for(int k=0;k<a.size();k++) if(a[k]<P) continue; else if( find(b.begin(),b.end(),a[k])!=b.end() ) {
				for(int x=A;x<=B;x++) if(s[x]==s[j]) s[x]=s[i];
				break;
			}
		}
		set<int> ret;
		for(int i=A;i<=B;i++) ret.insert(s[i]);
		printf("Case #%d: %d\n",num+1,ret.size());
	}
	return 0;
}
