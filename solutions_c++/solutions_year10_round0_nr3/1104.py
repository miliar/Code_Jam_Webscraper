#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int main () {
	fstream filestr;
	ofstream outstr;
	int cases;
	filestr.open("/Users/HOOI/Downloads/C-small-attempt3.in");
	outstr.open("/Users/HOOI/Downloads/GoogleCodeJam/PracticeOut.txt");
	filestr >> cases;
	vector<int> g;
	vector<int> h;
	for (int i=1;i<=cases;i++){
		g.clear();
		h.clear();
		int runs,cap,n;
		int sum=0;
		int psum=0;
		int cur=0;
		int htemp=0;
		map <int, int> m;
		vector<int> money;
		int pmoney=0;
		filestr >> runs >> cap >> n;
		for (int j=0;j<n;j++){ filestr >> htemp; h.push_back(htemp); }
		for (int j=0;j<n;j++) sum += h[j];
		for (int j=0;j<n;j++) g.push_back(h[j]);
		for (int j=0;j<n;j++) g.push_back(h[j]);
		cout << "WORKING ON VECTOR: ";
		for (int j=0;j<n;j++) cout << h[j]<<",";
		if (sum<=cap){
			cout << "Case #"<<i<<": "<< sum*runs << endl; 
			outstr << "Case #"<<i<<": "<< sum*runs << endl; continue;
		}
			
		for (int turn=0;turn<runs;turn++){
			psum=0;
			//INCREASE CURRENT
			for (int pos=cur;;pos++){ 
				if (psum+g[pos]<=cap){ psum += g[pos]; cout <<"psum->"<<psum<<endl;}
				else {
					cout <<"else!";
					pmoney += psum;
					money.push_back(pmoney);
					cur=pos%n;
					break;
				}
			}
			
			//SET AND CHECK MAP
			
			if (!m.count(cur)){
				m[cur]=turn;
				cout << "set m "<<cur<<" to "<<turn<<endl;
			}
			else {
				for (int l=0;l<money.size();l++) cout << "money "<<l<<" is "<<money[l]<<endl;
				
				int cyclelength = turn-m[cur]; cout <<"cyclelength is " <<cyclelength<<endl;
				int cyclemoney=money[turn]-money[m[cur]]; cout << "cyclemoney is "<<cyclemoney<<endl;
				int remainder = (runs-m[cur]-1) % cyclelength; cout << "remainder is " <<remainder<<endl;
				int rmoney = money[m[cur]+remainder]-money[m[cur]]; cout << "rmoney is "<<rmoney<<endl;
				int qmoney = ((runs-m[cur]-1)/cyclelength)*cyclemoney; cout << "qmoney is "<<qmoney<<endl;
				int smoney = money[m[cur]]; cout << "smoney is "<<smoney<<endl;
				int tmoney = rmoney + qmoney + smoney;
				cout << "Case #"<<i<<": "<<tmoney<<endl;
				outstr << "Case #"<<i<<": "<<tmoney<<endl;
				goto out;
			} //endelse
		} //endrunloop
		outstr << "Case #"<<i<<": "<<money[money.size()-1]<<endl;
		cout << "Case #"<<i<<": "<<money[money.size()-1]<<endl;
	out:;
	}//endcaseloop
	filestr.close();
	outstr.close();
	return 0;
}
