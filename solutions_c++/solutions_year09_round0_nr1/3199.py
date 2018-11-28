#include <stdio.h>
#include <string.h>
#include <math.h>

char s[10000][50];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int l,d,n;
	scanf("%d%d%d\n",&l,&d,&n);
	for (int i = 0 ; i<d ; i++){
		gets(s[i]);
	}
	int cnt = 0;
	char teks[10000];

	while (gets(teks)){
		printf("Case #%d: ",++cnt);
		int res = 0;
		int tekl = strlen(teks);
		for (int i = 0 ; i<d ; i++){
			int tekpos = 0;
			bool open = false,matched = false, bad = false;
			for (int j = 0 ;j<tekl ; j++){
				if (teks[j]=='('){
					open = true;
					matched = false;
				} else
					if (teks[j]==')'){
						open = false;
						if (!matched)
							bad = true;
					}
					else
					{
						if (open){
							if (!matched)
							if (teks[j]==s[i][tekpos]){
								tekpos++;
								matched = true;
							}
						} else
						{
							if (teks[j]!=s[i][tekpos]){
								bad = true;
							} else
								tekpos++;
						}
					}
						
			}
			if (!bad && tekpos==l) res++;
		}
		printf("%d\n",res);
	}
	return 0;
}