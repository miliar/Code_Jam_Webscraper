#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.out");
	int t;
	fin>>t;
	for(int ci=1;ci<=t;ci++){
		string tmpstr;
		fin>>tmpstr;
		vector<int> db;
		for(int i=0;i<tmpstr.size();i++){
			db.push_back(tmpstr[i]-'0');
		}
		int pos;
		for(pos=db.size()-1;pos>0;pos--){
			if(db[pos]>db[pos-1]) break;
		}
		if(pos==0){
			int min=10, min_i;
			for(int i=0;i<db.size();i++){
				if(db[i]<min && 0<db[i]){
					min=db[i];
					min_i=i;
				}
			}
			db[min_i] = 0;
			sort(db.begin(), db.end());
			fout<<"Case #"<<ci<<": ";
			fout<<min;
			for(int i=0;i<db.size();i++)
				fout<<db[i];
			fout<<endl;
			continue;
		}
		int min=10, min_i;
		for(int i=pos;i<db.size();i++){
			if(db[i]<min && db[pos-1]<db[i]){
				min=db[i];
				min_i=i;
			}
		}
		db[min_i] = db[pos-1];
		db[pos-1] = min;
		sort(db.begin()+pos, db.end());
		fout<<"Case #"<<ci<<": ";
		for(int i=0;i<db.size();i++)
			fout<<db[i];
		fout<<endl;
	}
}