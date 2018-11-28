#include<cstdio>
#include<string>
#include<iostream>

using namespace std;

char rule1[27][27];
bool rule2[27][27];

int getVal(char C) {
	return C - 'A';
}

void initMatrix(){
	int i,j;
	for (i = 0; i < 27; i++) {
		for (j = 0; j < 27; j++){
			rule1[i][j] = '\0';
			rule2[i][j] = false;
		}
	}
}

void addRule1(string rule) {
	int c1 = getVal(rule[0]);
	int c2 = getVal(rule[1]);
	char r = rule[2];
	rule1[c1][c2] = r;
	rule1[c2][c1] = r;
}

void addRule2(string rule) {
	int c1 = getVal(rule[0]);
	int c2 = getVal(rule[1]);	
	rule2[c1][c2] = true;
	rule2[c2][c1] = true;	
}

string getSolution(string sir) {
	int i;

	string result;
	result.clear();
	int lastPoz = 0;
	result.push_back(sir[0]);
	int prevC = getVal(sir[0]);
	int j;
	for (i = 1; i < sir.length(); i++) {		
		int curC = getVal(sir[i]);

		if (rule1[prevC][curC] != '\0'){ 
			result[lastPoz] = rule1[prevC][curC];
			prevC = getVal(result[lastPoz]);
		}
		else {
			bool del = false;
			for (j = 0; (j <= lastPoz) && (!del); j++) {
				if (rule2[curC][getVal(result[j])]){ 
					del = true;
				}
			}
			if (del){ 
				result.clear();
				lastPoz = -1;
				prevC = 27;
			}
			else {
				lastPoz++;
				result.push_back(sir[i]);
				prevC = curC;
			}
		}
	}
	
	string out;	
	if (result.size() > 0) {
		for (i = 0; i < result.size(); i++){
			out.push_back(' ');
			out.push_back(result[i]);
			out.push_back(',');
		}
		out[0] = '[';
		out[out.size() - 1] = ']';
	}
	else{
		out.push_back('[');
		out.push_back(']');
	}
	return out;
}

int main() {
	int i, T;
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	scanf("%d\n", &T);
	
	for (i = 0; i < T; i++) {		
		string r1, r2, sir;
		int nr1, nr2, j;
		initMatrix();
		
		scanf ("%d", &nr1);
		for (j = 0;j < nr1; j++) {
			cin>>r1;
			addRule1(r1);			
		}

		scanf ("%d", &nr2);
		for (j = 0;j < nr2; j++) {
			cin>>r2;
			addRule2(r2);
		}

		int l;
		cin>>l>>sir;		
		
		printf("Case #%d: ",i+1);
		cout<<getSolution(sir)<<"\n";
		
	}

	return 0;
}