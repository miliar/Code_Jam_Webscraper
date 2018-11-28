#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int main(){
	ifstream fin;
	fin.open("B-Large.in");
	ofstream fout;
	fout.open("B-Large.out");
	int C,N,K,B,T;
	fin >> C;
	for(int i=0;i<C;i++){
		fin >> N >> K >> B >> T;
		vector <int> vx;
		for(int j=0;j<N;j++){
			int x;
			fin >> x;
			vx.push_back(x);
		}
		vector <int> vv;
		for(int j=0;j<N;j++){
			int v;
			fin >> v;
			vv.push_back(v);
		}
		vector <int> canreach;
		canreach.assign(vv.size(),0);
		for(int j=0;j<vv.size();j++){
			if(vx[j]+T*vv[j]>=B) canreach[j] = 1;
		}
		int z = count(canreach.begin(),canreach.end(),1);
		int nswaps = 0;
		if((z >=K)&&(z>=1)){
			int w = 0;			
			int ind = canreach.size()-1;
			while(true){
				if(canreach[ind] == 1){
					w++;
					if(w==K) break;
				}
				ind --;
			}
			for(int j=ind;j<canreach.size();j++){
				if(canreach[j] == 1){
					int q = find(vx.begin(),vx.end(),vx[j])-vx.begin();
					nswaps+= count(canreach.begin()+q,canreach.end(),0);
				}
			}
			fout <<"Case #" << i+1 << ": " << nswaps << endl;
		}
		else if (K==0) fout <<"Case #" << i+1 << ": " << 0 << endl;
		else fout  <<"Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
	}

	return 0;
}