# include <iostream>
# include <algorithm>
#include <vector>
# include <fstream>
using namespace std;

int fixedpoints(vector<int> a){
	int count=0;
	int n=a.size();
	vector<int> b(n);
	for(int i=0;i<n;i++){b[i]=a[i];}
	sort(b.begin(),b.end());
	for(int i=0;i<n;i++){if(a[i]==b[i]){count++;}}
	return count;
}
	
int main(){
	int T;
	cin>>T;
	int n;
	fstream fout("output.txt");
	
	for(int i=1;i<=T;i++){
	cin>>n;
	vector<int> a(n);
	for(int j=0;j<n;j++){cin>>a[j];}
	fout<<"Case #"<<i<<": "<<(n-fixedpoints(a))<<endl;
	}
	fout.close();
	return 0;
}

	

