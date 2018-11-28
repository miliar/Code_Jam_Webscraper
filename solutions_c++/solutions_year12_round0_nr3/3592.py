#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<map>
#include<fstream>


using namespace std;

int main(){
	ifstream in;
	ofstream out;
	in.open("C-small.txt");
	out.open("C-small_out.txt");
	int T;
	in>>T;
	for(int C=1;C<=T;++C){
		int A,B;
		in>>A>>B;
		int res=0;
		for(int n=A;n<B;++n){
			stringstream ss;
			ss<<n;
			string str;
			ss>>str;
			map<string,int>mapa;
			for(int j=0;j<str.size();++j,str=str.substr(1,str.size()-1)+str[0]){
				int m;
				stringstream ss2;
				ss2<<str;
				ss2>>m;
				if(mapa[str]==1)continue;
				if(m<=B)
					if(n<m)
						res++;
				mapa[str]=1;
			}
		}
		out<<"Case #"<<C<<": "<<res<<endl;
	}
	in.close();
	out.close();
	return 0;
}