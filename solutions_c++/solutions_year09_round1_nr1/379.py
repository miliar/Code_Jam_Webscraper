#include<iostream>
using namespace std;

#define MAXSZ 30000000

int happy[MAXSZ][11];

int ani(int n, int b);

int main(){
	int T;
	cin>>T;
	char ch;
	while(true){
		scanf("%c", &ch);
		//cout<<ch<<endl;
		if(ch=='\n') break;
	}
	
	for(int i=0; i<MAXSZ; i++) for(int j=0; j<11; j++)
		happy[i][j]=2;
	for(int i=2; i<11; i++) happy[1][i]=1;
	for(int i=2; i<MAXSZ; i++){
		for(int j=2; j<11; j++)
			ani(i, j);
		bool alldone=true;
		for(int j=2; j<11; j++) if(happy[i][j]!=1) alldone=false;
		if(alldone){ break; }
		//cout<<i<<endl;
	}
	
	for(int t=1; t<=T; t++){
		int len=0, list[10];
		while(true){
			while(true){
				scanf("%c", &ch);
				//cout<<ch<<endl;
				if(ch!=' ') break;
			}
			if(ch=='\n') break;
			list[len]=ch-'0';
			while(true){
				scanf("%c", &ch);
				//cout<<ch<<endl;
				if(ch<'0' || ch>'9') break;
				list[len]=10*list[len]+(ch-'0');
			}
			len++;
			if(ch=='\n') break;
		}
		int ans=2;
		while(true){
			bool done=true;
			for(int i=0; i<len; i++) if(happy[ans][list[i]]!=1)
				{ done=false; break; }
			if(done) break;
			ans++;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
		//for(int i=0; i<len; i++) cout<<list[i]<<" ";
		//cout<<endl;
	}
	return 0;
}

int ani(int n, int b){
	//cout<<n<<" "<<b<<" "<<happy[n][b]<<endl;
	if(happy[n][b]==3) return 0;
	if(happy[n][b]==0 || happy[n][b]==1) return happy[n][b];
	
	int next=0, d, t=n;
	while(n>0){
		d=n%b;
		n/=b;
		next+=d*d;
	}
	happy[t][b]=3;
	int result=ani(next, b);
	happy[t][b]=result;
	return happy[t][b];
}
