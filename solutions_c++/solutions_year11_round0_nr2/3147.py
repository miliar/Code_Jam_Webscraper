#include<iostream>
#include<fstream>
#include<map>
#include<vector>


#define pb push_back
using namespace std;

int main(int argc, char **argv){
	ifstream ifs(argv[1]);

	int T;

	ifs>>T;

	int times=0;
	while(T--){
		++times;

		vector<string> combine, opposed;
		int C,D,N;
		ifs>>C;

		string temp;
		while(C--){
			ifs>>temp;
			combine.pb(temp);
		}

		ifs>>D;

		while(D--){
			ifs>>temp;
			opposed.pb(temp);
		}

		ifs>>N;

		string str;
		ifs>>str;

		string ans="";

		map<char, int> M;
		for(int i=0;i<str.size();i++){
			ans+=str[i];	
			M[ str[i] ]++;
			if(ans.size()<=1)
				continue;

			bool flag=false;
			int size = ans.size();
			for(int j=0;j<combine.size();j++){

				if((ans[size-1]==combine[j][0] && ans[size-2]==combine[j][1]) || (ans[size-1]==combine[j][1] && ans[size-2]==combine[j][0])){
					M[ ans[size-1] ]--;
					ans.erase( size-1, 1);
					M[ ans[size-2] ]--;
					ans.erase( size-2, 1);
					ans+=combine[j][2];
					flag=true;
					break;
				}
			}


			if(flag)
				continue;

			for(int j=0;j<opposed.size();j++){

				if( M[opposed[j][0]]>=1 && M[opposed[j][1]]>=1){
					ans="";
					M.clear();
					break;
				}
			}

		}

		cout<<"Case #"<<times<<": [";
		for(int i=0;i<ans.size();i++){
			cout<<ans[i];
			if(i!=ans.size()-1)
				cout<<", ";
		}
		cout<<"]\n";
	}
	return 0;
}
