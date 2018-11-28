#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<fstream>
#include<map>   
using namespace std;
static vector<int> numbers;
static map<int,int> rep;


int main(){
	ifstream cin;
	ofstream cout;
	cin.open("A-large.in");
	cout.open("out.txt");
	int n;
	cin>>n;
	for(int k=0;k<n;k++){
		bool X=false, O=false, empty=false;
		vector<string> a;
		for(int i=0;i<4;i++){
			string s;	
			cin>>s;
			a.push_back(s);
		}

		//check rows

		for(int i=0;i<4;i++){
			int x=0,o=0,t=0;

			for(int j=0;j<4;j++){
				if(a[i][j]=='X') x++;
				else if(a[i][j]=='O') o++;
				else if(a[i][j]=='T') t++;
				else empty=true;
			}
			if(x+t==4) X=true;
			if(o+t==4) O=true;
		}

		for(int j=0;j<4;j++){
			int x=0,o=0,t=0;

			for(int i=0;i<4;i++){
				if(a[i][j]=='X') x++;
				else if(a[i][j]=='O') o++;
				else if(a[i][j]=='T') t++;
				else empty=true;
			}
			if(x+t==4) X=true;
			if(o+t==4) O=true;
		}
		int x=0,o=0,t=0;
		for(int i=0;i<4;i++){
			if(a[i][i]=='X') x++;
			else if(a[i][i]=='O') o++;
			else if(a[i][i]=='T') t++;
			else empty=true;
		}
		if(x+t==4) X=true;
		if(o+t==4) O=true;

		x=0,o=0,t=0;
		for(int i=0;i<4;i++){
			if(a[i][3-i]=='X') x++;
			else if(a[i][3-i]=='O') o++;
			else if(a[i][3-i]=='T') t++;
			else empty=true;
		}
		if(x+t==4) X=true;
		if(o+t==4) O=true;


		cout<<"Case #"<<k+1<<": ";
		if(X) cout<<"X won";
		else if(O) cout<<"O won";
		else if(!empty) cout<<"Draw";
		else cout<<"Game has not completed";

		cout<<endl;




	}





	return 0;

}


