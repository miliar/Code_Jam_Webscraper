#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;



int main()
{
	int T, t, x, il, y, inpcount;
	long long ct, mult;
	char inpstr[70];
	char basestr[40] = "0123456789abcdefghijklmnopqrstuvwxyz";
	int strvalue[40], inpvalue[70];
	ifstream myfile ("input.in");
	ofstream output ("output.txt", ios::trunc);
	
	
	myfile >> T;
	for (t=1;t<=T;t++) {
		myfile >> inpstr;
		il = strlen(inpstr);
		if (il>1) {
			for (y=0;y<36;y++) { strvalue[y]=-1; }
			inpcount=0;
			for (x=0;x<il;x++) {
				for (y=0;y<36;y++) {
					if (inpstr[x]==basestr[y]) {
						if (strvalue[y]==-1) {
							if (inpcount==0) strvalue[y] = 1;
							if (inpcount==1) strvalue[y] = 0;
							if (inpcount>1) strvalue[y] = inpcount;
							inpcount++;
						}
						inpvalue[x]=strvalue[y];
					}
				}
			}

cout << t << " " << inpstr << " " << inpcount << " ";
//output << t << " " << inpstr << " " << inpcount << " ";
for (x=0;x<il;x++) {
	cout << inpvalue [x] << " ";
//	output <<inpvalue [x] << " ";
}
cout << "\n";
//output <<"\n";

			if (inpcount==1) inpcount=2;
			mult=1;
			ct=0;
			for (x=il-1;x>-1;x--) {
//				output << ct << " " << mult << " " << inpvalue[x] << " ";
				ct = ct + (mult * inpvalue[x]);
				mult = mult * inpcount;
			}
//			output <<"\n";
		}
		else ct=1;

		cout << t << " " << ct << "\n";
		output << "Case #" << t << ": " << ct << "\n";


		
	}


	
	return 0;
}