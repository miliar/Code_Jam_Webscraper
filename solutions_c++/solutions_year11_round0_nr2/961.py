#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;



class comb {
	public:
		char a,b,c; // a and b will become c

};

class opp {
	public:
		char a,b; // a and b are opposed

};

string list;
string fin;
vector<comb> combs;
vector<opp> opps;
int T,c,d,n;
int fPos = 1;


int combinate(int pos) {

	//cout << "combinate(" << fin[pos] << ", " << fin[pos-1] << ");" << endl;

	for(int i = 0; i < c; i++) {
		
		if( (fin[pos] == combs[i].a && fin[pos-1] == combs[i].b) ||
			 (fin[pos] == combs[i].b && fin[pos-1] == combs[i].a) ) {
			//cout << "combining " << fin[pos]  << " and " << fin[pos-1]  << " into " << combs[i].c << endl;	 
		
			//spell.replace(pos,2,1,combs[i].c);
			fin.erase(pos-1,2);
			fin.insert(pos-1,1,combs[i].c);
			fPos--;
			//cout << spell.length();
			return 1;
		}
	
	}
	
	return 0;

}

int opposed(int pos) {

	for(int i = 0; i < pos; i++) {
	
		for(int j = 0; j < d; j++) {
		
			//cout << " Checking " << spell[i] << ", " << spell[pos] << endl;
		
			if( (fin[i] == opps[j].a && fin[pos] == opps[j].b) || 
			    (fin[i] == opps[j].b && fin[pos] == opps[j].a) ) {
			    
			    //cout << fin[i] << " and " << fin[pos] << " is oppsosed!! " << endl;
			    
			    fin = "";
			    fPos = -1;
			    return 1;
			 }
			
		}
	
	}
	
	return 0;
}


int main() {

	
	
	
	cin >> T;
	
	for(int x = 1; x <= T; x++) {
	
		combs.clear();
		opps.clear();
		list = "";
		fin  = "";
		fPos = 1;
	
		cin >> c;
		for(int i = 0; i < c; i++) {
			comb tmp;
			scanf("%*c");
			scanf("%c%c%c", &tmp.a, &tmp.b, &tmp.c);
			//cout << tmp.a << " : "<< tmp.b << " : "<< tmp.c << endl;
			combs.push_back ( tmp );
		}
		// ADD EXTRA SPACE SCaNF BLANK SPAce
	
		cin >> d;
		for(int i = 0; i < d; i++) {
		
			opp tmp;
			scanf("%*c");
			scanf("%c%c", &tmp.a, &tmp.b);
			//cout << tmp.a << " : "<< tmp.b << endl;
			opps.push_back ( tmp );
		}
	
		cin >> n >> list;

		
		
		
		fin.append(list,0,1);
		
		for(int i = 1; i < n; i++) {
			
			fin.append(list, i, 1);
			
			
			if(!combinate(fPos))
				opposed(fPos);
			
			//printf("(%d,%d) %c\t", fPos, i, fin[fPos-1]);
			//cout << fin << endl;
		
		
		
			fPos++;
		}
	
	
		cout << "Case #" << x << ": ";
		cout << "[";
		for(int i = 0; i < fPos; i++) {
			cout << fin[i];
			if(i+1 < fPos) cout << ", ";
	
		}
		cout << "]" << endl;
	}	
	

return 0;
}
