#include<iostream>
#include<map>
using namespace std;

int main(){
	int L, D, N;
	cin>>L>>D>>N;
	char str[32];
	char alien[D][L+1];
	
	for(int i=0; i<D; i++){
		cin>>alien[i];
	}
	for(int i=1; i<=N; i++){
		char pat[1024];
		cin>>pat;
		map<char, bool> m[1024];
		bool b=true;
		for(int j=0, k=0, l=strlen(pat); j<l; j++){
			if(pat[j]=='('){ b=false; continue; }
			if(pat[j]==')'){ b=true; k++; continue; }
			m[k][pat[j]]=true;
			if(b) k++;
		}
		int ans=0;
		for(int j=0; j<D; j++){
			bool p=true;
			for(int k=0; k<L; k++){
				if(m[k][alien[j][k]]==false){ p=false; break; }
			}
			if(p) ans++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
