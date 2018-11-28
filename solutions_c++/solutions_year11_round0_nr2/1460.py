#include <stdio.h>

//Q, W, E, R, A, S, D, F
char combine[26][26];
bool oppose[26][26];
short has_element[26];
short tail;
char res[128];

void reset_has_element(){
	int i;
	for(i=0;i<26;i++)
		has_element[i] = 0;
}
void printlist(){
	int i;
	printf("[");
	for(i=0;i<=tail;i++){
		printf("%c", res[i]);
		if(i<tail)
			printf(", ");
	}
	printf("]\n");
}
void solve(){
	int i, j, c, d, n;
	bool has_oppose;
	char str[128];
	for(i=0;i<26;i++){
		has_element[i] = 0;
		for(j=0;j<26;j++){
			combine[i][j] = 0;
			oppose[i][j] = false;
		}
	}

	scanf("%d", &c);
	for(i=0;i<c;i++){
		scanf("%s", str);
		combine[str[0]-'A'][str[1]-'A'] = str[2];
		combine[str[1]-'A'][str[0]-'A'] = str[2];
	}
	scanf("%d", &d);
	for(i=0;i<d;i++){
		scanf("%s", str);
		oppose[str[0]-'A'][str[1]-'A'] = true;
		oppose[str[1]-'A'][str[0]-'A'] = true;
	}
	scanf("%d", &n);
	scanf("%s", str);

	tail = 0;
	res[tail] = str[0];
	has_element[res[tail]-'A']++;
	for(i=1;i<n;i++){
//		printlist();

		/** Combine **/
		if(tail >= 0 && combine[res[tail]-'A'][str[i]-'A'] != 0){
//			printf("combine: %c+%c = %c\n", res[tail], str[i], combine[res[tail]-'A'][str[i]-'A']);
			has_element[res[tail]-'A']--;
			res[tail] = combine[res[tail]-'A'][str[i]-'A'];
			has_element[res[tail]-'A']++;
			continue;
		}

		/** Oppose **/
		has_oppose = false;
		for(j=0;j<26;j++){
			if(has_element[j] > 0 && oppose[j][str[i]-'A']){
				has_oppose = true;
				break;
			}
		}
		if(has_oppose){
//			printf("has_oppose\n");
			reset_has_element();
			tail = -1;
			continue;
		}

		/** Append **/
//		printf("append %c\n", str[i]);
		has_element[str[i]-'A']++;
		res[++tail] = str[i];
	}
	printlist();
}
int main(){
	int i,T;
	scanf("%d", &T);

	for(i=0;i<T;i++){
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}

