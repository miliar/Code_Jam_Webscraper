#include <iostream>
using namespace std;

void swap(int &a,int&b)
{
	int temp=a;
	a=b;
	b=temp;
}
void perm(int src[],int &min,int list[],int k,int m){
	if(k==m){
		int temp=0;
		for(int i=0;i<=m;i++){
		//	cout<<list[i];
			temp+=src[i]*list[i];
		}
		if(min>temp)min=temp;
	//	cout<<endl;
	}
	for(int i=k;i<=m;i++){
		swap(list[k],list[i]);
		perm(src,min,list,k+1,m);
		swap(list[k],list[i]);
	}
}
void main()
{
	int cases,num,i,k;
	int *a,*b;
	cin>>cases;
	for(k=0;k<cases;++k){
		cin>>num;
		a=new int[num];
		b=new int[num];
		for(i=0;i<num;++i){
			cin>>a[i];
		}
		int min=0;
		for(i=0;i<num;++i){
			cin>>b[i];
			min+=a[i]*b[i];
		}
		perm(a,min,b,0,num-1);
		cout<<"Case #"<<k+1<<": "<<min<<endl;
		delete[] a;
		delete[] b;
	}
}