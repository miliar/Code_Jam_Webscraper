#include<iostream>
#include<cmath>
#include<set>
using namespace std;

int main() {
	int T;
	cin>>T;
	int*count = new int[T];
	for (int j=0;j<T;j++) {
		cin>>ws;
		int A,B;
		cin>>A>>B;
	
		set < pair<long long,long long> > s;
		
		for (long long n=A;n<B;n++) {
			if (n < 10)
				continue;
			int sz = 1;
			long long i = n;
			while (i/10 > 0) {
				sz++;
				i/=10;		
			}
			i = n;
			for (int j=0;j<sz-1;j++) {
				long long c = (i%10)*pow(10,sz-1) + i/10;
				if (c>n && c<=B) {
					s.insert(make_pair(n,c));
				}
				i = c;
			}
		}
	
		count[j]=s.size();
	}

	for (int i=0;i<T;i++)
		cout<<"Case #"<<i+1<<": "<<count[i]<<endl;
	return 0;
}
