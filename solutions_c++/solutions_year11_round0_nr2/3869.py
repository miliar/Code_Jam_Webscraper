
#include <iostream>
#include <vector>
#include <fstream>
#include <map>
#include <algorithm>
#include <string>



int main(int argc, char** argv){
	std::ifstream input(argv[1],std::ios_base::in);
	std::ofstream output(argv[2],std::ios_base::out);
	int caseNum;
	input>>caseNum;
	for(int k = 0;k<caseNum;++k)
	{
		int combsCount;
		input>>combsCount;
		//std::cout<<"combsCount:"<<combsCount<<"\n";
		std::map<std::string,char> combs;
		if(combsCount!=0){
		//Store combs here
			for(int i = 0;i<combsCount;++i){
				char a,b,c;
				input>>a>>b>>c;
				std::string s = "";
				s+=a;
				s+=b;
				combs[s] = c;
				//std::cout<<a<<b<<c<<"\n";
			}
		}
		int opsCount;
		input>>opsCount;
		//std::cout<<"opsCount:"<<opsCount<<"\n";
		std::map<char,char> ops;
		if(opsCount!=0){
			for(int i = 0;i<opsCount;++i){
				char a,b;
				input>>a>>b;
				ops[a] = b;
				ops[b] = a;
				//std::cout<<a<<b<<"\n";
			}
		//store ops here;
		}
		int bes;
		input>>bes;
		//std::cout<<"bes:"<<bes<<"\n";
		std::vector<char> elems(0);
		if(bes!=0){
			for(int i = 0;i<bes;++i)
			{
				char c;
				input>>c;
				if(elems.empty()){
					elems.push_back(c);
					continue;
				}
				//std::cout<<c<<"\t";
				std::string s;
				s += c;
				s += elems.back();
				if(combs.count(s)>0){
					//std::cout<<"qweert\n";
					elems.pop_back();
					elems.push_back(combs[s]);
					continue;
				}
				s = "";
				s += elems.back();
				s += c;
				if(combs.count(s)>0){
					//std::cout<<"asdfg\n";
					elems.pop_back();
					elems.push_back(combs[s]);
					continue;
				}
				elems.push_back(c);
				if(ops.count(c)>0){
					//std::cout<<"zxcvb\n";
					for(unsigned vi = 0;vi<elems.size()-1;vi++){
						if(ops[c] == elems[vi]){
							elems.clear();
							break;;
						}
					}
				}
			}
			//elems read here
		}
		
		//for(std::vector<char>::iterator vvv = elems.begin();vvv!=elems.end();++vvv)
		//	std::cout<<*vvv;
		//std::cout<<"\n";
		
		output<<"Case #"<<k+1<<": [";
		
		if(!elems.empty()){
			for(unsigned vi = 0;vi<elems.size()-1;vi++){
				output<<elems[vi]<<", ";
			}
			output<<elems[elems.size()-1];
		}
		output<<"]\n";
	}
	system("pause");
	return 0;
}