#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

ifstream cin("A-Large.in");
ofstream cout("A.out");

long long getval(string s){
	if(s.size()==1) return 1;
	string s2 = s;
	sort(s2.begin(),s2.end());
	string s3;
	unique_copy(s2.begin(),s2.end(),back_inserter(s3));
	long long base = s3.size();
	long long zzz =2;
	base = max(zzz,base);
	map<char,long long> mp;
	mp[s[0]]=1;
	long long k=0;
	long long available[200]={0};
	available[1]=1;
	for(long long i=1;i<s.size();i++){
		if(mp.count(s[i])==0) {
			long long j = find(available,available+200,0)-available;
			
			available[j]=1;
			mp[s[i]]=j;
		}
	}
	long long sum = 0;
	for(long long q=0;q<s.size();q++){
		sum = sum*base;
		sum += mp[s[q]];		
	}
	return sum;
}	

void testval(){
	while(true){
	cout << "Please enter string" << endl;
	string s;
	cin >> s;
	long long i = getval(s);
	cout << "i=" << i << endl;
	}

}

int main(){
	//testval();
	long long N;
	cin >> N;
	for(long long i=0;i<N;i++){
		string s;
		cin >> s;
		long long v = getval(s);
		cout << "Case #" << i+1 << ": " << v << endl;	
	}
	return 0;
};