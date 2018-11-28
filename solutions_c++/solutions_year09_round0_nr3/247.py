// Problem C, Google Code Jam 09'
// using DP
#include <cstdio>
#include <cstring>

// calculate the result for the string w
void calc(char* w, int num) {
	const char* s="welcome to code jam"; 
	int wlen = strlen(w), cnt[19][510]; // cnt[i][j] represents how many times s[0-i] appears in w[0-j];
	for(int i=0; i<19; i++) {
		if(!i) 
			cnt[i][i]= (s[0]==w[0]?1:0);
		else 
			cnt[i][i] = (s[i]==w[i]?cnt[i-1][i-1]:0);
		
		for(int j=i+1; j<wlen; j++) {
			if(!i) 
				cnt[i][j] = (cnt[i][j-1]+(s[i]==w[j]?1:0))%10000;
			else
				cnt[i][j] = (cnt[i][j-1]+(s[i]==w[j]?cnt[i-1][j-1]:0))%10000;
		}
	}
	printf("Case #%d: %04d\n", num, (wlen-1>=18?cnt[18][wlen-1]:0) );
}

int main (int argc, char * const argv[]) {
	int cases; char w[502]; 
    FILE *f = fopen("./C-large.in.txt", "r");
	fscanf(f, "%d", &cases); fgets(w, 502, f);
	
	for(int i=1; i<=cases; i++) {
		fgets(w, 502, f);
		calc(w, i);
	}
	
	fclose(f);
    return 0;
}
