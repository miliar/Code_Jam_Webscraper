#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i = 0 ; i < t; i++){
		int n,m,r = 0;
		cin>>n>>m;
		vector<string> p;
		vector<string> np;
		for(int j = 0 ; j < n; j++){
			string s;
			cin>>s;
			p.push_back(s);;
		}
		for(int k = 0; k < m; k++){
			string s;
			cin>>s;
			np.push_back(s);;
		}
		int old = p.size();
		//main code
		int sz = np.size();
		for(int a = 0 ; a < sz; a++ ){
			string pp = np[a];
			string ppc = "/";
			for(int b = 1; b < (int)pp.length(); b++){
				if(pp.at(b) == '/' ){
					bool got = false;
					for(int k = 0; k < (int)p.size(); k++){
						if(p[k] == ppc){
							got = true;
							break;
						}
					}
					if(!got){
						p.push_back(ppc);

					}
				}
				//ppc.append(pp.at(b));
				ppc += pp.at(b);
			}
			bool got = false;
			for(int k = 0; k < (int)p.size(); k++){
				if(p[k] == ppc){
					got = true;
					break;
				}
			}
			if(!got){
				p.push_back(ppc);

			}
		}
		r = p.size() - old;
		//eoc
		cout<<"Case #"<<i+1<<": "<<r<<endl;

	}
	//system("pause");
	return 0;
}