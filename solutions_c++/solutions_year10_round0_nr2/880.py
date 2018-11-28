#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

#define MAXDIGITS  100
#define PLUS 1
#define MINUS -1

#define MAXN 1002

typedef struct{
	int digits[MAXDIGITS];
	int signbit;
	int lastdigit;
} bignum;

FILE *infile, *outfile;

void print_bignum(bignum *n) {
	int i;
	 if(n->signbit == MINUS) printf("- ");
	 for(i = n->lastdigit; i >=0; i--) {
		 printf("%c", '0' + n->digits[i]);
		 fprintf(outfile,"%c", '0' + n->digits[i]);
	 }
	 printf("\n");
	 fprintf(outfile,"\n");
}

void zero_justify(bignum *n) {
	while((n->lastdigit > 0) 
		  && (n->digits[n->lastdigit] == 0 ) ) 
		  n->lastdigit--;
	if((n->lastdigit == 0)&&( n->digits[0] == 0)) 
		n->signbit = PLUS;
};

void initialize_bignum(bignum *n) {
	int i;
	n->signbit = PLUS;
	for(i = 0; i < MAXDIGITS; i++) {
		n->digits[i] = 0;
	}
}

void add_bignum(bignum *a, bignum *b, bignum *c) {
	int carry;		// carry digit
	int i;			// counter
	int tmp;		// temp

	initialize_bignum(c);

	c->lastdigit = ( a->lastdigit > b->lastdigit ) ? 
		        (a->lastdigit+1) : (b->lastdigit +1);
	carry = 0;

	for( i = 0; i<= (c->lastdigit ); i++) {
		tmp = carry + a->digits[i] + b->digits[i];
		c->digits[i] = tmp % 10;
		carry = tmp / 10;
	}

	zero_justify(c);
};

int compare_bignum(bignum *a, bignum *b) {
	int i;

	if(b->lastdigit > a->lastdigit ) 
		return (PLUS * a->signbit);
	if(a->lastdigit > b->lastdigit ) 
		return (MINUS * b->signbit);

	for(i = a->lastdigit; i>=0; i--) {
		if(a->digits[i] > b->digits[i]) 
			return (MINUS * a->signbit );
		if(b->digits[i] > a->digits[i]) 
			return (PLUS * a->signbit );
	}

	return 0;
};

void subtract_bignum(bignum *a, bignum *b, bignum *c) {
	int borrow;
	int v, i;

	if( compare_bignum(a,b) == PLUS) {
		subtract_bignum(b,a,c);
		//c->signbit = MINUS;
		return;
	}

	c->lastdigit = (a->lastdigit) > (b->lastdigit) ?
		(a->lastdigit) : (b->lastdigit );
	borrow = 0;
	for(i=0; i<=(c->lastdigit); i++) {
		v = a->digits[i] - borrow - b->digits[i];
		if(a->digits[i] > 0)
			borrow = 0;
		if(v < 0) {
			 v += 10;
			 borrow = 1;
		}

		c->digits[i] = v % 10;
	}
	zero_justify(c);
};

void convert_input(char *str, bignum *n) {
	// convert input string 'str' to number
	initialize_bignum(n);
	int i=0, j = 0, len, l=0;
	len = strlen(str);
	while(!isdigit(str[l])) l++;
	for(i = len-1; i >=l; i--) {
		n->digits[j++] = str[i] - '0';
	}
	n->lastdigit = len - 1;
}
void copy_bignum(bignum *a, bignum *b) {

	initialize_bignum(b);
	b->lastdigit = a->lastdigit;
	b->signbit = a->signbit;
	for(int i = 0; i <= a->lastdigit; i++)
		b->digits[i] = a->digits[i];
}

// calculate a % b for big number
// a should be larger than b at beginning
void mod_bignum(bignum *a, bignum *b, bignum *res) {
	bignum tmp;
	initialize_bignum(&tmp);
	copy_bignum(a, res);
	int comp;

	while ( comp = compare_bignum(res,b),
		    comp != PLUS) {
		if(b->lastdigit == 0 && b->digits[0] == 1) {
			res->lastdigit = 0;
			res->digits[0] = 0;
			return;
		}
		if(b->lastdigit == 0 && b->digits[0] == 2) {
			if(res->digits[res->lastdigit] % 2 == 0) {	
				res->digits[0] = 0;
			}
			else {
				res->digits[0] = 1;
			}

			res->lastdigit = 0;
			return;
		}
		// res > b
		subtract_bignum(res, b, &tmp);
		copy_bignum(&tmp, res);
	}
}

