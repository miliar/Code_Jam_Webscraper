#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

using namespace std;

ifstream fin;
ofstream out;
vector<long long> list;
long long maxv = -1;
int total;

void search(int cur,long long inx,long long ins,long long ox,long long os){
	//cout << cur << " " << inx << " " << ins << " " << ox << " " << os << endl; 
	if(cur >= total - 1){
		if(inx == ox && ins != 0 && os != 0) {
			long long mm  = (ins > os) ? ins : os;
			maxv = (maxv > mm) ? maxv : mm;
		}
		return;
	}
	long long value = list[cur];
	//if in
	long long newinx = inx ^ value;
	long long newins = ins + value;
	
	search(cur+1,newinx,newins,ox,os);
	//if not
	long long newox = ox ^ value;
	long long newos = os + value;
	search(cur+1,inx,ins,newox,newos);
}


int main(int argc,char** argv) {
	fin.open(argv[1]);
	out.open(argv[2]);

	int cnum = 0;
	fin >> cnum;

	for(int i = 0; i < cnum; i++) {
		
		out << "Case #" << i + 1 << ": ";

		maxv = -1;
		list.clear();
		fin >> total;
		int tmp = 0;
		for(int j = 0; j < total; j++){
			fin >> tmp;
			list.push_back(tmp);
		}
	    list.pop_back();
		search(0,tmp,tmp,0,0);

		if(maxv < 0) {
			out << "NO" << endl;
		} else {
			out << maxv << endl;
		}

	}


	fin.close();
	out.close();
}
