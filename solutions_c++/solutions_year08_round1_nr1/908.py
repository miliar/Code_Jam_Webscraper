#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(){
	ofstream out("results.txt");
	int T;
	cin>>T;
	int v1[8],v2[8];
	for(int i=0;i<T;i++){
		int n;
		cin>>n;
		for(int j=0;j<n;j++){
			cin>>v1[j];
		}
		for(int j=0;j<n;j++){
			cin>>v2[j];
		}
		sort(v2,v2+n);
		int res=0;
		for(int j=0;j<n;j++)
			res+=v1[j]*v2[j];
		
		int max=res;
		res=0;
		
		do{
			for(int j=0;j<n;j++)
				res+=v1[j]*v2[j];
			if(max>res)
				max=res;
			res=0;
		}while(next_permutation(v2,v2+n)!=0);
		out<<"Case #"<<i+1<<": "<<max<<endl;
	}
    system("pause");
    return 0;
}
