#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main(){
	vector<int> vin;
	vector<char>vc;
	int n;
	cin >> n;
	char ch;
	int x;
	for(int t=0; t<n; t++){
		int p;
		cin >> p;
		for(int b=0; b<p; b++){
			cin >> ch;
			vc.push_back(ch);
			cin >> x;
			vin.push_back(x);
		}
		int tim1=0;
                int tim2=0;
                int x1=1;                      
		int x3=1;
                int x2,x4;
		for(int i=0; i<p; i++){
			if(vc[i]=='B'){
				x2=vin[i];
				if(max(tim1,tim2)-tim1 >=abs(x2-x1))
					tim1=max(tim1,tim2)+1;
				else
					tim1=tim1+abs(x2-x1)+1;
				x1=x2;
			}
			else if(vc[i]=='O'){
				x4=vin[i];
				if(max(tim1,tim2)-tim2>=abs(x4-x3))
					tim2=max(tim1,tim2)+1;
				else
					tim2=tim2+abs(x4-x3)+1;
				x3=x4;
			}
		}
		cout <<"Case #" << t+1<< ": " << max(tim1,tim2) << endl;
		vc.clear();
		vin.clear();
	}
	return 0;
}			
