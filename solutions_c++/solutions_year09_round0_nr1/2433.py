#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cctype>
#include<cstdlib>
#include<cmath>

using namespace std;

//Variables globales


//Funciones


int main(){
	int L, D, N, i, j, k, l, n;
	vector<string> dic(6000);
	vector<string> pat(600);
	string tmp;
	bool flag;
	cin>>L>>D>>N;
	for(i=0; i<D; i++){
		cin>>dic[i];
	}
	flag=false;
	for(i=0; i<N; i++){
		cin>>tmp;
		//vector<string> toks;
		vector<vector<int> > toks;
		vector<int> t(30);
		flag=false;
		for(j=0; j<tmp.length(); j++){
			if(tmp[j]=='('){	//Entonces empieza un or, prendemos una bandera
				flag=true;
				//t="";
			}else if(tmp[j]==')'){
				flag=false;
				toks.push_back(t);
				for(k=0; k<30; k++)t[k]=0;
			}else{
				if(flag){	//Entonces estamos capturando un or
					t[tmp[j]-97]=1;
				}else{
					t[tmp[j]-97]=1;
					toks.push_back(t);
					t[tmp[j]-97]=0;
				}
			}
		}
		if(toks.size()!=L)cout<<"Case #"<<i+1<<": "<<"0"<<endl;
		else{	
			n=0;
			for(j=0; j<D; j++){	//Para cada palabra en el diccionario
				flag=true;
				for(k=0; k<L && flag; k++){	//Para cada letra de la palabra
					if(toks[k][dic[j][k]-97]==0)flag=false;
				}
				if(flag)n++;
			}
			cout<<"Case #"<<i+1<<": "<<n<<endl;
		}
	}
	return 0;
}
