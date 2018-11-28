#include <iostream>
#include <iomanip>
#include <cstring>
using namespace std;
int main(){
	char s[1000];
	char ref[] = "welcome to code jam";
	int mat[20][1000],i,j;
	int n,len,reflen=strlen(ref);
	cin>>n;
	cin.getline(s,1000);
	for(int x=0;x<n;x++){
		cin.getline(s,1000);
		len = strlen(s);
		//cout<<len<<endl<<s<<endl;
		for(i=0;i<reflen+1;i++)
			for(j=0;j<len+10;j++)
				mat[i][j]=0;

		for(j=len-1;j>=0;j--){
			if(s[j]=='m'){
				mat[18][j]=1;
			}
			mat[18][j]+=mat[18][j+1];
			//cout<<mat[i][j];
		}
		for(i=17;i>=0;i--){
			for(j=len-1;j>=0;j--){
				if(s[j]==ref[i]){
					mat[i][j]=mat[i+1][j+1];
				}
				mat[i][j]=(mat[i][j]+mat[i][j+1])%1000;
				//cout<<mat[i][j];
			}
			//cout<<endl;
		}
		cout << "Case #"<<(x+1)<<": "<< setw(4) << setfill('0') << mat[0][0]<<endl;
	}
}
