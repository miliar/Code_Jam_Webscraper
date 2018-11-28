#include <iostream>
#include <queue>
#include <list>
using namespace std;

void read();
int antal_test_cases;

struct test{

	list<int>ls_bla;
	list<int>ls_org;
	queue<bool> tur_knap;

};
int solve(test input);

test *test_c;


int main(){
	read();
	for (int i=0;i<antal_test_cases;i++){
		long res= solve(test_c[i]);
		printf("Case #%i: %ld\n",i+1,res);
	}
	return 0;
}


int solve(test input){

	int antal_knapper=input.tur_knap.size();

	list<int>::iterator ls_p_b= input.ls_bla.begin();
	list<int>::iterator ls_p_o = input.ls_org.begin();

	bool slut_org = false;
	bool slut_bla= false;

	int placering_bla=1;
	int placering_org=1;
	int bla_mod;
	if (ls_p_b!=input.ls_bla.end()){
		bla_mod =*ls_p_b; //p� vej imod
	}else
	{
		slut_bla= true;
	}

	int org_mod;
	if (ls_p_o!=input.ls_org.end()){
		org_mod =*ls_p_o; //p� vej imod
	}else
	{
		slut_org= true;
	}

	
	

	bool oragnges_tur = input.tur_knap.front();
	input.tur_knap.pop();
	int tid=0;

	bool klik =false;


	while(antal_knapper>0){
		tid++;




		//skal vi begv�ge bl� og orange, eller er de begge "f�rdige".
		if (!slut_org){ // bev�g organge
			// er vi p� dne placering vi vil v�re p�
			if (placering_org==org_mod){
				// kan vi tage den ?
				if (oragnges_tur){
					antal_knapper--;


					klik = true;
					// find n�ste knap osv.
					ls_p_o++;
					if (ls_p_o!=input.ls_org.end()){
						
						org_mod = *ls_p_o;
					}else{
						slut_org=true;
					}




				}
			}else{
				// vi er ikke fremme, g� imod.
				if (org_mod>placering_org){
					placering_org++;
				}else{
					placering_org--;
				}
			}

		}

		// bev�g bl�
		if (!slut_bla){ 
				if (placering_bla==bla_mod){
				// kan vi tage den ?
				if (!oragnges_tur){
					antal_knapper--;

					// find n�ste knap osv.
					

					klik = true;
					ls_p_b++;
					if (ls_p_b!=input.ls_bla.end()){
						
						bla_mod = *ls_p_b;
					}else{
						slut_bla=true;
					}




				}
			}else{
				// vi er ikke fremme, g� imod.
				if (bla_mod>placering_bla){
					placering_bla++;
				}else{
					placering_bla--;
				}
			}

		}


		if (klik&&antal_knapper>0){
				oragnges_tur = input.tur_knap.front();
				input.tur_knap.pop();
				klik= false;
		}





	}

	return tid;


}




void read(){
	cin>> antal_test_cases;
	test_c = new test[antal_test_cases];
	for (int i=0;i<antal_test_cases;i++){
		int knapper=0;
		cin>>knapper;
		for (int y=0;y<knapper;y++){
			
			char temp;
			int tal;
			cin >> temp;
			cin >> tal;
			if (temp=='O'){
				//orange
				test_c[i].ls_org.push_back(tal);
				test_c[i].tur_knap.push(true);
				
			}else{
				//bl�
				test_c[i].ls_bla.push_back(tal);

				test_c[i].tur_knap.push(false);
			}
		
		}
		
	
	}


}