// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;

int main()
{
	int tests;
	int actions;
	char hallway[100];
	int button[100];
	int moves;
	int opos;
	int bpos;
	int completedactions;
	int ocounter;
	int bcounter;
	int nexto;
	int nextb;
	bool gonext = false;

	cin >> tests;
	for(int i = 1; i<=tests; i++){
		completedactions = 0;
		moves = 0;
		opos = 1;
		bpos = 1;
		ocounter = 0;
		bcounter = 0;
		nexto=0;
		nextb=0;

		cin >> actions;
		for(int j=0; j<actions; j++){
			cin >> hallway[j];
			cin >> button[j];
		}
		moves = 0;
		while(completedactions<actions){
			gonext=false;
			if (nexto==0){
				while(ocounter < actions && hallway[ocounter]!='O'){
					ocounter++;
				}
				if(ocounter < actions)
					nexto=button[ocounter];
			}
			if (nextb==0){
				while(bcounter < actions && hallway[bcounter]!='B'){
					bcounter++;
				}
				if(bcounter < actions)
					nextb=button[bcounter];
			}
			if(nexto==opos){
				if(hallway[completedactions] == 'O'){
					ocounter++;
					gonext=true;
					nexto=0;
				}
			}
			else if (nexto<opos){
				opos--;
			}
			else{
				opos++;
			}
			if(nextb==bpos){
				if(hallway[completedactions] == 'B'){
					bcounter++;
					gonext=true;
					nextb=0;
				}
			}
			else if (nextb<bpos){
				bpos--;
			}
			else{
				bpos++;
			}

			if(gonext==true)
				completedactions++;
			moves++;
		}

		cout << "Case #" << i << ": " << moves << "\n";
	}
	return 0;
}

