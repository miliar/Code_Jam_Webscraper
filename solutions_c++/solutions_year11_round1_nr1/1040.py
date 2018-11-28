#include <iostream>
using namespace std;



bool solveEachCase();

void main(){
	int caseNum;
	cin >> caseNum;
	for(int i = 0;i< caseNum;i++){
		cout << "Case #" <<(i+1) <<": ";
		if(solveEachCase())
			cout<<"Possible";
		else
			cout<<"Broken";
		if(i<caseNum-1)
			cout<<endl;
	}
}

bool solveEachCase(){
	int n, Pd, Pt;
	double lN;
	bool a, b;
	cin >> lN;
	cin >> Pd;
	cin >> Pt;

	if(lN >= 100){
		a = true;
	}else{
		n = (int) lN;
		a = false;
		for(int d = 1;d<=n;d++){
			for(int w = 0;w<=d;w++){
				if(w*100 == Pd*d){
					a = true;
					break;
				}
					
			}
			if(a==true)
				break;
		}
	}

	if((Pt==100&&Pd!=100)||(Pt==0&&Pd!=0)){
		b = false;
	}else{
		b = true;
	}

	return a&&b;
}