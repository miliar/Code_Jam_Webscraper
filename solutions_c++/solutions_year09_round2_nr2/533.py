#include<cstdio>
#include<string>

using namespace std;

string Str;
char Buff[30];

int main() {
	freopen("BLL.in","r",stdin);
	freopen("BLL.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t = 0 ; t < T ; t++) {
		scanf("%s",Buff);
		Str = string(Buff);
		bool Sign = true;
		for(int i = Str.length() - 2 ; i >= 0; i--) {
			if (Str[i + 1] > Str[i]) {
				for(int j = Str.length() - 1; j > i ; j--) {
					if (Str[j] > Str[i]) {
						char Temp = Str[i];
						Str[i] = Str[j];
						Str[j] = Temp;
					//	printf("%s\n",Str.c_str());
						sort(&Str[i + 1],&Str[Str.length()]);
						Sign = false;
						break;
					}
				}
				break;
			}
		}
		
		if (Sign) {
			Str = Str + '0';
			sort(&Str[0],&Str[Str.length()]);
			for(int i = 0 ; i < Str.length() ; i++) {
				if (Str[i] != '0') {
					Str[0] = Str[i];
					Str[i] = '0';
					break;
				}
			}
		}
		
		printf("Case #%d: %s\n",t + 1,Str.c_str());
	}
//	while (1);
	return 0;
}

