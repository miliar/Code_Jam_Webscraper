#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
	
	int T;
	cin >> T;
	for (int z=0;z<T;z++) {
		int N;
		cin >> N;
		
		// results
		vector<double> rpi(N,0),wp(N,0),owp(N,0),oowp(N,0);

		// source
		vector<int> raw1(N,-1);
		vector< vector<int> > raw2(N,raw1);
		for (int i=0;i<N;i++) {
			string str;
			cin >> str;
			for (int j=0;j<N;j++) {
				if (i==j || str[j]=='.')
					continue;
				if (str[j]=='1')
					raw2[i][j] = 1;
				else
					raw2[i][j] = 0;
			}
		}

		// wp
		for (int i=0;i<N;i++) {
			int sum = 0, cc = 0;
			for (int j=0;j<N;j++)
				if (raw2[i][j]==-1)
					continue;
				else {
					cc ++;
					sum +=raw2[i][j];
				}
			wp[i] = sum*1.0/cc;
		}

		//owp
		for (int i=0;i<N;i++) {
			//find oppents
			vector<int> oppI;
			for (int j=0;j<N;j++)
				if (raw2[i][j]!=-1)
					oppI.push_back(j);

			// calculate opponents wp with column out
			int nOppI = oppI.size();
			vector<double> oppIwp(nOppI,0.0);
			for (int j=0;j<nOppI;j++) {
				double sum=0.0;
				int cc = 0;
				for (int k=0;k<N;k++)
					if (k==i || raw2[oppI[j]][k]==-1)
						continue;
					else {
						cc ++;
						sum += raw2[oppI[j]][k];
					}
				oppIwp[j] = sum/cc;
			}

			double sum = 0.0;
			for (int j=0;j<nOppI;j++)
				sum += oppIwp[j];

			owp[i] = sum/nOppI;
		}

		//oowp
		for (int i=0;i<N;i++) {
			// oppI
			vector<int> oppI;
			for (int j=0;j<N;j++)
				if (raw2[i][j]!=-1)
					oppI.push_back(j);

			// 
			int nOppI = oppI.size();
			double sum = 0.0;

			for (int j=0;j<nOppI;j++) {
				sum += owp[oppI[j]];
			}

			oowp[i] = sum/nOppI;
		}

		for (int i=0;i<N;i++)
			rpi[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];

		// output
		cout << "Case #" << z+1 << ":" << endl;
		for (int i=0;i<N;i++)
			cout << rpi[i] << endl;

	} // end one case
}