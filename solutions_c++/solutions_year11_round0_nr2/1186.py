#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main(){
	freopen("B-small-attempt5.in","r",stdin);
	freopen("B-small-attempt5.out","w",stdout);
	int cases,i,j,k,p,q,c,d,n,resNum;
	scanf("%d",&cases);
	vector<char> res;
	vector<string> cs,ds;
	string str;
	for(i=1; i<=cases; i++){
		res.clear();
		cs.clear();
		ds.clear();
		resNum = 0;
		//C
		scanf("%d",&c);
		for(k=0; k<c; k++){
			cin>>str;
			cs.push_back(str);
		}
		//D
		scanf("%d",&d);
		for(k=0; k<d; k++){
			cin>>str;
			ds.push_back(str);
		}
		//N
		scanf("%d",&n);
		cin>>str;
		//solve
		int l = str.length();
		char c1,c2;
		k=0;
		for(j=0; j<l; j++){
			if (res.size() == 0) {
				res.push_back(str[j]);
				continue;
			}
			bool flag = false;
			//check combin
			for(k=0; k<cs.size(); k++){
				if ((str[j] == cs[k][0] && res[res.size()-1] == cs[k][1]) || (str[j] == cs[k][1] && res[res.size()-1] == cs[k][0])) {
					res[res.size()-1] = cs[k][2];
					flag = true;
					break;
				}
			}
			if (flag) continue;
			
			for(p=0; p<ds.size(); p++){	
				if (ds[p][0] == str[j]){
					for(k=0; k<res.size(); k++) {
						if (res[k] == ds[p][1]) {
							res.clear();
							flag = true;
							break;
						}
					}
				}
				if (flag) break;
				if (ds[p][1] == str[j]) {
					for(k=0; k<res.size(); k++) {
						if (res[k] == ds[p][p]) {
							res.clear();
							flag = true;
							break;
						}
					}
				}
				
			}
			if ( flag == false) {
				res.push_back(str[j]);
			}
		}

		printf("Case #%d: [",i);
		for(j=0; j<res.size(); j++){
			printf("%c", res[j]);
			if (j!= res.size()-1) printf(", ");
		}
		printf("]\n");
	}
	return 0;
}