#include <fstream.h>
#include <string.h>

char s[512], w[] = "welcome to code jam";
int a[512][32];

int main(){
	int i, j, n, k=1;
	ifstream f("c-large.in");
	ofstream g("C-large.out");
	int T;
	f >> T;
	f.get();
	while(T--){
		f.getline(s, 512);
		n = strlen(s);
		for(i = 0; i < 512; i++)
			for(j = 0; j < 32; j++)
				a[i][j] = 0;
		if(s[0]==w[0]) a[0][0] = 1;
		else a[0][0] = 0;
		for(i = 1; i < n; i++)
			if(w[0] == s[i])
				a[i][0] = 1 + a[i-1][0];
			else a[i][0] = a[i-1][0];
		for(i = 1; i < n; i++)
			for(j = 1; j <= 18 && j <= i; j++)
				if(w[j] == s[i])
					a[i][j] = (a[i-1][j] + a[i][j-1])%10000;
				else a[i][j] = a[i-1][j];
		g << "Case #" << k++ << ": ";
		if(a[n-1][18] < 10) g << "000";
		else if(a[n-1][18] < 100) g << "00";
		else if(a[n-1][18] < 1000) g << "0";
		g << a[n-1][18] << "\n";
	}
	f.close();
	g.close();
	return 0;
}
