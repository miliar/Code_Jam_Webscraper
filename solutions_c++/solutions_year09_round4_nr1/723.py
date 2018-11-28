#include<iostream>
#include<string>
#include<fstream>

using namespace std;
int ar[50];
int actual[50];
bool computed[50];
int main(){
	ofstream fout("A.out");
	int ca,n;
	cin>>ca;
	for(int cas=1; cas<=ca; ++cas){
		cin>>n;
		string s;
		for(int i=0; i<n; ++i){
			cin>>s;
			bool found=false;
			for(int j=s.size()-1; j>=0; --j){
				if(s[j]=='1'){
					ar[i]=j;
					found=true;
					break;
				}
			}
			if(!found){
				ar[i]=-1;
			}
		}
		memset(computed,0, sizeof(computed));
		int tot=0;
		for(int i=0; i<n; ++i){
			for(int j=0; j<n; ++j){
				if(computed[j]) continue;
				if(ar[j]<=i){
					actual[j]=i;
					computed[j]=true;
					break;
				}
			}
		}
		for(int i=0; i<n; ++i){
			for(int j=i+1; j<n; ++j){
				if(actual[i]>actual[j])
					tot++;
			}
		}
		fout<<"Case #"<<cas<<": "<<tot<<endl;
	}
}
