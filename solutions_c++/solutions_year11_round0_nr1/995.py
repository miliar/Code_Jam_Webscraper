#include <iostream>

#define O 0
#define B 1

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	
	int but, test, t=1, n, cont, res, aux;
	int po, pb;
	char r, flag;
	
	cin >> test;
	while (test--){
		cin >> n;
		cont = 0;
		res = 0;
		po = 1;
		pb = 1;
		
		cin >> r >> but;
		flag = r;
		cont += (but - po)+1;
		res += cont;
		
		if (r == 'O') po = but;
		else pb = but;
		
		//cout << "DBG: r: " << r << " but: " << but << " cont: " << cont << " po: " << po << " pb: " << pb << " res: " << res << endl;
		
		for (int i=1; i<n; i++){
			cin >> r >> but;
			
			if (flag == r) {
				if (r == 'O') aux = (but - po);
				else aux = (but - pb);
				if (aux < 0) aux *= -1;
				
				res += aux+1;
				cont += aux+1;
			}
			else {
				if (r == 'O') aux = (but - po);
				else aux = (but - pb);
				if (aux < 0) aux *= -1;
				
				if (cont < aux){
					res += (aux - cont)+1;
					cont = (aux - cont)+1;
				}
				else{
					cont = 1;
					res++;
				}
				flag = r;
			}
			if (r == 'O') po = but;
			else pb = but;
			
			//cout << "DBG: r: " << r << " aux: " << aux << " but: " << but << " cont: " << cont << " po: " << po << " pb: " << pb << " res: " << res << endl;
		}
		
		cout << "Case #" << t++ << ": " << res << "\n";
	}
	return 0;
}