#include <iostream>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int n,s,p;
		cin>>n>>s>>p;
		int totales[n];
		int sorprendente=0;
		int maximo=0;
		if(p==0){
			for(int j=0;j<n;j++)
				cin>>totales[j];
			maximo=n;
		}
		else{
			for(int j=0;j<n;j++){
				cin>>totales[j];
				if((totales[j]-p) >= (p-1)*2)
					maximo++;
				else
					if((totales[j]-p) == (p-2)+(p-1) || (totales[j]-p) == (p-2)*2){
						if(sorprendente < s && totales[j]!=0){
							maximo++;
							sorprendente++;
						}
					}
			}
		}
		cout<<"Case #"<<i+1<<": "<<maximo<<endl;
	}	
	return 0;
}
