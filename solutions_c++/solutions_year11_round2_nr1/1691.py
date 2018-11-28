#include<iostream>

using namespace std;

void run(){
	int i,j;


	char **S;
	int S_x;

	double *wp,*owp,*oowp;
	int *wp_c;
	int c;

	cin>>S_x;
	S=new char*[S_x];

	wp=new double[S_x];
	wp_c=new int[S_x];
	owp=new double[S_x];
	oowp=new double[S_x];

	for(i=0;i<S_x;i++){
		S[i]=new char[S_x];
		wp[i]=0.0;
		wp_c[i]=0;
		for(j=0;j<S_x;j++){
			cin>>S[i][j];
			if(S[i][j]=='1'){
				wp[i]+=1.0;
				wp_c[i]++;
			}else if(S[i][j]=='0') wp_c[i]++;
		}
		wp[i]/=wp_c[i];
	}

	for(i=0;i<S_x;i++){
		c=0;
		owp[i]=0.0;
		for(j=0;j<S_x;j++){
			if(S[i][j]=='1'){
				c++;
				owp[i]+=wp[j]*wp_c[j]/(wp_c[j]-1.0);
			}else if(S[i][j]=='0'){
				c++;
				owp[i]+=(wp[j]*wp_c[j]-1.0)/(wp_c[j]-1.0);
			}
		}
		owp[i]/=c;

	}

	for(i=0;i<S_x;i++){
		c=0;
		oowp[i]=0.0;
		for(j=0;j<S_x;j++){
			if(S[i][j]!='.'){
				c++;
				oowp[i]+=owp[j];
			}
		}
		oowp[i]/=(double)c;
	}

	for(i=0;i<S_x;i++) cout<<wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25<<endl;
}

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		cout<<"Case #"<<i+1<<": \n";
		run();

	}
	return 0;
}

