#include <sstream>
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;


struct t{
	int a, b, c;
	t(int x, int y, int z){
		a=x, b=y, c=z;
	}
};

bool operator < (t a, t b){
	return a.a < b.a;
}

main(){
	int tx, z, na, nb;

	cin >> z;

	for(int j=0; j<z; j++){
		cin >> tx;	
		scanf("%d %d\n", &na, &nb);
		vector <t> V;

		for(int i=0; i<na+nb; i++){
			string S;
			getline(cin, S);
			S[2] = S[8] = ' ';
			stringstream SS;
			SS.str(S);
			int a, b, c, d;
			SS >> a >> b >> c >>d;
			
			V.push_back(t(60*a+b, 60*c+d, i < na));
		}

		sort(V.begin(), V.end());
		
		priority_queue<int> Q1, Q2;
		int res1 = 0, res2 = 0;


		for(int i=0; i<V.size(); i++){
			if(V[i].c == 0){
				if(!Q1.empty() && - Q1.top() <= V[i].a){
					Q1.pop();
				}
				else res2++;
				Q2.push( - V[i].b - tx);	
			}
			else{
				if(!Q2.empty() && - Q2.top() <= V[i].a){
					Q2.pop();
				}
				else res1++;
				Q1.push(- V[i].b - tx);	
			}
		}

		printf("Case #%d: %d %d\n", j+1, res1, res2);
		
	}	
}
