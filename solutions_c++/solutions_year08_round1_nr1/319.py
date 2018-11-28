#include<iostream>
#include<stdlib.h>
using namespace std;

int sx(const void *a,const void *b){
	long *aa,*bb;
	aa=(long *)a;
	bb=(long *)b;
	return (*aa>*bb)?1:-1;
}

int sy(const void *a,const void *b){
	long *aa,*bb;
	aa=(long *)a;
	bb=(long *)b;
	return (*aa<*bb)?1:-1;
}

main(int argc, char **argv){
	int T,n;
	long x[800],y[800];
	cin>> T;
	for(int t=0;t<T;t++){
		long s=0;
		cin>>n;
		for(int i=0;i<n;i++) cin>>x[i];
		for(int i=0;i<n;i++) cin>>y[i];
		qsort((void *)x,n,sizeof(long),sx);
		qsort((void *)y,n,sizeof(long),sy);
		//for(int i=0;i<n;i++) cout << x[i]<<' ';
		//cout << endl;
		//for(int i=0;i<n;i++) cout << y[i]<<' ';
		//cout << endl;
		for(int i=0;i<n;i++) s+=x[i]*y[i];
		cout<<"Case #"<<t+1<<": "<<s<<endl;
	}
}	
