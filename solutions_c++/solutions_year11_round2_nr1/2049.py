#include<vector>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<limits>
#include<string>
#include<map>
#include<set>
using namespace std;
void process();
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cout<<"Case #"<<i<<": "<<endl;
		process();
	}
}

void process() {
	int n;
	cin>>n;
	vector<vector<char> >	vd;
	for(int i=0;i<n;i++) {
		vector<char> row;
		for(int i=0;i<n;i++) {
			char ch;
			cin>>ch;
			row.push_back(ch);
		}
		vd.push_back(row);
	}
	vector<double >wp;
	//compute wp
	for(int i=0;i<n;i++) {
		vector<char> row = vd[i];
		double sum =0;
		int step=0;
		for(int j=0;j<n;j++) {
			if(row[j]=='1') {
				sum+=1.0;
			}
			if(row[j]!='.') {
				step++;
			}
		}
		wp.push_back(sum/step);
//		cout<<"wp"<<i<<" "<<wp[i]<<endl;
	}
	//compute owp and oowp
	vector<double>owp;
	for(int i=0;i<n;i++) {
		//compute i's owp
		double iowp=0;
		int count=0;
		vector<char> row = vd[i];
		for(int j=0;j<n;j++) {
			if(row[j]!='.') {
			count++;
				//compute the j's owp
				vector<char> orow = vd[j];
				double tempowp=0;
				int step =0;
				for(int k=0;k<n;k++) {
					if(k!=i) {
						if(orow[k]=='1') {
							tempowp+=1.0;
						} 
						if(orow[k]!='.') {
							step++;
						}
					}
				}
				iowp+=(tempowp/step);
			}
		}
	
		owp.push_back(iowp/count);
//		cout<<"owp"<<owp[i]<<endl;
	}
	vector<double> oowp;
	for(int i=0;i<n;i++) {
		double ioowp = 0;
		int step =0;
		vector<char> row = vd[i];
		for(int j=0;j<n;j++) {
			if(row[j]!='.') {
				step++;
				ioowp+=owp[j];
			}
		}
		oowp.push_back(ioowp/step);
	}
	
	for(int i=0;i<n;i++) {
		double rpi = 0.25*wp[i]+0.5*owp[i] + 0.25*oowp[i];
		cout<<rpi<<endl;
	}
}
