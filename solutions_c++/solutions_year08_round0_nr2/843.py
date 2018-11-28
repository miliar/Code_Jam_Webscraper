#include <iostream>
#include <string>
#include <sstream>
using namespace std;

string addit(string a, int q) {
	istringstream s(a);
	char temp;
	int h,m;
	s >> h >> temp >> m;
	m = m + q;
	h+=m/60;
	m = m%60;
	char out[15];
	sprintf(out, "%02d:%02d",h,m);
	string outs(out);
	return outs;
}

int main() {
	int n, test = 1, t, na, nb;
	string ad[105], aa[105], bd[105], ba[105];
	bool cad[105], caa[105], cbd[105], cba[105];
	int i,j, ca, cb;
	cin >> n;
	
	while(n--) {
		cin >> t >> na >> nb;
		ca = na; cb = nb;
		for(i=0;i<na;i++) {
			cin >> ad[i] >> aa[i];
			cad[i] = caa[i] = false;
		}
		for(i=0;i<nb;i++) {
			cin >> bd[i] >> ba[i];
			cbd[i] = cba[i] = false;
		}
		
		for(i=0;i<na;i++) {
			string x = addit(aa[i],t);
			string min;
			int min_pos = -1;
			for(j=0;j<nb;j++) {
				if(!cbd[j] && x.compare(bd[j])<=0)
					if(min_pos==-1 || bd[j]<min) {
						min = bd[j];
						min_pos = j;
					}
			}
			if(min_pos!=-1) {
				caa[i] = true;
				cbd[min_pos] = true;
				cb--;
			}
		}
		
		for(i=0;i<nb;i++) {
			string x = addit(ba[i],t);
			string min;
			int min_pos = -1;
			for(j=0;j<na;j++) {
				if(!cad[j] && x.compare(ad[j])<=0)
					if(min_pos==-1 || ad[j]<min) {
						min = ad[j];
						min_pos = j;
					}
			}
			if(min_pos!=-1) {
				cba[i] = true;
				cad[min_pos] = true;
				ca--;
			}
		}
		
		cout << "Case #" << (test++) << ": " << ca << " " << cb << endl;
	}
	return 0;
}