bignum tmp1, tmp2, tmp3;

void gcd_bignum(bignum *a, bignum *b, bignum *res) {
	copy_bignum(a, &tmp1);
	copy_bignum(b, &tmp2);

	int cnt = 0;
	while(tmp2.lastdigit != 0 || tmp2.digits[tmp2.lastdigit] != 0) {
		copy_bignum(&tmp2, &tmp3);
		mod_bignum(&tmp1, &tmp3, &tmp2);
		copy_bignum(&tmp3, &tmp1);
		if(tmp2.lastdigit == 0 && tmp2.digits[0] == 1) {
			copy_bignum(&tmp2, res);
			return;
		}
		if(tmp2.lastdigit == 0 && tmp2.digits[0] == 2) {
			res->lastdigit = 0;
			if(tmp1.digits[0] % 2 == 0) {
				res->digits[0] = 2;
			}
			else {
				res->digits[0] = 1;
			}
			return;
		}

		//printf("%d:\n", cnt++);
		//print_bignum(&tmp1);
		//print_bignum(&tmp2);
		//printf("\n");
	}

	copy_bignum(&tmp1, res);
}

bignum events[MAXN];
bignum diff[MAXN];
bignum gcd[MAXN];

int main() {

	int C, N;

	char instr[MAXN];
	bignum tmp;
	//FILE *infile;
	infile = freopen("B-small-attempt0.in", "r", stdin);

	/*FILE *outfile;*/
	outfile = fopen("c1.out", "w");

	scanf("%d", &C);
	for(int cs = 0; cs < C; cs++) {
		scanf("%d", &N);
		int cnt = 0;
		// read in N numbers, get rid of repeated ones
		for(int i = 0; i < N; i++) {
			bool repeat = false;
			scanf("%s", instr);
			convert_input(instr, &tmp);
			for( int j = 0; j < cnt; j++)
				if(compare_bignum(&events[j], &tmp) == 0 ) {
					repeat = true;
					break;
				};
			if(!repeat) {
				copy_bignum(&tmp, &events[cnt]);
				cnt++;
			}
		}
		// calculate the difference of numbers;
		int cnt2 = 0;
		for(int j = 0; j < cnt; j++) {
			for( int m = j +1; m < cnt; m++) {
				subtract_bignum(&events[j], &events[m], &tmp);
				bool repeat = false;
				for(int k = 0; k < cnt2; k++)
					if(compare_bignum(&diff[k], &tmp) == 0 ) {
						repeat = true;
						break;
					};
				if(!repeat) {
					copy_bignum(&tmp, &diff[cnt2]);
					cnt2++;
				}
			}
		}
		// calculate the gcd of the differences
		copy_bignum(&diff[0], &tmp);
		for(int j = cnt2 -1; j >= 0; j--) {
			for(int k = 0; k < j; k++) {
				gcd_bignum(&diff[k],&diff[k+1], &tmp);
				copy_bignum(&tmp, &diff[k]);
			}
		}

		bignum result;
		while(compare_bignum(&tmp, &events[0]) == PLUS) {
			add_bignum(&diff[0], &tmp, &result);
			copy_bignum(&result, &tmp);
		}
		subtract_bignum(&tmp, &events[0], &result);

		printf("Case #%d: ", cs+1);
		fprintf(outfile, "Case #%d: ", cs+1);
		print_bignum(&result);
		
	}


	//bignum n1, n2, n3;
	//char input1[MAXDIGITS], input2[MAXDIGITS];

	//for(int i = 0; i < 10; i++) {
	//scanf("%s %s", input1, input2);
	//convert_input(input1, &n1);
	//convert_input(input2, &n2);
	////print_bignum(&n1);
	////print_bignum(&n2);

	//add_bignum(&n1, &n2, &n3);
	////print_bignum(&n3);
	//subtract_bignum(&n1, &n2, &n3);
	////print_bignum(&n3);
	//if( compare_bignum(&n1, &n2) == PLUS)
	//	mod_bignum(&n2, &n1, &n3);
	//else
	//	mod_bignum(&n1, &n2, &n3);
	//printf("module: ");
	//print_bignum(&n3);

	//gcd_bignum(&n1, &n2, &n3);
	//printf("gcd: ");
	//print_bignum(&n3);
	//}

	return 1;
	
}