#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main(){
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int t,n;
	int i,j,k,l;
	double temp,temp2;
	int count,count2;
	string s;
	char c[108][108];
	double wp[108];
	double owp[108];
	double oowp[108];
	cin >> t;
	for(i=1;i<=t;i++){
		cout << "Case #" << i << ":" <<endl;
		cin >> n;
		for(j=1;j<=n;j++){ 
			getline(cin,s);
			for(k=1;k<=n;k++){
				cin.get(c[j][k]);
			}
		}
		for(j=1;j<=n;j++){
			temp=0;count=0;
			for(k=1;k<=n;k++){
				if(c[j][k]=='1'){
					temp++;
					count++;
				}else if(c[j][k]=='0'){
					count++;
				}
			}
			wp[j]=temp/count;
		}
		for(j=1;j<=n;j++){
			temp=0;temp2=0;count=0;count2=0;
			for(k=1;k<=n;k++){
				if(k==j)continue;
				count=0;temp=0;
				if(c[j][k]=='0' || c[j][k]=='1'){
					for(l=1;l<=n;l++){
						if(l==k || l==j)continue;
						if(c[k][l]=='1'){
							temp++;
							count++;
						}else if(c[k][l]=='0'){
							count++;
						}
					}
					count2++;
					temp2+= temp/count;
				}
			}
			owp[j]=temp2/count2;
		}

		for(j=1;j<=n;j++){
			temp=0;count=0;
			for(k=1;k<=n;k++){
				if(j==k) continue;
				if(c[j][k]=='1' || c[j][k]=='0'){
					count++;
					temp+=owp[k];
				}
			}
			oowp[j]=temp/count;
		}
		for(j=1;j<=n;j++){
			cout << 0.25*wp[j]+0.5*owp[j]+0.25*oowp[j] << endl;
		}

	}
}