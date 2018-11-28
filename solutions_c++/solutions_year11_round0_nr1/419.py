#include <iostream>
#include <vector>
#define pb push_back

using namespace std;

int n;

inline int ABS(int k){
	return k<0 ? -k : k;	
}
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		int nowO= 1, nowB= 1;
		int timeO= 0, timeB= 0;
		cin >> n;
		for (int i=0 ; i<n ; i++){
			char ch;
			int k;
			cin >> ch >> k;
			if (ch=='O'){
				timeO+= ABS(nowO - k);
				nowO= k;
				if (timeO<timeB)
					timeO= timeB;
				timeO++;
			}else{
				timeB+= ABS(nowB - k);
				nowB= k;
				if (timeB<timeO)
					timeB= timeO;
				timeB++;
			}
		}
		int time= max(timeO, timeB);
		cout << "Case #" << t << ": " << time << endl;
	}
	return 0;
}