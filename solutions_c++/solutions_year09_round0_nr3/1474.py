#include <cstdio>
#include <cstring>

using namespace std;

int N;

int t1, t2;

const char* txt1 = "welcome to code jam";
char buffer[1024];

int res[512][512];

int get_res(int j, int k) {		
	int s = 0;

	if ((j<t1) && (k<t2)) {	
		if (res[j][k]>=0)
			return res[j][k];
	
		if (txt1[j]==buffer[k]) {
			if ((j+1)==t1)
				s+=1;
			else
				s+=get_res(j+1, k+1);
		}
	
		s+=get_res(j, k+1);
		
		res[j][k] = s;
	}
	
	return s % 10000;
}

int main() {
	scanf("%d\n", &N);
	t1 = strlen(txt1);		
	for(int i=0; i<N; i++) {
		
		fgets (buffer , 1024 , stdin);	
		t2 = strlen(buffer);
		
		for(int j=0; j<t1; j++) 
			for (int k=0; k<t2; k++)
				res[j][k] = -1;
				
		printf("Case #%d: %04d\n", (i+1), get_res(0, 0));
	}
	return 0;
}



