#include <iostream>
using namespace std;
int main(int argc, char *argv[]){
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		int n;
		cin>>n;
		int mask=0;
		int total=0;
		int minVal=-1;
		for(int i=0;i<n;++i){
			int x;
			cin>>x;
			total+=x;
			mask^=x;
			if((minVal<0) || (x<minVal)){
				minVal=x;
			}
		}
		int sol=(mask==0)?(total-minVal):0;
		if(sol>0){
			cout<<"Case #"<<c+1<<": "<<sol<<endl;
		}else{
			cout<<"Case #"<<c+1<<": NO"<<endl;
		}
	}
	return 0;
}
