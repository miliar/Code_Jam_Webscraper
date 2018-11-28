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
		int S, Q, Ans, last, templast, current;
		string temp;
		vector<string > Ss;
		vector<string > Qs;
		mFile >> S;
		getline(mFile,temp);

		for (int i=0;i<S;i++) {
			getline(mFile,temp);
			Ss.push_back(temp);
		}

		mFile >> Q;
		getline(mFile,temp);
		for (int i=0;i<Q;i++) {
			getline(mFile,temp);
			Qs.push_back(temp);
		}

		Ans=0;
		last=0;
		current=0;

		while (current<Q-1) {
			for (int i=0;i<S;i++) {
				if (find(Qs.begin()+current,Qs.end(),Ss[i])!=Qs.end()) {
					templast = find(Qs.begin()+current,Qs.end(),Ss[i])-Qs.begin();
					last = (templast>last)?templast:last;
				}
				else {
					last=Q;Ans--;break;
				}
			}
			current=last;
			Ans++;
		}

		cout << "Case #" << i+1 << ": " << Ans << endl;
	};
	return 0;
};