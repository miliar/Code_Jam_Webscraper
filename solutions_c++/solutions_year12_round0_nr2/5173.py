#include<iostream>
using namespace std;
int a[100][100];
int re[100]={0};
int ou;
void count()
{
	for(int i=0; i<ou; ++i)
	{
		int est = 3*(a[i][2]-1);
		int rest = a[i][1];
		for(int j=0;j<a[i][0];++j){
			
			if(a[i][j+3]>est)
				++re[i];
			else if(rest>0){
				if(a[i][j+3]>=3*a[i][2]-4&&a[i][j+3]>1){
					++re[i];
					--rest;
				}
			}
		
		}
	}
}
int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
	int num;
	int n;
	
	int sur;
	int best;
	cin>>ou;
	for(int j=0;j<ou;++j){
	cin>>n;
	a[j][0]=n;
	cin>>sur;
	a[j][1]=sur;
	cin>>best;
	a[j][2]=best;
	for(int i=0; i<n;++i){
		cin>>num;
		a[j][i+3]=num;
	}
	}
	count();
	for(int i=0; i<ou; ++i)
		cout<<"Case #"<<i+1<<": "<<re[i]<<endl;
	return 0;
}