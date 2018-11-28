#include<iostream>
#include<algorithm>

using namespace std;

int main(){
	int test, n, p;
	char r, flag;
	int po, pb, dif, aux;
	int passos;
	
	cin >> test;
	for(int t=1;t<=test;t++){
		cin >> n;
		
		passos=0;
		po = 1;
		pb = 1;
		
		cin >> r >> p;
		flag = r;
		dif = po - p;
		if(dif<0) dif=-dif;
		
		aux = dif+1;
		passos = dif+1;
		if(r == 'O') po = p;
		else pb = p;
		
		for(int i=1;i<n;i++){
			cin >> r >> p;
			
			if(flag == r){
				if(r=='O'){
					dif = po - p;
					po = p;
				}
				else{
					dif = pb - p;
					pb = p;
				}
				if(dif<0) dif=-dif;
				
				passos+=dif+1;
				aux+=dif+1;
			}
			else{
				if(r=='O'){
					dif = po - p;
					po = p;
				}
				else{
					dif = pb - p;
					pb = p;
				}
				if(dif<0) dif=-dif;
				
				if(dif > aux){
					passos+=(dif-aux)+1;
					aux = (dif-aux)+1;
				}
				else{
					passos++;
					aux = 1;
				}
				
				flag = r;
			}
			
			
		}
		cout << "Case #" << t << ": " << passos << "\n";
	}
	
	return 0;
}
