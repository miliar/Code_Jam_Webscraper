#include<iostream>
#include<map>
using namespace std;
bool Generatable(char* word,string& cipher,int len){
	int i=0,header=0;
	bool braket=false,mismatch=false;
	if(cipher[0]=='(')braket=true,header=1;
	while(!mismatch){
		if(braket){
			mismatch=true;
			while(cipher[header]!=')'){
				if(cipher[header]==word[i]){
					mismatch=false;break;
				}
				header++;
			}
			while(cipher[header]!=')'){
				header++;
			}
		}
		else {
			if(cipher[header]!=word[i])mismatch=true;
		}
		i++;
		if(i==len)break;
		header++;
		if(cipher[header]!='(')braket=false;
		else braket=true,header++;
		
	}
	return !mismatch;
}
int main(){
	int L,D,N,cas=0,i=0,coun;
	cin>>L>>D>>N;
	char dictword[D][25];
	string cipher;
	while(i<D){
		cin>>dictword[i];
		i++;
	}
	while(cas++<N){
		cin>>cipher;
//		CountInterpretation(cipher);
		i=coun=0;
		while(i<D){
			if(Generatable(dictword[i],cipher,L))
				coun++;
			i++;
		}
		cout<<"Case #"<<cas<<": "<<coun<<endl;
	}
	return 0;
}
