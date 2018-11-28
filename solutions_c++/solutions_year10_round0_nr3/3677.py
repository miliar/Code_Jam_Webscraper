#include<iostream>
#include<fstream>
using namespace std;
int f(int r,int k,int n,int *g);
void change(int n,int i,int *g);
void main()
{
	ifstream in("C-small-attempt0.in");
	if(!in){cout<<"文件无法打开！";exit(-1);}
	ofstream out("out.txt");
	if(!out){cout<<"文件无法创建！";exit(-1);}
	int R,K,N,T;
	int *g;
	in>>T;
	for(int i=1;i<=T;i++){
		in>>R>>K>>N;
		g=new int[N];
		for(int j=0;j<N;j++)in>>g[j];
		out<<"Case #"<<i<<": "<<f(R,K,N,g)<<endl;
		delete []g;
	}

}
int f(int r,int k,int n,int *g)
{
	int left,j;
	int sum=0;
	for(int i=1;i<=r;i++){
		j=0;left=k;
		while(left-g[j]>=0&&j<n){
			left-=g[j++];
		}
		sum+=k-left;
		change(n,j,g);
	}
	return sum;
}
void change(int n,int i,int *g)
{
	int *a=new int[i];
	for(int p=0;p<i;p++)a[p]=g[p];
	for(int p=i;p<n;p++)g[p-i]=g[p];
	for(int p=0;p<i;p++)g[n-i+p]=a[p];
	delete []a;
}