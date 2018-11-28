#include <cstdio>
#include <cstring>
#include <cmath>


int T, mcase = 1;
char combine[256][4];
char oppset[256][4];
int com, opp, N;

bool iscom(char a, char b, char &c)
{
	for(int i=0; i<com; i++){
		if(a == combine[i][0] && b == combine[i][1] || a == combine[i][1] && b == combine[i][0]){
			c = combine[i][2];
			return true;
		}
	}
	return false;
}

bool isopp(char a, char b)
{
	for(int i=0; i<opp; i++){
		if(a == oppset[i][0] && b == oppset[i][1] || a == oppset[i][1] && b == oppset[i][0])
			return true;
	}

	return false;
}

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	char str[101];

	scanf("%d", &T);
	while(mcase <= T){
		scanf("%d", &com);
		for(int i=0; i<com; i++)
			scanf("%s", combine[i]);
		scanf("%d", &opp);
		for(int i=0; i<opp; i++)
			scanf("%s", oppset[i]);
		scanf("%d", &N);
		scanf("%s", str);

		for(int i=1; i<N; i++){
			char temp;
			if(com > 0 && iscom(str[i-1], str[i], temp)){
				str[i] = temp;
				str[i-1] = 0;
			}

			if(opp > 0){
				for(int j=0; j<i; j++){
					if(isopp(str[j], str[i])){
						for(int k=0; k<=i; k++)
							str[k] = 0;
						break;
					}
				}
			}
		}

		printf("Case #%d: [", mcase);
		int i=0;
		while (i < N && str[i] == 0)
			i ++;
		if(i < N)
			printf("%c", str[i]);
		for(i++; i<N; i++)
			if(str[i] != 0)
				printf(", %c", str[i]);
		printf("]\n");
		mcase ++;
	}
}