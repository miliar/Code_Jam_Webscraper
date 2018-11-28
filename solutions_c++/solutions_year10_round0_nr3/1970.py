//#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;

ifstream cin ("C-large.in");
ofstream cout ("outfile10.out");

struct dat{
	bool valid;
	long moneyz;
	int skip;
	dat (long m = 0, int s = 0) {
		valid = false;
		moneyz = m;
		skip = s;
	}
};

long f(long r, long k, int n, vector<long> queue) {
	dat A[n];
	int counter = 0;
	long money = 0;
	for (int i =0;i<r;i++) {
		long count = 0;
		int start = counter;
		if (A[start].valid == false) {
			while (count<k && counter<n) {
				if ((count+queue[counter]) > k) break;
				count += queue[counter];
				counter = (counter+1) %n;
				if (start == counter) break;
				
			}
			A[start].valid = true;
			A[start].moneyz = count;
			A[start].skip = counter;
			money+=count;
		}
		else {
			counter = A[start].skip;
			money+= A[start].moneyz;
		}
			
		
		/*
		for (int j=0;j<counter;j++) {
			int temp;
			temp = queue.front();
			queue.erase(queue.begin());
			queue.push_back(temp);
		}
		 */
	}
	return money;
	
}
int main () {
	int T;
	string s;
	cin>>T;
	cin.get();
	for (int i=0;i<=T;i++) {
		long R,K;
		int N;
		vector<long> queue;
		getline(cin,s);
		istringstream str(s);
		str>>R;
		str>>K;
		str>>N;
		getline(cin,s);
		istringstream slr(s);
		for (int j = 0; j<N; j++) {
			long temp;
			slr>>temp;
			queue.push_back(temp);
		}

		cout<<"Case #"<<i+1<<": "<<f(R,K,N,queue)<<endl;
			

	}	
	return 0;
}
