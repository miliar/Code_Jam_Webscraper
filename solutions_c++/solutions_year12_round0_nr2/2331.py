#include<iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n;
		cin>>n;
		int s;
		cin>>s;
		int p;
		cin>>p;
		int count=0;
		int thresh;
		if(p==0||p==1) thresh=p-2;
		else thresh=3*p-4;
		for(int j=0;j<n;j++){
			int ti;
			cin>>ti;
			if(ti>thresh+1) count++;
			else if((p!=0&&p!=1)&&s>0&&(ti==thresh||ti==thresh+1)){
				count++;
				s--;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;	
}
