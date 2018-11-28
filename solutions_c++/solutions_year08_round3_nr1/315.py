#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>


using namespace std;

int main(int argc,char** argv){
	long long int cases;
	long long int P, K, L;
	long long int tmp;
	long long int result;
	cin >> cases;
	for(long long int i=0;i<cases;i++){
		cin >> P;
		cin >> K;
		cin >> L;
		vector<long long int> vi;
		for(long long int j=0;j<L;j++){
			cin >> tmp;
			vi.push_back(tmp);
		}
		sort(vi.rbegin(),vi.rend());
		long long int level;
		result=0;
		level=0;
		for(long long int j=0;j<L;j++){
			if(j%K==0)level++;
			result+=vi[j]*level;
		}
		
		cout << "Case #" << i+1 << ": " << result << endl;
	}
}
