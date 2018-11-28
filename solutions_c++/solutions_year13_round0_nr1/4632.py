#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <sstream>
 
using namespace std;	

int main(){
	int kolko;
	string slovo;
	cin>>kolko;
	int por=0;
	while(kolko--){
		por++;
		vector<string > hra;
		string a;
		int b=4;
		while(b--) {cin>>a; hra.push_back(a);}
		bool vysledok=false;
		string odpoved;
		for(int i = 0; i< 4; i++){
			bool nasli=true;
			if((hra[i][0]!='.')&&(hra[i][1]!='.')){
				char hladame=hra[i][0];
				if (hladame=='T') hladame=hra[i][1];
				for(int j = 1; j< 4; j++){
					if((hra[i][j]!=hladame)&&(hra[i][j]!='T')){
						nasli=false;
						break;
					}
				}
				if(nasli){
					string p;
					p.resize(1);
					p[0]=hladame;
					odpoved+=p;
					odpoved+=" won";
					vysledok=true;
					break;
				}
			}
		}

		if(vysledok==false)
		for(int i = 0; i< 4; i++){
			bool nasli=true;
			if((hra[0][i]!='.')&&(hra[1][i]!='.')){
				char hladame=hra[0][i];
				if (hladame=='T') hladame=hra[1][i];
				for(int j = 1; j< 4; j++){
					if((hra[j][i]!=hladame)&&(hra[j][i]!='T')){
						nasli=false;
						break;
					}
				}
				if(nasli){
					string p;
					p.resize(1);
					p[0]=hladame;
					odpoved+=p;
					odpoved+=" won";
					vysledok=true;
					break;
				}
			}
		}

		if(vysledok==false){
			char hladame=hra[0][0];
			if((hra[0][0]!='.')&&(hra[1][1]!='.')){
			if(hladame=='T') hladame=hra[1][1];
			
			if(((hra[1][1]==hladame)||(hra[1][1]=='T'))	&& ((hra[2][2]==hladame)||(hra[2][2]=='T'))	&& ((hra[3][3]==hladame)||(hra[3][3]=='T'))	) {
					string p;
					p.resize(1);
					p[0]=hladame;
					odpoved+=p;
					odpoved+=" won";
					vysledok=true;			
			}
			}
		}
		if(vysledok==false){
			char hladame=hra[0][3];
			if((hra[0][3]!='.')&&(hra[1][2]!='.')){
			if(hladame=='T') hladame=hra[1][2];
			
			if(((hra[1][2]==hladame)||(hra[1][2]=='T'))	&& ((hra[2][1]==hladame)||(hra[2][1]=='T'))	&& ((hra[3][0]==hladame)||(hra[3][0]=='T'))	) {
					string p;
					p.resize(1);
					p[0]=hladame;
					odpoved+=p;
					odpoved+=" won";
					vysledok=true;			
			}
			}
		}
		if(vysledok==false){
			bool je=false;
			for(int i=0; i<4; i++){
				for(int j=0; j<4; j++){
					if(hra[i][j]=='.') {je=true; break;}
				}
				if (je) break;
			}
			if(je) {
				vysledok=true;
				odpoved="Game has not completed";
			}
			else {
				vysledok=false;
				odpoved="Draw";
			}
		}
		cout<<"Case #"<<por<<": "<<odpoved<<endl;
	}
}
// \n ||