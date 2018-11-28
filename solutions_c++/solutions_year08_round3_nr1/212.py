#include <iostream>
#include <iterator>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int64;


vector<int> mm;
int main()
{
	int casenum=0;
	cin>>casenum;
	for (int i=0; i<casenum; i++){
		int P,K;
		int L;
		cin>>P>>K>>L;
		mm.clear();		
		int temp;
		int64 res=0;
		for (int j=0; j<L; j++){
			cin>>temp;
			mm.push_back(temp);
		}
		sort(mm.begin(), mm.end());
		reverse(mm.begin(),mm.end());

		for (int j=0; j<L; j++){
			res+=mm[j]*(j/K+1);
		}

		cout<<"Case #"<<(i+1)<<": "<<res<<endl;
	}

	//system("pause");
	return 0;
}
