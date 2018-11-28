#include <iostream>
#include <string>
using namespace std;

int main(){
	int cases;
	cin >> cases;
	
	for(int T=1;T<=cases;T++){
		
		int combo_num;
		cin >> combo_num;

		string combo[combo_num];
		for(int i=0;i<combo_num;i++){
			cin >> combo[i];
		}




		int oppo_num;
		cin >> oppo_num;

		string oppo[oppo_num];
		for(int i=0;i<oppo_num;i++){
			cin >> oppo[i];
		}

		int input_len;
		cin >> input_len;

		string list="";
		char c;
		for(int i=0;i<input_len;i++){
			cin >> c;
			//cout << c;
			bool is_combo = false;


			int len = list.length();
			if(len>0){
				for(int j=0;j<combo_num;j++){
					
					if(	(c==combo[j][0] && list[len-1]==combo[j][1]) ||
					 	(c==combo[j][1] && list[len-1]==combo[j][0])){
						list[len-1] = combo[j][2];
						is_combo = true;

						//cout << "combo" << endl;

						break;
					}
				}
			}
			bool is_oppo = false;

			if(!is_combo){
				int len = list.length();
				if(len>0){
					for(int j=0;j<oppo_num;j++){
						for(int k=0;k<len;k++){
							if(	(list[k]==oppo[j][0] && c==oppo[j][1]) ||
								(list[k]==oppo[j][1] && c==oppo[j][0])){
									list="";
									is_oppo = true;

									//cout << "oppo" << endl;

									break;
							}
						}	
					}
				}
				if(!is_oppo){
					list = list + c;
				}
			}


		}
		string out;
		if(list.length()>0){
			out = "[";
		
			for(int i=0;i<list.length()-1;i++){
				out = out +list[i]+", ";
			}
			out = out + list[list.length()-1]+"]";
		}
		else{
			out="[]";
		}
		cout << "Case #" << T << ": " << out << endl;
		//cout << endl;
	}
	

	
	return 1;
}

// Input 
//  	
// Output 
//  
// 5
// 0 0 2 EA
// 1 QRI 0 4 RRQR
// 1 QFT 1 QF 7 FAQFDFQ
// 1 EEZ 1 QE 7 QEEEERA
// 0 1 QW 2 QW
// Case #1: [E, A]
// Case #2: [R, I, R]
// Case #3: [F, D, T]
// Case #4: [Z, E, R, A]
// Case #5: []