#include <stdio.h>
#include <string.h>

int parse(char *s) ;
int pattern_match(char *s1, char *s2) ;

int l, d, n ;
char dic[5010][100] ;
char tok[20][100] ;
char str[1000000] = "" ;

int main()
{
	freopen("A-large.in", "r", stdin) ;
	freopen("A_large.out", "w", stdout) ;
	int i, x, k = 1 ;
	
	while (scanf("%d %d %d", &l, &d, &n) == 3){
		for (i = 1 ; i <= d ; i++) scanf("%s", dic[i]) ;
		for (i = 1 ; i <= n ; i++){
			scanf("%s", str) ;
			x = parse(str) ;
			printf("Case #%d: %d\n", i, x) ;
		}


	}
	return 0 ;
}

int parse(char *s)
{
	int i, x ;
	char temp[1000] = "" ;
	int pos = 0 ;
	int sub_pos = 0 ;
	int count = 0 ;

	for (i = 0 ; s[i] ; i++){
		if (s[i] == '('){
			tok[pos][0] = '\0';
			while (s[i] != ')'){
				tok[pos][sub_pos++] = s[i] ;
				i++ ;
			}
			tok[pos][sub_pos] = '\0' ;
			sub_pos = 0 ;
			temp[pos] = '#' ;
			pos++ ;
		}else{
			temp[pos] = s[i] ;
			pos++ ;
		}
	}
	temp[pos] = '\0' ;
	
	for (i = 1 ; i <= d ; i++){
		x = pattern_match(dic[i], temp) ; 
		if (x == 1) count++ ;
	}
	return count ;
}

int pattern_match(char *s1, char *s)
{
	char s2[1000] = "" ;
	int i ;
	if (strlen(s1) != strlen(s)) return -1 ;
	strcpy(s2, s) ;
	for (i = 0 ; s1[i] ; i++){
		if (s2[i] == '#'){
			if (strchr(tok[i], s1[i]))
				s2[i] = s1[i] ;
		}
	}
	if (!strcmp(s1, s2)) return 1 ;
	return -1 ;
}


