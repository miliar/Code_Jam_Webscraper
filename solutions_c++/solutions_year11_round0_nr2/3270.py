#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<list>

using namespace std;
//Q, W, E, R, A, S, D, F
int main()
{
	int T;

	std::cin >> T;
	int case_num = 1;
	vector<char> base_elements(8);
	base_elements[0] = 'Q';
	base_elements[1] = 'W';
	base_elements[2] = 'E';
	base_elements[3] = 'R';
	base_elements[4] = 'A';
	base_elements[5] = 'S';
	base_elements[6] = 'D';
	base_elements[7] = 'F';

	while (case_num <= T)
	{
		while(1)
		{
		 int C,D,N,temp=0;
		 string tempStr,codeStr;
		 std::cin >> C;
		 map<pair<char,char>,char> B_to_NB;
		 map<pair<char,char>,int> oppose;
		 while(temp < C)
		 {
			 std::cin >> tempStr;
				 B_to_NB.insert(make_pair(make_pair((char)tempStr[0],(char)tempStr[1]),(char)tempStr[2]));
				 B_to_NB.insert(make_pair(make_pair((char)tempStr[1],(char)tempStr[0]),(char)tempStr[2]));
			 temp++;
		 }
		 temp = 0;
		 std::cin >> D;
		 while(temp < D)
		 {
			 std::cin >> tempStr;
				 oppose.insert(make_pair(make_pair(tempStr[0],tempStr[1]),1));
				 oppose.insert(make_pair(make_pair(tempStr[1],tempStr[0]),1));
			 temp++;
		 }

		 temp = 0;
		 std::cin >> N;
		 std::cin >> codeStr;
		 list<char> charlist;
		 //int cur_vec_pos = -1;
		 while(temp < N)
		 {
			 vector<char>::const_iterator result = find(base_elements.begin(), base_elements.end(), codeStr[temp]);
			 if(result != base_elements.end() && !charlist.empty())
			 {
					 map<pair<char,char>,char>::iterator it1 = B_to_NB.find(make_pair(codeStr[temp],charlist.back()));
					 if(it1 != B_to_NB.end())
					 {

						 charlist.pop_back();
						 charlist.push_back(it1->second);
					 }
					 else
					 {
						 int called = 0;
						 map<pair<char,char>,int>::iterator it2;
						 list<char>::iterator it3 = charlist.begin();
						 while(it3 != charlist.end())
						 {
							 it2 = oppose.find(make_pair(codeStr[temp],*it3));
							 if(it2 != oppose.end())
								 {
									 charlist.clear();
									 //cur_vec_pos = -1;
									 called = 1;
									 break;
								 }
							 it3++;
					     }
						 if(called == 0)
						 {
							 charlist.push_back(codeStr[temp]);
				             //cur_vec_pos++;
						 }
				     }
			  }
			 else
			 {
				 charlist.push_back(codeStr[temp]);
				 //cur_vec_pos++;
			 }
			 temp++;
		 }
		 std::cout << "Case #" << case_num << ": [" ;
		 list<char>::iterator it4 = charlist.begin();
		 while(it4 != charlist.end())
		 {
			 std::cout << *it4 ;
			 it4++;
			 if(it4 != charlist.end())
			 {
				 std::cout << ", " ;
			 }
		 }
		 std::cout << "]" << std::endl;
		 break;
		}
		case_num++;
	}
	return 1;
}