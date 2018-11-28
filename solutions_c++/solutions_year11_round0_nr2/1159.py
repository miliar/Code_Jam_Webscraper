#include <iostream>
#include <fstream>
#include <string>
using namespace std;
typedef struct{
	char base[2];
	char nonbase;
}combination;
int main(){

	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	int t;
	int i,j,k,l,m;
	int c,d,n;
	bool isClear;
	bool isComb;
	string s;
	combination comb[40];
	char oppose[50][2];
	//bool isOppose[50];
	//bool isCombi[40];
	char result[105];
	int length;
	cin >> t;
	for(i=1;i<=t;i++){
		length=0;
		cin >> c;
		for(j=0;j<c;j++){
			cin >> s;
			comb[j].base[0]=s[0];
			comb[j].base[1]=s[1];
			comb[j].nonbase=s[2];
			//isCombi[j]=false;
		}
		cin >> d;
		for(j=0;j<d;j++){
			cin >> s;
			oppose[j][0]=s[0];
			oppose[j][1]=s[1];
			//isOppose[j]=false;
		}
		cin >> n >> s;
		for(j=0;j<n;j++){
			isClear=false;
			isComb=false;
			for(k=0;k<d;k++){
				//if(isOppose[k])continue;
				for(m=0;m<2;m++){
					if(s[j]==oppose[k][1-m]){
						for(l=0;l<length;l++){
							if(result[l]==oppose[k][m]){
								//isOppose[j]=true;
								length=0;
								isClear=true;
								break;
							}
						}
					}
					if(isClear)break;
				}
			}
			if(isClear)continue;
			if(j+1<n){
				for(k=0;k<c;k++){
					//if(isCombi[k])continue;
					if((s[j]==comb[k].base[0] && s[j+1]==comb[k].base[1])||
						(s[j]==comb[k].base[1] && s[j+1]==comb[k].base[0])){
							result[length++]=comb[k].nonbase;
							//isCombi[k]=true;
							isComb=true;
							j++;
							break;
					}
				}
			}
			if(isComb)continue;
			result[length++]=s[j];
		}
		cout << "Case #" << i << ": [";
		for(j=0;j<length;j++){
			if(j>0){
				cout << ", " << result[j];
			}else{
				cout << result[j];
			}
		}
		cout << "]" << endl;
	}
	return 0;
}