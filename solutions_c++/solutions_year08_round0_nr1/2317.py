#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
	ofstream out;
	out.open("save.out", ios::out);
	ifstream in;
	in.open("save.in", ios::in);
	string line;
	if (!in) { cout << "sux in"; }
	if (!out) { cout << "sux out"; }
	int n,s,q,i,j,k;
	int minv, minn;
	in >> n; 
	for (int l=0; l<n; l++){
		in >> s; getline(in,line);
		string se[s];
		for (i=0; i<s; i++) { getline(in,line); se[i]=line;}
		in >> q; getline(in,line);
		int a[s][q];
		minv=0; minn=0;
		for (j=0; j<s; j++) a[j][0]=0;
		for (i=1; i<=q; i++){
			//cout << i<< endl;
			//for (j=0; j<s; j++) cout <<a[j][i-1] << " " ;
			//cout <<endl;
			string current;
			getline(in,current); //cout << current << endl;
			minn=1000000;
			for (j=0; j<s; j++){
				if (current==se[j]) a[j][i]=-1;
				else{
					if (a[j][i-1]!=-1) a[j][i]=a[j][i-1];
					if ((a[j][i-1]==-1) || (minv+1<a[j][i])) a[j][i]=minv+1;
					if (a[j][i]<minn) minn=a[j][i];
				}
			}
			//for (j=0; j<s; j++) cout <<a[j][i] << " " ;
			//cout << endl;
			minv=minn;
		}
		out << "Case #" << l+1 << ": " << minn << endl;
		cout << "Case #" << l+1 << ": " << minn << endl;
	}
	out.close();
	in.close();
	return 0;
}
