#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	cin>>t;
	for (int i=0; i<t; i++){
		int n, pd, pg, g, d;
		cin>>n;
		cin>>pd;
		cin>>pg;
		bool salida=0;
		if (((pg==100)&&(pd!=100))||((pg==0)&&(pd!=0)))
			cout<<"Case #"<<i+1<<": Broken"<<endl;
		else{
			for (int j=1; j<n+1;j++){
				float pdf=pd*j/100.0;
				float pdf2=pd*j/100;
				if ((pdf)==(pdf2)){
					cout<<"Case #"<<i+1<<": Possible"<<endl;
					salida=1;
					break;}
			}
			if(!salida)
				cout<<"Case #"<<i+1<<": Broken"<<endl;
		}
	}
	return 0;
}

