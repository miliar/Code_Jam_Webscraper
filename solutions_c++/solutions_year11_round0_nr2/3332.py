#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;
typedef long long i64;
char combine[40][5];
char oppose[40][5];
int c, d;
char isOppose(char a, vector<char> tmp){
	if(tmp.size()==0)
		return 'a';
	for(int i=0; i<tmp.size(); i++){
		for(int j=0; j<d; j++){
			if(tmp[i]==oppose[j][0] && a==oppose[j][1])
				return tmp[i];
			if(tmp[i]==oppose[j][1] && a==oppose[j][0])
				return tmp[i];
		}
	}
	return 'a';
}
char isCombine(char a, char b){
	for(int i=0; i<c; i++){
		if((a==combine[i][0] && b==combine[i][1])||(a==combine[i][1] && b==combine[i][0]))
			return combine[i][2];
	}
	return 'a';
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, cas=0;
	scanf("%d", &T);

	char input[110];
	vector<char> str;
	while(T--){
		cas++;
		memset(combine, 0, sizeof(combine));
		memset(oppose, 0, sizeof(oppose));
		memset(input, 0, sizeof(input));
		str.clear();
		int n;
		scanf("%d", &c);
		for(int i=0; i<c; i++)
			scanf("%s", combine[i]);
		scanf("%d", &d);
		for(int i=0; i<d; i++)
			scanf("%s", oppose[i]);
		scanf("%d", &n);
		scanf("%s", input);
		for(int i=0; i<n; i++){
			if(i>=1 && str.size()>0){
				char re = isCombine(str[str.size()-1], input[i]);
			//	printf("combine %c\n", re);
				if(re!='a'){
					str.pop_back();
					str.push_back(re);
				}
				else{
					re = isOppose(input[i], str);
			/*		for(int k=0; k<str.size(); k++)
						printf("%c", str[k]);
					printf(" %c ", input[i]);
					printf("oppose %c\n", re);
				*/
					if(re!='a'){
						str.clear();
					}
					else
						str.push_back(input[i]);
				}
			}
			else{
				str.push_back(input[i]);	
			}
		}
		printf("Case #%d: [", cas);
		if(str.size()>0){
			for(int i=0; i<str.size()-1; i++){
				printf("%c, ", str[i]);
			}
		}
		if(str.size()>0)
			printf("%c", str[str.size()-1]);
		printf("]\n");

	}
//	while(1);
	return 0;
}