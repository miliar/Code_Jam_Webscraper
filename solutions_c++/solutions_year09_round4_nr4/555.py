#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double dist(double x1, double y1, double x2, double y2){
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main(){
	int T, N;
	double x[40], y[40], r[40]; 
	double R;
   	

	cin >> T >> ws; 

	for (int cnt = 1; cnt <=T; ++cnt){
		cin >> N;
		for (int i=0; i<N; ++i){
			cin >> x[i] >> y[i] >> r[i];
		}
		if (N==1){
			R = r[0];
		} else if (N==2){
			R = max(r[0], r[1]);
		} else {
			double temp;
			for (int i=0; i<N; ++i){
				temp = r[i];
				double temp2 = dist(x[(i+1)%N], y[(i+1)%N], x[(i+2)%N], y[(i+2)%N])+r[(i+1)%N]+r[(i+2)%N];
				temp2 /=2;
				if (temp2 > temp)
					temp = temp2;
				if (i==0 || temp < R){
					R = temp;
				}
			}
		}


		cout.setf(ios::fixed);
		cout << "Case #" << cnt << ": ";
		cout << setprecision(5) << R;
		cout << endl;
	}

	cerr << "Program Terminated Properly." << endl;

	return 0;
}
