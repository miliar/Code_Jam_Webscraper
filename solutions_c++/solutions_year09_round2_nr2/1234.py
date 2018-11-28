#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

char str[40];
int T;

bool cmp(char A, char B){
	return A > B;
}

int main(){
	scanf ("%d", &T);
	for (int x = 0; x < T; x++){
		scanf ("%s", str);
		int len = strlen(str);
		int pos = 0;
		for (int i = 1; i < len; i++){
			if (str[i] > str[i-1])
				pos = i;
		}
		printf ("Case #%d: ", x+1, pos);
		if (pos){
			int sw = len-1;
			for (int i = len-1; i >=0; i--)
				if (str[i] > str[pos-1]){
					sw=i;
					break;
				}

			swap(str[sw], str[pos-1]);
			sort(str+pos, str+len);
			printf ("%s\n", str);
		}
		else{
			sort(str, str+len);
			int zc = 0;
			int go = 0;
			for (int i = 0; i < len; i++){
				if (str[i] == '0')
					zc++;
				else if (go==0){
					printf ("%c", str[i]);
					for (int j = 0; j <= zc; j++)
						printf ("0");
					go = 1;
				}
				else
					printf ("%c", str[i]);
			}
			printf ("\n");
		}
	} 

}
