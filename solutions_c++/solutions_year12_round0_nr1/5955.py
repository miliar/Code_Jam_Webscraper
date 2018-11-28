#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	char codigo[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	cin>>t;
	cin.ignore();
	for (int i=0;i<t;i++){
		string linea;
		(getline(cin, linea));
			cout<<"Case #"<<i+1<<": ";
			for(int j=0; j<linea.size();j++){
				if(linea[j]==' '){
					cout<<" ";
				}
				else{
					cout<<codigo[(int)linea[j]-97];
				}
			}
			cout<<endl;
		}
	return 0;
}

