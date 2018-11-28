#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <deque>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <cstdio>

#define MAX(x,y) ((x)>(y))?(x):(y)
#define MIN(x,y) ((x)<(y))?(x):(y)
#define ABS(x)   ((x)>0)  ?(x):(-x)
#define SQR(x)    (x)*(x)



using namespace std;

struct DTree{
	double w;
	string f;
	DTree * y;
	DTree * n;
	DTree():f(""),y(NULL),n(NULL){};
	void read(){
		char c=' ';
		while(c!='(') cin>> c;
		cin >> w;
		c=' ';
		while(c==' ' ||  c=='\n') cin >> c;
		if(c==')'){
			return;
		} else {
			cin.putback(c);
			cin >> f;
			y=new DTree();
			y->read();
			n=new DTree();
			n->read();
		}
		while(c!=')') cin>> c;
		return;
	};
	void getcute(double &C, vector<string> &vf){
		C*=w;
		if (f=="") return;
		vector<string>::iterator i;
		if ((i=find(vf.begin(), vf.end(), f))==vf.end()) {
			n->getcute(C, vf);
		} else {
			vf.erase(i);
			y->getcute(C, vf);
		}
		return;
	};
};
			
main(){
	int N;
	cin >> N;
	for(int n=0; n<N; n++){
		int L;
		cin >> L;
		DTree root;
		root.read();
		cin >> L;
		cout << "Case #" << n+1 << ":" << endl;
		for(int l=0; l<L; l++){
			string name;
			int F;
			cin >> name >> F;
			vector <string> vf;
			for(int f=0; f<F; f++){
				string fn;
				cin >> fn;
				vf.push_back(fn);
			}
			double cute=1.0;
			root.getcute(cute,vf);
			printf("%9.7f\n",cute);
		}
	}
}	
	
