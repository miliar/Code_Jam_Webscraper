#include <stdio.h>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <fstream>

unsigned long long int run(int R,int k,int N,std::list<int>& g);

int main(int argc,char** argv){
	std::ifstream ifs(argv[1]);
	std::string buf;
	char* p;
	
	if(!ifs || !getline(ifs,buf)) return 1;
	int T = atoi(buf.c_str());
	int c = 0;;

	while(T-->0){
		c++;
		int R,k,N;
		if(!ifs || !getline(ifs,buf)) break;
		sscanf(buf.c_str(),"%d %d %d",&R,&k,&N);
		if(!ifs || !std::getline(ifs,buf)) break;
		std::list<int> g;
		std::string str = buf;		
		int cut;
		while( (cut = str.find_first_of(" ")) != str.npos){
			if(cut > 0){
				std::string tmp = str.substr(0,cut);
				g.push_back(atoi(tmp.c_str()));
			}
			str = str.substr(cut+1);	
		}
		if(str.length()>0){
			g.push_back(atoi(str.c_str()));
		}
		printf("Case #%d: %lld\n",c,run(R,k,N,g));
	}
}

std::list<int>::iterator getSlider(std::list<int>& g,std::list<int>::iterator& ite,unsigned int & hash,const int N,int& ck){
	int c=0;
	hash = 0x12345678;
	while(ck>=*ite && N>c){
		ck -= *ite;
		hash ^= *ite;
		ite++;
		c++;
		if(ite == g.end()){
			ite = g.begin();
		}		
	}
	return ite;
}



unsigned long long int run(int R,int k,int N,std::list<int>& g){
	std::list<int>::iterator ite = g.begin();
	std::vector<std::string> series;
	int ck;
	unsigned long long int outer_cycle_euro = 0;
	int lim;
	unsigned long long int inner_cycle_euro = 0;
	std::string bef = "";
	int inner_loop_count = 1;

	int relax_time = 10000;
	int is_cycle_finded = 0;
	unsigned int hash;
	while(R>0 && relax_time-->0){
		R--;
		ck = k;
		ite = getSlider(g,ite,hash,N,ck);
		inner_cycle_euro += k-ck;
	}
	// assume cyclic series
	if(R>0){
		unsigned int tmp[1000];
		std::list<int>::iterator old_ite = ite;
		for(int i=0;i<1000;i++){
			ck = k;
			ite = getSlider(g,ite,hash,N,ck); 
			tmp[i] = hash;
		}
	

		int i;	
		for(i=1;i<1000;i++){
			if(tmp[0] == tmp[i]){
				int flag = 0;
				for(int j=0; j+i<1000;j++){
					if(tmp[j+i] != tmp[j]){
						flag = 1;
						break;
					}
				}
				if(flag == 0){
					// cycle found
					// 0 -> i-1 is cycle
					break;
				}else{
					// not cycle
					continue;
				}
			}
		}
		ite = old_ite;
		for(int j=0;j<i;j++){
			ck = k;
			ite = getSlider(g,ite,hash,N,ck);
			outer_cycle_euro += k-ck;
		}	
		int rest = R % i;
		int count = R / i;
		outer_cycle_euro *= count;
		R = rest;

	}
	while(R-->0){
		ck = k;
		ite = getSlider(g,ite,hash,N,ck);
		inner_cycle_euro += k-ck;
	}

	return inner_cycle_euro + outer_cycle_euro;
}
