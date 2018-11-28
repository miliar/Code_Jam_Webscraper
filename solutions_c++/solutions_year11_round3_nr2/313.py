#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int NMAX=1000;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t,it;
	int mas[NMAX]={0};
	vector<int> v;
	fin>>t;
	for(it=1;it<=t;++it){
		v.clear();
		long long l,t,n,c,time;
		int i;
		time=0;
		fin>>l>>t>>n>>c;

		for(i=0;i<c;++i){
			fin>>mas[i];
		}

		for(i=0;i<n;++i){
			if(t>=2*mas[i%c]){
				t-=2*mas[i%c];
				time+=mas[i%c]*2;
			}
			else{
				v.push_back(2*mas[i%c]-t);
				time+=t;
				t=0;
			}
		}

		sort(v.begin(),v.end());
		while(l>0&&!v.empty()){
			time+=v.back()/2;
			v.pop_back();
			--l;
		}
		while(!v.empty()){
			time+=v.back();
			v.pop_back();
		}
		fout<<"Case #"<<it<<": "<<time<<endl;
	}

	return 0;
}