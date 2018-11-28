#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
#include<map>
#include<cstdlib>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<cstring>

using namespace std;

#define PB(x) push_back(x)
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define VVI (vector<vector<int> >) 
#define FOR(I,A,B) for(int I=A;I<B;I++)
#define FORA(I,A,B) for(int I=A;I>B;I--)
#define SORT(x) sort(x.begin(),x.end())

int main(){
	long long int a[10000];
	//int b[1000010];
	long long int n,t,l,c,l1,l2;
	long long int tt,tmp;
	long long int sum=0;
	cin>>tt;
	for(int k=1;k<=tt;k++){
		cin>>l>>t>>n>>c;
		for(int i=0;i<c;i++){
			cin>>a[i];
		}
		sum=0;
		l1=0;
		l2=0;
		if(l==0){
			for(int i=0;i<n;i++){
				sum+=a[i%c];
			}
			sum*=2;
		}else if(l==1){
			for(int i=0;i<n;i++){
				sum+=a[i%c];
				if(sum*2>t){
					if(l1==0){
						l1=((sum*2)-t)/2;
					}else if(a[i%c] > l1){
						l1=a[i%c];
					}
				}
			}
			sum*=2;
			sum-=l1;
		}else{
			for(int i=0;i<n;i++){
				sum+=a[i%c];
				if(sum*2>t){
					if(l2==0){
						l2=((sum*2)-t)/2;
					}else if(a[i%c] > l1){
						if(a[i%c]>l2){
							l1=l2;
							l2=a[i%c];
						}else{
							l1=a[i%c];
						}
					}
				}
			}
			sum*=2;
			sum-=l1;
			sum-=l2;
		}
		cout<<"Case #"<<k<<": "<<sum<<endl;
	}
	return 0;
}
