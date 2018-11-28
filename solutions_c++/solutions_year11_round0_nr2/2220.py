
//Problem B

#include <iostream>

using namespace std;

int n,c,d;

int combine[26][26];
int opposed[26][26];
int invoke[100];
int seq[100];
int seqn;

void co(){
	int a,b;
	int i;
	if (seqn<2) return;
	a=seqn-2; b=seqn-1;
	//if (a<0) return;
	if (combine[seq[a]][seq[b]]>0){
		seq[a]=combine[seq[a]][seq[b]]-'A';
		seqn--;
		return;
	}
	for (i=0;i<b;i++){
		if (opposed[seq[i]][seq[b]]){
			seqn=0;
			return;
		}
	}
}

void compute(){
	int i,j;
	seqn=0;
	for (i=0;i<n;i++){
		seq[seqn]=invoke[i];
		seqn++;
		co();
	}
}

int main(){
	int t;
	int i,j;
	char c1,c2,c3;

	cin>>t;
	for (i=0;i<t;i++){
		memset(combine,0,26*26*sizeof(int));
		memset(opposed,0,26*26*sizeof(int));
		cin>>c;
		for (j=0;j<c;j++){
			cin>>c1>>c2>>c3;
			//cout<<":"<<c1<<c2<<c3<<" ";
			combine[c1-'A'][c2-'A']=c3;
			combine[c2-'A'][c1-'A']=c3;
		}
		cin>>d;
		for (j=0;j<d;j++){
			cin>>c1>>c2;
			//cout<<":"<<c1<<c2<<" ";
			opposed[c1-'A'][c2-'A']=1;
			opposed[c2-'A'][c1-'A']=1;
		}
		cin>>n;
		for (j=0;j<n;j++){
			cin>>c1;
			invoke[j]=c1-'A';
			//cout<<invoke[j];
		}

		compute();
		cout<<"Case #"<<(i+1)<<": [";
		for (j=0;j<seqn;j++){
			if (j>0) cout<<", ";
			cout<<((char)(seq[j]+'A'));
			//cout<<seq[j];
		}
		cout<<"]"<<endl;
	}
}
