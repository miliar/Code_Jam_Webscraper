#include<iostream>
#include<vector>
#include<string>

using namespace std;

class Line{
public: 
	long a,b;
};

bool getsign(int a){
	if(a>=0) return true;
	return false;
}

int main(){
	int t;
	cin>>t;
	for(int i = 0 ; i < t; i++){
		int r = 0, n;
		cin>>n;
		vector<Line> line;
		for(int j = 0; j < n; j++){
			Line l;
			cin>>l.a>>l.b;
			line.push_back(l);

		}

		int sz = line.size();
		for(int k = 0; k < (int)sz; k++){
			for(int p = k+1 ; p < (int)sz; p++){
				int sub1 = line[k].a - line[p].a,
					sub2 = line[k].b - line[p].b;
				if((sub1 > 0 && sub2 < 0) || (sub1 < 0 && sub2 > 0)){
					r++;
				}

			}
		}


		cout<<"Case #"<<i+1<<": "<<r<<endl;

	}
	//system("pause");
	return 0;
}
