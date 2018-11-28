#include<iostream>
#include<cstdlib>
#define F 1
#define err 0.0000001
using namespace std;

int r[1000];
int s[1000];
int px[1000],py[1000];
int cmp(const void *a,const void *b){
int aa=*(const int*)a;
int bb=*(const int*)b;
return (r[aa]<r[bb])-(r[aa]>r[bb]);
}
long long rand2(){
return (((long long)rand())<<31)+rand();
}
long long sqrll(long long x){
return x*x;
}
bool check(int j){
	for(int i=0;i<j;i++){
		long long d=sqrll(px[s[i]]-px[s[j]])+sqrll(py[s[i]]-py[s[j]]);
		if(d<F*F*sqrll(r[s[i]]+r[s[j]]))
			return false;
	}
	return true;
}
int main(){
	int t;
	cin>>t;
	srand(123452541);
	cout.setf(ios_base::fixed);
	cout.precision(1);
	for(int i=1;i<=t;i++){
		int n,w,l;
		cin>>n>>w>>l;
		for(int j=0;j<n;j++)
			cin>>r[j];
		for(int j=0;j<n;j++)
			s[j]=j;
		qsort(s,n,sizeof*s,cmp);
//for(int j=0;j<n;j++)
//cout<<s[j];
		for(int j=0;j<n;j++)
			do{
				px[s[j]]=rand2()%(w*F+1);
				py[s[j]]=rand2()%(l*F+1);
//cout<<px[s[j]]<<" "<<py[s[j]]<<endl;
			}while(!check(j));
		cout<<"Case #"<<i<<":";
		for(int j=0;j<n;j++)
			cout<<" "<<px[j]/(double)F+err<<" "<<py[j]/(double)F+err;
		cout<<endl;
	}
}


