#include <map>
#include <iostream>
#include "string"
using namespace std;

void create_mapping(string& scrambled, string& human, map<char, char>& mapping)
{	
	for(int i = 0; i < scrambled.length(); ++i)
	{
		//if(scrambled[i] != ' ')
		//{
			mapping[ scrambled[i] ] = human[i];
		//}
	}
	
}

void solve_mappping(map<char, char>& mapping)
{
	
	string scrambled1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string human1 = "our language is impossible to understand";
	create_mapping(scrambled1, human1, mapping);	
	scrambled1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	human1 = "there are twenty six factorial possibilities";
	create_mapping(scrambled1, human1, mapping);	
	human1 = "so it is okay if you want to just give up";
	scrambled1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	create_mapping(scrambled1, human1, mapping);
	mapping['z'] = 'q';
	mapping['q'] = 'z';
	typedef pair<const char,char> map_iter_t;
	std::cout<<"{ ";
	for_each(mapping.begin(), mapping.end(), ^(map_iter_t it) {
		std::cout << "{ "<< it.first << " , " << it.second <<" }, ";
	});
	std::cout<<" }";	
}


int main()
{
	map<char, char> mapping;
	solve_mappping(mapping);
	freopen("A-small-attempt0.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    string tcCount;
    std::getline(std::cin, tcCount);
    string in_line;
    string out_line;
    int line_nbr = 1;
	while (std::getline(std::cin, in_line))
	{
		string out_line(in_line);
		for (int i = 0; i < in_line.length(); ++i)
		{
			out_line[i] = mapping[ in_line[i] ];
		}
    	std::cout <<"Case #" <<line_nbr <<": " << out_line << std::endl;
    	++line_nbr;
	}


}