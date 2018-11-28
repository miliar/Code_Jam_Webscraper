#include <iostream>
#include <map>

using namespace std;

int main(){
	//printf("ok");
	int S,Q,N,X=0,Y;
	cin >> N;
	for(int i=0;i<N;i++){
		map<string,int> usado;
		string sArr[300];
		char auxA[101];
		string aux;
		cin >> S;
		//cout << S << endl;
		int sUsado=0;
		gets(auxA);
		for(int j=0;j<S;j++){
			gets(auxA);
			aux = auxA;
			usado[aux]=3;
			sArr[j]=aux;
			//cout << aux << endl;
		}
		Y=0;
		cin >> Q;
		//cout << Q << endl;
		gets(auxA);
		for(int j=0;j<Q;j++){
			gets(auxA);
			aux = auxA;
			//cout << aux << "=" << usado[aux] << endl;
			if(usado[aux]==3){
				usado[aux]=1;
				//cout << "marca " << aux <<"\n";
				sUsado++;
				if(sUsado==S){
					for(int k=0;k<S;k++){
						usado[sArr[k]]=3;
					}
					usado[aux]=1;
					Y++;
					sUsado=1;
					//cout << "troca " << j <<" "<< aux <<endl;
				}
			}
		}
		X++;
		cout << "Case #" << X << ": " << Y << endl;
	}
	
	//string a="ok";
	//cout << a;
	return 0;
}
