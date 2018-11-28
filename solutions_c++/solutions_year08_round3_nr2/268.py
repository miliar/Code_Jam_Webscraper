// Bertrand Nouvel Google Jam 2008

#include <ext/hash_map>
#include <list>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <gmpxx.h>

using namespace std;
using namespace __gnu_cxx;

int T;

mpz_class zero(0);
mpz_class v2(2);
mpz_class v3(3);
mpz_class v5(5);
mpz_class v7(7);

bool is_ugly(mpz_class z) {
	if (z%v2==zero) {
		return true;
	}
	if (z%v3==zero) {
		return true;
	}
	if (z%v5==zero) {
		return true;
	}
	if (z%v7==zero) {
		return true;
	}
	return false;
}


char * trimzero(char * s) {
	while ((*s=='0')&&(s[1]!=0)) s++;
	return s;
}



void create_sub_expr(const mpz_class & b, char * s,  mpz_class & ctr, int thsgn) {
	char c;
	int l=strlen(s);
	mpz_class v;
	mpz_class tv;

	v=mpz_class(trimzero(s));
	if (thsgn==0) {
		tv=b+v;
//		std::cout << b << "," << v;
	}
	else {
		tv=b-v	;
//		std::cout << b << "," << v;
	}
	if (is_ugly(tv)) { ctr++; /*std::cout << "*" << s;*/}
//	std::cout << "\n";
	//if (v==zero) ctr--;

	for (int i=1;i<l; i++) {
		c=s[i];
		s[i]=0;
		mpz_class t(trimzero(s));
		s[i]=c;
		if (thsgn==0) {
			create_sub_expr(b+t, s+i,  ctr,0);
			create_sub_expr(b+t, s+i,  ctr,1);
		} else {
			create_sub_expr(b-t, s+i,  ctr,0);
			create_sub_expr(b-t, s+i,  ctr,1);
		}			
	}
}


int main(int argc, char ** argv) {
	char buf[1024];
	mpz_class res;
	scanf("%d\n",&T);

	
	for (int t=0; t<T;t++) {
		scanf("%s\n",buf);
		//std::cout << buf << "#\n";
		res=0;
		create_sub_expr(zero,buf,res,0);

		std::cout << "Case #"<< (t+1) << ": " << res << "\n";
	}
	

	

	return 0;
}
