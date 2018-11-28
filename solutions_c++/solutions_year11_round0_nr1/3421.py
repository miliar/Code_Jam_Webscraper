#include<iostream>
#include<cstdlib>
#include<fstream>
using namespace std;
int main(){
	ifstream cin("a.in");
	ofstream cout("a.out");
	int n,k=1,m;
	cin>>n;
	while(n--){
		cin>>m;
		int po=1,pb=1,to=0,tb=0;
		char t;
		int p;
		for(int i=0;i<m;i++){
			cin>>t>>p;
			if(t=='O'){
				to+=abs(p-po)+1;
				if(to<=tb)
					to+=(tb-to)+1;
				po=p;
			}
			else{
				tb+=abs(p-pb)+1;
				if(tb<=to)
					tb+=(to-tb)+1;
				pb=p;
			}
		}
		cout<<"Case #"<<k++<<": "<<max(to,tb)<<endl;
	}
	return 0;
}
