#include <iostream>
#include <vector>

int pequal(std::pair <char, char> p1, std::pair <char, char> &p2){
return ((p1.first == p2.first && p1.second == p2.second)
	|| (p1.first == p2.second && p1.second == p2.first));
}

int main(int argc, char ** argv){

 std::vector <char> elements;
 std::vector < std::pair < std::pair <char,char> , char > > combinations;
 std::vector < std:: pair <char, char> > opposed;
 char e1, e2, e3;
 unsigned T, N, i , j, k, l, D, C;

 std:: cin >> T;
 for(i=0;i<T;i++){
 std::cin >> C;
 elements.clear();
 opposed.clear();
 combinations.clear();
 for(j=0;j<C;j++){
	std::cin >> e1 >> e2 >> e3;
	combinations.push_back(std::make_pair(std::make_pair(e1,e2),e3));
	}
 std::cin >> D;
 for(j=0;j<D;j++){
	std::cin >> e1 >> e2;
	opposed.push_back(std::make_pair(e1,e2));
	}
 std::cin >> N;
 for(j=0;j<N;j++){
	std::cin >> e1;
	if (elements.empty()) { elements.push_back(e1); continue; }
	elements.push_back(e1);
	while(1){
		e1 = *(elements.end() - 1);
		e2 = *(elements.end() - 2);
		
		for(k=0;k<C;k++)
			if (pequal(std::make_pair(e1,e2),combinations[k].first)){
			elements.pop_back();
			elements.pop_back();
			elements.push_back(combinations[k].second);
			continue;
			}
		if(k>=C) break;
		}
	e1 = elements.back();
	for (k = 0; k < (elements.size() - 1);k++){
		for (l = 0; l< opposed.size();l++)
			if(pequal(std::make_pair(e1,elements[k]),opposed[l])) 
				{ elements.clear();	e1= 0; break;}
			if(e1 == 0) break;
		}
 	}
 std::cout<<"Case #"<< i+1<<": [";
 if(elements.size() == 0 ) {std::cout <<"]\n"; continue; }
 for (j=0;j<elements.size()-1;j++){
	std::cout<<elements[j]<<", ";
	}
 if (elements.size()) std::cout<< elements[elements.size()-1];
 std::cout<<"]\n";

 }

 return 0;
}
