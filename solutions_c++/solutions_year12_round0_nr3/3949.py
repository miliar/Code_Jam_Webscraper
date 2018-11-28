#include<iostream>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

set<int> data[2000000];

int main(){
	int T;
	
	
	for(int i=1;i<2000000;i++){
		int k=10;for(;k<i;k*=10);k/=10;
		
		for(int j=10;j<i;j*=10){
			int d=(i%j)*k+i/j;
			if(i<d&&d<=2000000)
				data[i].insert(d);
			k/=10;
		}
	}
	
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		int A,B;
		cin>>A>>B;
		int result=0;
		for(int i=A;i<B;i++){
	
			for(set<int>::iterator it=data[i].begin();it!=data[i].end();it++)
				if(*it<=B)
					result++;
			
			
		}
		cout<<"Case #"<<tc<<": "<<result<<endl;
	}
	return 0;
}
