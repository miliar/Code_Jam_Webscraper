#include <stdio.h>
#include <cstring>

char tstr[1024], str[5010][16];
bool can[5010], next[32];

int main(){
    int L, D, N, l, pos, cur, ret;

    scanf("%d%d%d", &L, &D, &N);
	gets(tstr);
	for(int i = 0;i < D;i++)
		gets(str[i]);
	for(int i = 0;i < N;i++){
		memset(can, true, sizeof(can));
		gets(tstr);
		l = strlen(tstr);
		pos = cur = 0;
		while(pos < L && cur < l){
			memset(next, false, sizeof(next));
			if(tstr[cur] == '(')
				while(tstr[++cur] != ')')
					next[tstr[cur] - 'a'] = true;
			else
				next[tstr[cur] - 'a'] = true;
			for(int j = 0;j < D;j++)
				if(can[j])
					if(!next[str[j][pos] - 'a'])
						can[j] = false;
			pos++;cur++;
		}
		ret = 0;
		for(int j = 0;j < D;j++)
			if(can[j])
				ret++;
		printf("Case #%d: %d\n", i + 1, ret);
	}
    return 0;
}

