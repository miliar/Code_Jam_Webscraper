#include "map"
#include "string"
#include "iostream"

typedef std::map<char,char> charactermap;

int main()
{
	charactermap googlese_map;
	googlese_map.insert(std::pair<char,char>(' ',' '));
	googlese_map.insert(std::pair<char,char>('a','y'));
	googlese_map.insert(std::pair<char,char>('b','h'));
	googlese_map.insert(std::pair<char,char>('c','e'));
	googlese_map.insert(std::pair<char,char>('d','s'));
	googlese_map.insert(std::pair<char,char>('e','o'));
	googlese_map.insert(std::pair<char,char>('f','c'));
	googlese_map.insert(std::pair<char,char>('g','v'));
	googlese_map.insert(std::pair<char,char>('h','x'));
	googlese_map.insert(std::pair<char,char>('i','d'));
	googlese_map.insert(std::pair<char,char>('j','u'));
	googlese_map.insert(std::pair<char,char>('k','i'));
	googlese_map.insert(std::pair<char,char>('l','g'));
	googlese_map.insert(std::pair<char,char>('m','l'));
	googlese_map.insert(std::pair<char,char>('n','b'));
	googlese_map.insert(std::pair<char,char>('o','k'));
	googlese_map.insert(std::pair<char,char>('p','r'));
	googlese_map.insert(std::pair<char,char>('q','z'));
	googlese_map.insert(std::pair<char,char>('r','t'));
	googlese_map.insert(std::pair<char,char>('s','n'));
	googlese_map.insert(std::pair<char,char>('t','w'));
	googlese_map.insert(std::pair<char,char>('u','j'));
	googlese_map.insert(std::pair<char,char>('v','p'));
	googlese_map.insert(std::pair<char,char>('w','f'));
	googlese_map.insert(std::pair<char,char>('x','m'));
	googlese_map.insert(std::pair<char,char>('y','a'));
	googlese_map.insert(std::pair<char,char>('z','q'));

	int test_number = 0;

	std::cin >> test_number;
	std::cin.ignore(1,'\n');

	for (int test_case = 0; test_case < test_number; ++test_case)
	{
		std::cout << "Case #" << test_case+1 << ": ";
		char string_to_translate[200];
		std::cin.getline(string_to_translate,200);
		for (char* itr = string_to_translate; *itr != '\0'; ++itr)
		{
			std::cout << googlese_map[*itr];
			//std::cout << *itr;
		}
		std::cout << std::endl;
	}

}