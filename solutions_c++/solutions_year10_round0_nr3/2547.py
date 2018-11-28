#include <iostream>
#include<fstream>
#include<Cstring>
using namespace std;

const char infile[] = "E://C-small-attempt0.in";
const char outfile[] = "E://robeywin.out";

int main(){
	
	ofstream o_file;
    ifstream i_file;
	i_file.open(infile);
	o_file.open(outfile);

	int T;
	int g[10];
	char a[10];
	i_file>>T;
	for(int i=1;i<=T;i++){
		int R,k,N;
		i_file>>R>>k>>N; //R-round,k people,N group
		int count=0;
		memset(g,0,sizeof(g));
		for(int j=0;j<N;j++){
			i_file>>g[j];
		}
		
		int t=0;
		for(int rou=0;rou<R;rou++){
			memset(a,0,sizeof(a));
			int r=0;
			while((r+g[t]<=k)&&(a[t]==0)){
				r+=g[t];
				a[t]=1;
				t++;
				t%=N;
			}
			count+=r;			
			if(rou==R-1)
				o_file<<"Case #"<<i<<": "<<count<<endl;
		}
	}

	i_file.close();
	o_file.close();
	return 0;
}