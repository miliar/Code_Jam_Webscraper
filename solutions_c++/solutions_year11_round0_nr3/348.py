#include<iostream>
using namespace std;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int Test;
	cin>>Test;
	for (int test=1;test<=Test;test++){
		int n;
		cin>>n;
		int sum=0,check=0;
		int min=10000000;
		int tmp;
		for (int i=0;i<n;i++){
			cin>>tmp;
			check^=tmp;
			sum+=tmp;
			if (tmp<min)
				min=tmp;
		}
		if (check==0)
			cout<<"Case #"<<test<<": "<<sum-min<<endl;
		else
			cout<<"Case #"<<test<<": NO"<<endl;
	}
}
