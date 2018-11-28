#include <stdio.h>
#include <vector>
#include <string>
#include <list>
#include <fstream>
#include <gmpxx.h>

typedef mpz_class bigint;

bigint run(int C,std::vector<bigint>& t);

bigint bi_gcd(bigint a,bigint b){
	bigint buf;
	while(b!=0){
		buf = a % b;
		a = b;
		b = buf;
	}
	return a;
}

int main(int argc,char** argv){
	char* p;
	
	std::ifstream ifs(argv[1]);
	std::string buf;
	std::getline(ifs,buf);
	int T = atoi(buf.c_str());
	int c = 0;

	while(ifs && getline(ifs,buf)){
		c++;
		std::vector<bigint> g;
		std::string str = buf;		
		int cut;
		while( (cut = str.find_first_of(" ")) != str.npos){
			if(cut > 0){
				bigint tmp(str.substr(0,cut));
				g.push_back(tmp);
			}
			str = str.substr(cut+1);	
		}
		if(str.length()>0){
			bigint tmp(str);
			g.push_back(tmp);
		}
		int C = g.begin()->get_si();
		g.erase(g.begin());
		bigint result = run(C,g);
		printf("Case #%d: %s\n",c,result.get_str().c_str());
	}
}

bigint run(int C,std::vector<bigint>& t){
	std::list<bigint> subpair;
	for(std::vector<bigint>::iterator ite = t.begin(); ite < t.end(); ite++){
		fprintf(stderr,"%s ",ite->get_str().c_str());
		for(std::vector<bigint>::iterator ite2 = ite+1; ite2<t.end(); ite2++){
			if(*ite > *ite2){
				subpair.push_back(*ite - *ite2);
			}else{
				subpair.push_back(*ite2- *ite );
			}
		}
	}
	fprintf(stderr,"\n");
	bigint gcd = *(subpair.begin());
	for(std::list<bigint>::iterator ite = ++subpair.begin(); ite != subpair.end(); ite++){
		gcd = bi_gcd(gcd,*ite);
	}
	fprintf(stderr,"GCD:%s\n",gcd.get_str().c_str());

	bigint closest_sub_mult;
	for(int i=0;i<1000;i++){
		int flag = 1;
		closest_sub_mult = ((*t.begin())/gcd + i)*gcd - *t.begin();
		//printf("INT %s\n",closest_sub_mult.get_str().c_str());
		if(closest_sub_mult < 0){
			continue;
		}
		for(std::vector<bigint>::iterator ite = t.begin() + 1; ite < t.end(); ite++){
			bigint closest_sub_mult2 = ((*ite)/gcd + i)*gcd - *ite;
			if(closest_sub_mult != closest_sub_mult2){
				flag = 0;
				break;
			}
		}
		if(flag){
			break;
		}
	}
	fprintf(stderr,"CLOSEST SUB MULT:%s\n",closest_sub_mult.get_str().c_str());
	return closest_sub_mult; 
}
