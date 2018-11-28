#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <iterator>
#include <iomanip>
#include <cstdio>
using namespace std;

int main(){
	vector <vector <int> > vvi;
	for(int i=0;i<=2000*1000+5;i++){
		//if(i%1000==0) cout << "i = " << i << endl;
		if(i%1000==0) printf("i=%d\n",i);
		ostringstream oss;
		oss << i;
		string s = oss.str();
		vector <int> vi;
		for(int j=0;j<s.size();j++){
			string s2 =s;
			rotate(s2.begin(),s2.begin()+j,s2.end());
			if(s2[0]!='0'){
				istringstream iss(s2);
				int q;
				iss >> q;
				if(i<q)vi.push_back(q);
			}
		}
		sort(vi.begin(),vi.end());
		vector <int> vi2;
		unique_copy(vi.begin(),vi.end(),back_inserter(vi2));
		vvi.push_back(vi2);
	}
	printf("Please enter a digit to start\n");
	int zzz;
	scanf("%d", &zzz);

	ifstream cin("C-Large.in");
	ofstream cout("C-small-attempt0.out");
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int A,B;
		cin >> A >> B;
		int ret = 0;
		for(int j=A;j<=B;j++){
			for(int k=0;k<vvi[j].size();k++)
				if(vvi[j][k]>=A && vvi[j][k] <= B)
					ret ++;
		}
		cout << "Case #" << i+1 << ": " << ret << endl;
	}
	//system("pause");
	return 0;
}