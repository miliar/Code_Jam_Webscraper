#include <fstream>
#include <vector>

using namespace std;

const int NMAX=256;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t,it;
	char c1,c2,c3;

	fin>>t;
	for(it=0;it<t;++it){
		int c,d,n,comb[NMAX][NMAX],op[NMAX][NMAX];
		int i,j;
		vector<char> v;

		memset(comb,0,NMAX*NMAX*sizeof(int));
		memset(op,0,NMAX*NMAX*sizeof(int));
		v.clear();

		fin>>c;
		for(i=0;i<c;++i){
			fin>>c1>>c2>>c3;
			comb[c1][c2]=c3;
			comb[c2][c1]=c3;
		}
		fin>>d;
		for(i=0;i<d;++i){
			fin>>c1>>c2;
			op[c1][c2]=1;
			op[c2][c1]=1;
		}
		fin>>n;
		for(i=0;i<n;++i){
			fin>>c1;
			if(!v.empty()){
				if(comb[v[v.size()-1]][c1]!=0){
					c2=v[v.size()-1];
					v.pop_back();
					v.push_back(comb[c2][c1]);
				}
				else{
					for(j=0;j<v.size();++j){
						if(op[v[j]][c1]){
							v.clear();
							break;
						}
					}
					if(!v.empty()){
						v.push_back(c1);
					}
				}
			}
			else{
				v.push_back(c1);
			}
		}

		fout<<"Case #"<<it+1<<": "<<"[";
		for(i=0;i<(int)v.size()-1;++i){
			fout<<v[i]<<", ";
		}
		if(i<v.size()){
			fout<<v[i];
		}
		fout<<"]"<<endl;
	}
	return 0;
}