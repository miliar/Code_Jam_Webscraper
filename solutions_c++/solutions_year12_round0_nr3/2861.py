#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}

int main(){
	//freopen("test.in", "rt", stdin);
	freopen("cs.in", "rt", stdin);
	freopen("cs.out","wt", stdout);

	int nCases=1;
	cin>>nCases;
	for (int nCase=1;nCase<=nCases;nCase++) {
		cout<<"Case #"<<nCase<<": ";

		int a,b;
		cin>>a>>b;

		int res=0;

		for (int i=a;i<=b;i++) {
			string orgNum=toString<int>(i);
			string newNum;
			vector<int> pairedWith;
			for (int j=1;j<orgNum.length();j++) {
				newNum=orgNum.substr(orgNum.length()-j)+orgNum.substr(0,orgNum.length()-j);
				int iNewNum=toInt(newNum);
				if (iNewNum>i && iNewNum<=b) {
					newNum=toString<int>(iNewNum);
					if (newNum.length()==orgNum.length())
						if (find(pairedWith.begin(),pairedWith.end(),iNewNum)==pairedWith.end()) {
							pairedWith.push_back(iNewNum);
							res++;
						}
				}
			}
		}

		cout<<res<<endl;
	}

	return 0;
}
