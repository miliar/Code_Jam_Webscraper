#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
		ios_base :: sync_with_stdio();
		
		int cc;
		cin >> cc;			
		
		for(int i=0;i<cc;i++){
			
			char kto[100];
			
			int b[100],bb=0,bbb=0;
			int o[100],oo=0,ooo=0;
			
			int rr;
			
			int b_poz = 1;
			int o_poz = 1;
			
			int time = 0;
			
			cin >> rr;
			
			for(int j=0;j<rr;j++){
				cin >> kto[j];
				if(kto[j] == 'B') {cin >> b[bb++];}
				else {cin >> o[oo++];}
			}			
			
			int z = 0;
			while(z != rr){
				if(kto[z] == 'B') {
					if(b[bbb] != b_poz) {
						if(b[bbb] > b_poz) {b_poz++;}
						else {b_poz--;}
					}
					else if(b[bbb] == b_poz) {
						bbb++;
						z++;
					}
					
					int n_p = z;
					while(n_p != rr){
						if(kto[n_p] == 'O') {break;}
						n_p++;
					} 
					if(n_p <= rr){					
						if(o[ooo] != o_poz) {
							if(o[ooo] > o_poz) {o_poz++;}
							else {o_poz--;}
						}
					}
				}
				//-----O------------------------------------------------
				else if(kto[z] == 'O') {
					if(o[ooo] != o_poz) {
						if(o[ooo] > o_poz) {o_poz++;}
						else {o_poz--;}
					}
					else if(o[ooo] == o_poz) {
						ooo++;
						z++;
					}										
					int n_p = z;
					while(n_p != rr){
						if(kto[n_p] == 'B') {break;}
						n_p++;
					} 	
					if(n_p <= rr){				
						if(b[bbb] != b_poz) {
							if(b[bbb] > b_poz) {b_poz++;}
							else {b_poz--;}
						}
					}
				}			
				time++;
			}			
			cout <<"Case #"<<i+1<<": "<<time<<endl;
		}			
		return 0;
}
