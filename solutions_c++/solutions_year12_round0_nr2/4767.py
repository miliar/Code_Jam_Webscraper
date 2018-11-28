#include <iostream>
#include <cstdio>
using namespace std;
bool is_surp(int num,int beat){
	if(num<28){

		if(num%3==0 and num/3+1>=beat)
			return true;
		
		if(num%2!=0 and (num+1)%3==0 and (num+4)/3>=beat)
			return true;
		if(num%2==0 and num/3+1>=beat and (num-1)%3==0)
			return true;
		if(num%2==0 and num/3+2>=beat and (num-1)%3!=0)
			return true;
		return false;
	}
	return false;
}

int main(int argc, char *argv[]) {
	freopen( "input_s.txt", "r", stdin );
	freopen( "output_s.txt", "w", stdout );
	int casos,surp,googlers,p,cont;
	cin>>casos;
	//if(is_surp(14,6))cout<<"caca";
	for(int i=0;i<casos;i++){
		cont=0;
		cin>>googlers>>surp>>p;
		for(int x=0;x<googlers;x++){
			int aux;
			cin>>aux;
			if(aux%3!=0 and aux/3+1>=p)
				cont++;
			else if(aux%3==0 and aux/3>=p)
				cont++;
			else if(surp>0 and is_surp(aux,p) and aux!=0){
				cont++;
				surp--;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		cout<<cont<<"\n";
	}
	return 0;
}

