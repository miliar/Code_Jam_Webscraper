/*
*  Javier Segovia
*  0.016
*/
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair

int COMB[300][300];
string OPP[300];
int main(){
	int kases; cin>>kases;
	for (int k=1; k<=kases; k++) {
		for (int i=0; i<260; i++) {
			OPP[i]="";
			for (int j=0; j<260; j++) {
				COMB[i][j] = -1;
			}
		}
		int combine,composed;
		cin>>combine;
		char a,b,c;
		for (int i=0; i<combine; i++) {
			cin>>a>>b>>c;
			COMB[int(a)][int(b)] = int(c);
			COMB[int(b)][int(a)] = int(c);
		}
		cin>>composed;
		for (int i=0; i<composed; i++) {
			cin>>a>>b;
			OPP[int(a)].PB(b);
			OPP[int(b)].PB(a);
		}
		int val,len;
		cin>>len;
		size_t jt;
		string s="";
		
		for(int i=0;i<len;i++){
			cin>>c;
			if(s.LE == size_t(0) ){
				s.PB(c); 
				continue;
			}
			s.PB(c);
			val = COMB[int(s[int(s.LE)-1])][int(s[int(s.LE)-2])];
			if(val != -1){ //composed
				s.erase(int(s.LE) -1);
				s.erase(int(s.LE)-1);
				c = char(val);
				s.PB(c);
			}
			else if(OPP[int(c)].SL > 0){
				jt = s.find_first_of(OPP[int(c)]);
				if(jt != string::npos){//
					s ="";
				}
			}
		}
		cout<<"Case #"<<k<<": [";
		for (int i=0; i<int(s.LE); i++) {
			if(i)cout<<", ";
			cout<<s[i];
		}
		cout<<"]"<<endl;
	}
}