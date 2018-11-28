#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int cache[1001][2];

int main(){
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	int t;
	fin>>t;
	for(int ti=1; ti<=t; ti++){
		int r,k,n;
		fin>>r>>k>>n;
		list<int> group;
		int in_long;
		for(int i=0; i<n; i++){
			fin>>in_long;
			group.push_back(in_long);
		}
		//init cache
		for(int i=0; i<n; i++){
			int sum=0;
			int j=0;
			list<int>::iterator iter1 = group.begin();
			while(1){
				sum += *iter1;
				j++;
				if(sum > k || j > n) break;
				cache[i][0] = sum;
				cache[i][1] = j;
				if(j == n) break;
				else iter1++;
			}
			iter1 = group.begin();
			group.push_back(*iter1);
			group.pop_front();
		}
		//solve
		long long sol=0;
		int curr = 0;
		for(int i=0;i<r;i++){
			sol += (long long) cache[curr][0];
			curr = (curr + cache[curr][1]) % n;
		}
		fout<<"Case #"<<ti<<": "<<sol<<endl;
	}
}