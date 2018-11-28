#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	
	ifstream fin("small");
	ofstream fout("answersmall");
	int T,N,S,p,t,tot,no=1;
	fin>>T;
	//cout<<T<<endl;
	while (T--) {

		fin>>N>>S>>p;
		tot=0;	
		for (int i = 0; i < N; i++ ) {
			fin>>t;
			int tmp1 = t%3, tmp2 = t/3;
			if (t < p) continue;
			if (tmp2 >= p) {
				tot++;
				continue;
			}
			if (tmp1 == 0) {
				tmp2++;
				if (tmp2 >= p && S) {
					tot++;
					S--;
					continue;
				}

			}
			if (tmp1 >= 1) {
				tmp2++;
				if (tmp2 >=p) {
					tot++;
					continue;
				}	
			}
			if (tmp1 == 2) {
				tmp2++;
				if (tmp2 >=p && S) {
					tot++;
					S--;
					continue;
				}	
			}
	
		}
		fout<<"Case #"<<no++<<": "<<tot<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
