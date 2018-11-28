#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <cctype>
#include <algorithm>
using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	for (int t = 1 ; t <= test ; t++){
		cout<<"Case #"<<t<<": ";
		int n;
		cin>>n;
		int x;
		int cnt=0;
		for (int i=0;i<n;i++){
			cin>>x;
			if (x!=(i+1))
				cnt++;
		}
		cout<<(double)cnt<<"\n";
	}
	return 0;
}