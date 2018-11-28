#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;


string tateti(vector<string> &v);

int main(int argc, char *argv[]) {
	
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
//	freopen ("a.in","r",stdin);
//	freopen ("a.out","w",stdout);
	
	int n,cont=1,cont_v=0;
	vector<string> v(4);
	string aux;
	
	cin>>n;
	while(cont<=n){
		cout<<"Case #"<<cont<<": ";
		for(int k = 0;k<4;k++){
			cin>>v[cont_v];
//			cout<<v[cont_v]<<endl;
			cont_v++;
		}
		cout<<tateti(v)<<endl;
		cont_v=0;
		cont++;
	}
	return 0;
}

char recorre_diago1(vector<string> &v){
	if(v[0][0]==v[1][1] && v[1][1]==v[2][2] && v[2][2]==v[3][3] && v[0][0]!='.')
		return v[0][0];
	return '.';
}
char recorre_diago2(vector<string> &v){
	if(v[0][3]==v[1][2] && v[1][2]==v[2][1] && v[2][1]==v[3][0] && v[0][3]!='.')
		return v[0][3];
	return '.';
}

char recorre_col(vector<string> &v){
	bool flag=true;
	for(int col=0;col<4;col++){
		for(int i = 1; i < 4; i++){
			if(v[i][col]==v[i-1][col] && (v[i][col])!='.')
				continue;
			else{
				flag=false;
				break;
			}
		}
		if(flag)
			return v[0][col];
		flag=true;
	}
	return '.';
}
char recorre_fila(vector<string> &v){
	bool flag=true;
	for(int j=0;j<4;j++){
		for(int col = 1; col < 4; col++){
			if(v[j][col]==v[j][col-1] && v[j][col]!='.'){
				continue;
			}
			else{
				flag=false;
				break;
			}
		}
		if(flag)
			return v[j][0];
		flag=true;
	}
	return '.';
}
vector<string> reemplaza_t(vector<string> &v,bool &punto){
	vector<string> v2(4,"....");
	for(int i = 0; i<4; i++){
		for(int j = 0; j<4; j++){
			if(v[i][j]=='T'){
				v[i][j] = 'X';
				v2[i][j] = 'O';
			}
			else{
				if(v[i][j]=='.')
					punto=true;
				v2[i][j] = v[i][j];
			}
		}
	}
	return v2;
}				
				
string tateti(vector<string> &v){
	bool punto = false;
	vector<string> vO = reemplaza_t(v,punto);
	char aux1=recorre_diago1(v),aux2=recorre_diago2(v),aux3=recorre_col(v),aux4=recorre_fila(v);
	char aux5=recorre_diago1(vO),aux6=recorre_diago2(vO),aux7=recorre_col(vO),aux8=recorre_fila(vO);
	string s(1,'.');
	if(aux1 != '.'){
		s[0]=aux1;
		s=s+" won";
		return s;
	}
	if(aux2 != '.'){
		s[0]=aux2;
		s=s+" won";
		return s;
	}
	if(aux3 != '.'){
		s[0]=aux3;
		s=s+" won";
		return s;
	}
	if(aux4 != '.'){
		s[0]=aux4;
		s=s+" won";
		return s;
	}
	if(aux5 != '.'){
		s[0]=aux5;
		s=s+" won";
		return s;
	}
	if(aux6 != '.'){
		s[0]=aux6;
		s=s+" won";
		return s;
	}
	if(aux7 != '.'){
		s[0]=aux7;
		s=s+" won";
		return s;
	}
	if(aux8 != '.'){
		s[0]=aux8;
		s=s+" won";
		return s;
	}
	if(punto)
		return "Game has not completed";
	return "Draw";
}
