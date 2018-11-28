#include <iostream>
#include <vector>
#include <string>

int main(int argc, char* argv[])
{
	int t, c, i;
	int N, K;
	int nStatus, comp;
	bool bOnOff;

	scanf("%d", &t);

	for(c = 0; c < t; c ++) {
		scanf("%d %d", &N, &K);

		nStatus = 0;
		bOnOff= false;

		for(i = 0; i < K; i ++)
			nStatus += 1;

		//comp = 1 << (N-1);

		i = N-1;

		while(i >= 0) {
			bOnOff = true;
			comp = 1 << i;

			if(comp & nStatus) {
				bOnOff = true;				
			}
			else {
				bOnOff = false;
				break;
			}
			i--;
		}

		if(bOnOff)
			printf("Case #%d: ON\n", c+1);
		else
			printf("Case #%d: OFF\n", c+1);
	}	
}