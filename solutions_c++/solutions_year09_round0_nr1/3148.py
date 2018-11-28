#include<iostream>
#include<string>

using namespace std;

int l,d,n,counter=0;
string word[5000];
int  box(string surd);
int compare(int i,int j,int nong[50],int pong[50][256]);

int main(){
//	int l,d,n;
//	string word[50];
	int i;
	string surd;
	cin>>l>>d>>n;
	for(i=0;i<d;i++){
		cin>>word[i];
	}
	for(i=0;i<n;i++){
		cout<<"Case #"<<i+1<<": ";
		counter=0;
		cin>>surd;
		box(surd);
//		cout<<counter<<endl;
	}
	return 0;
}

int box(string surd){
	int i,j=0,k=0;
	int pong[l][256],nong[l];
	char c;
	for(i=0;i<l;i++){
		k=0;
		if(surd[j]=='('){
			j++;
			while(surd[j]!=')'){
				pong[i][k]=surd[j];
				k++;
				j++;
			}
			nong[i]=k;
			j++;
		}else{
			pong[i][0]=surd[j];
			nong[i]=1;
			j++;
		}
	}
//	cout<<nong[0]<<endl;
	for(i=0;i<nong[0];i++){
		for(j=0;j<d;j++){
			if(word[j][0]==pong[0][i]){
//				cout<<word[j]<<endl;
				compare(i,j,nong,pong);
			}
		}
	}
	cout<<counter<<endl;
}

int compare(int a,int b,int nong[50],int pong[50][256]){
	int i,j;
	for(i=1;i<l;i++){
		for(j=0;j<nong[i];j++){
			if(word[b][i]==pong[i][j]){
				break;
			}
		}
		if(j>=nong[i])
			return 0;
	}
	counter++;
	return 0;
}
