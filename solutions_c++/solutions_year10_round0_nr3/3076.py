#include <cstdlib>
#include <iostream>
#include <string>
#include <queue>

using namespace std;


int roller(long times, long k, long groups[], long size){
	queue<long> fila;
	queue<long> fila2;

	long auxK;
	long goBack;
	long money=0;
	for(int i=0; i<size; i++){
		fila.push(groups[i]);
	}

	while(times !=0 ){
	 auxK = k;
		while(1){
			//fprintf(stdout,"%i fila", fila.empty());
			if(!fila.empty()){
				//fprintf(stdout, "auxK %i, fila %i \n", auxK, fila.front());
				if(auxK >= fila.front()){
					auxK -= fila.front();
					goBack = fila.front();
					fila.pop();
					fila2.push(goBack);
				}else{
					money += (k - auxK);
					while(!fila2.empty()){
						fila.push(fila2.front());
						fila2.pop();
					}
					break;
				}
			}else{
				money += (k - auxK);
				while(!fila2.empty()){
				fila.push(fila2.front());
				fila2.pop();
				}
				break;
			}

		}
			//fprintf(stdout,"auxk %i times %i money %i\n",auxK, times, money);
		times--;
	}

return money;

}


int main(int argc, char *argv[]){

	long cases, times, k, groups, counter;
	long money;
	counter = 1;
	cin >> cases;

	while(cases !=0){
		cin >> times;
		cin >> k;
		cin >> groups;
		long gr[groups];
		int i = 0;
		long kaka = groups;
		while(groups !=0){
			cin >> gr[i];
			groups--;
			i++;
		}
		money = roller(times, k, gr, kaka);
		fprintf(stdout,"Case #%i: %i\n", counter, money);
		cases--;
		counter++;
	}

}

