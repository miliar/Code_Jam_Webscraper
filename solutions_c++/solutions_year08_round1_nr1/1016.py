#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	std::freopen("stdout.txt", "w", stdout);
	
	int totNum;
	ifstream mFile("A-small.in.txt");
	mFile >> totNum;
	for (int i=0;i<totNum;i++) {
		int leng,temp,Ans=0;
		
		vector <int > v1, v2;
		mFile >> leng;
		
		for (int i=0;i<leng;i++) {
			mFile >> temp;
			v1.push_back(temp);
		}

		for (int i=0;i<leng;i++) {
			mFile >> temp;
			v2.push_back(temp);
		}

		sort(v1.begin(),v1.end());
		sort(v2.rbegin(),v2.rend());

		for (int i=0;i<leng;i++) {
			Ans+=v1[i]*v2[i];
		}

		cout << "Case #" << i+1 << ": " << Ans << endl;
	};
	return 0;
};