#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

fstream fin("A-small-attempt3.in.txt",ios::in);
fstream fout("A-small-attempt3.out.txt",ios::out);

int main() {
	int cases, N;
	fin>>N;
	int i, j, res, num, query;
	//char name[102][200];
	int flag[200];
	string name;
	for (i=1; i<=N; i++) {
		fout<<"Case #"<<i<<": ";
		res = 0;
		fin>>num;
		fin.get();
		map<string,int> engine;
		memset(flag,0,sizeof(flag));
		for (j=1; j<=num; j++) {
			getline(fin,name,'\n');
			//fin.getline(name,sizeof(name[j]),'\n');
			engine[name] = j;
		//	cout<<name<<endl;
		}
		fin>>query;
		fin.get();
		int cnt = 0;
		for (j=0; j<query; j++) {
		//	fin.getline(name[101],sizeof(name[101]),'\n');
			getline(fin,name,'\n');
			int tmp = engine[name];
		//	cout<<name<<' '<<tmp<<endl;
			if (!flag[tmp])
				cnt++;
			flag[tmp] = 1;
			if ( num == cnt ) {
				memset(flag,0,sizeof(flag));
				flag[tmp] = 1;
				res++;
				cnt = 1;
			}
		}
		engine.clear();
		if ( cnt != 0 )
			res++;
		fout<<(res-1>0?res-1:0)<<endl;
	}
	return 0;
}