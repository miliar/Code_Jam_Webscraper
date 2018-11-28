#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> start, end;

long long num(int A, int B) {
	long long ans=0;
	for (int i=1;i<=A;i++) {
		ans+=min(end[i],B)-min(start[i],B+1)+1;
	}
	return ans;
}

long long num(int A1, int A2, int B1, int B2) {
	long long ans=0;
	int pot;
	for (int i=A1;i<=A2;i++) {
		//cout << "Do row " << i << endl;
		// intersection of both
		pot=min(end[i],B2)-max(start[i],B1)+1;
		if (pot>0) ans+=pot;
		//cout << pot << endl;
		//ans+=min(end[i],B)-min(start[i],B+1)+1
	}
	return ans;
}

int main() {
	int T;
	cin >> T;
	
	
	start.push_back(0);
	end.push_back(0);
	start.push_back(1);
	end.push_back(1);
	start.push_back(2);
	end.push_back(3);
	for (int i=3;i<=1000000;i++) {
		// starts where earliest "end" goes over
		vector<int>::iterator it = lower_bound(end.begin(),end.end(),i);
		int starter=it-end.begin();
		start.push_back(starter);
		end.push_back(starter+i-1);
		//cout << starter << " to " << starter+i-1 << endl;
	}
	
	for (int i=1;i<=T;i++) {
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;	
		cout << "Case #" << i << ": ";
		cout << (long long)(A2-A1+1)*(long long)(B2-B1+1)-num(A1,A2,B1,B2);
		cout << endl;
	}
	
	return 0;	
}
