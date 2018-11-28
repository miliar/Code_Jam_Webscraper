#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> C;

int proc(){
	unsigned int xsum=0,sum=0,min=-1;
	for(int i=0;i<C.size();i++){
		xsum^=C[i];
		sum+=C[i];
		if(C[i]<min) min=C[i];
	}
	if(xsum!=0)
		return 0;
	else
		return sum-min;	
}

int main(){
	int T;
	string temp;
	cin>>T;

	for(int t=0;t<T;t++){
		int N,m,preal;
		cin>>N;
		C.clear();
		for(int c=0;c<N;c++){
			cin>>m;
			C.push_back(m);
		}
		cout<<"Case #"<<(t+1)<<": ";
		preal=proc();
		if(preal==0)
			cout<<"NO"<<endl;
		else
			cout<<preal<<endl;
	}
}
