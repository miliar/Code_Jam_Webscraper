#include<fstream>
#include<iostream>

using namespace std;

#define MAX	200

int x[2][MAX],r[MAX],nx[2];

int main(){

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	cin.rdbuf(fin.rdbuf());
	cout.rdbuf(fout.rdbuf());

	char ch;
	int ntc,n,p,nx[2],rx[2],px[2],ret,d,k,np,res;

	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n;
		nx[0] = nx[1] = 0;
		for (int i=0;i<n;i++){
			cin >> ch >> p;		
			if (ch=='O'){
				x[0][nx[0]++] = p;
				r[i] = 0;
			}
			else{
				x[1][nx[1]++] = p;
				r[i] = 1;
			}
		}
		res = 0;
		px[0] = px[1] = 1;
		rx[0] = rx[1] = 0;
		x[0][nx[0]++] = 1;
		x[1][nx[1]++] = 1;
		for (int i=0;i<n;i++){
			ret = r[i];
			p = px[ret];
			np = x[ret][rx[ret]];
			d = abs(p-np);
			rx[ret]++;
			px[ret] = np;
			//
			ret = 1-ret;
			px[ret] += ((k = (px[ret]-x[ret][rx[ret]]))>0)?-min(abs(k),d+1):min(abs(k),d+1);
			//
			res+=d+1;
		}
		cout << "Case #" << tc << ": " << res << endl;
	}


	

	return 0;
}