#include <fstream.h>
#include <string.h>

int L, D, n, k, RES;
char dic[5001][16], t[16][256], s[1024];

void go(int x){
	int i;
	for(i = 0; i < L; i++)
		if(!strchr(t[i], dic[x][i]))
			return;
	RES++;	
}

int main(){
	int i, j, ns, p;
	ifstream f("A-large.in");
	ofstream g("A-large.out");
	f >> L >> D >> n;
	for(i = 0; i < D; i++)
		f >> dic[i];
	for(i = 0; i < n; i++){
		f >> s;
		ns = strlen(s);
		k = 0;
		j = 0;
		while(j < ns){
			p = 0;
			if(s[j] == '('){
				j++;
				while(s[j] != ')')
					t[k][p++] = s[j++];
				j++;
			}
			else t[k][p++] = s[j++];
			t[k++][p] = 0;
		}
		
		RES = 0;
		for(j = 0; j < D; j++)
			go(j);	
		g << "Case #" << i+1 <<": " << RES << "\n";
	}
	f.close();
	g.close();
	return 0;
}
