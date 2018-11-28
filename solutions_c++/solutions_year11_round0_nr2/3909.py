
#include <cstdio>
#include <vector>
#include <iostream>
#include <map>
#include <string>

int main(int argc, const char *argv[])
{
    using namespace std;
    size_t T;
	//scanf("%d", &T);
	cin >> T; cin.get();
    for (size_t c = 1; c <= T; c++) {
       int C;
	   cin >> C;
	   cin.get();
	   map<string,char> combine;
	   map<char,char> oppose;
	   for(int i = 0; i < C; i++) {
           string s;
		   cin >> s;
		   string key1 = string(1,s[0]) + string(1,s[1]);
		   string key2 = string(1,s[1]) + string(1,s[0]);
		   combine[key1] = s[2];
		   combine[key2] = s[2];
	   }
	   int D;
	   cin >> D;
	   for(int i = 0; i < D; i++) {
		   string s;
		   cin >> s;
           oppose[s[0]] = s[1];
		   oppose[s[1]] = s[0];
	   }
	   int N;
	   cin >> N;
	   string result = "";
	   for(int i = 0; i < N; i++) {
		   char ch;
		   cin >> ch;
		   //combine
		   bool combined = false;
		   result += string(1,ch);
		   //printf("result: %s\n", result.c_str());
		   if (result.size() >= 2) {
			   string end = string(1, result[result.size()-2]) + 
				   string(1,result[result.size()-1]);
			   map<string, char>::iterator itr = combine.find(end);
			   if (itr != combine.end()) {
				   result.resize(result.size()-1);
				  result[result.size()-1] = (*itr).second;
		          //printf("combined: %s\n", result.c_str());
				  combined = true;
			   }
		   }
		   if (!combined) {
			   if (oppose.find(ch) != oppose.end()) {
				   char other = (*(oppose.find(ch))).second;
				   for(int h = 0; h < result.size(); h++)
					   if (result[h] == other) {
                         result = "";
				          //printf("Clearing\n");
					   }
			   }
		   }
	   }
	   cin.get();
	   cout << "Case #" << c << ": [" ;
	   if (result.size() > 0) {
	   for(size_t i = 0; i < result.size()-1; i++) {
          cout << result[i] << ", ";
	   }
	   }
	   if (result.size() > 0)
		   cout << result[result.size()-1];
	   cout << "]" << endl;
    }
	return 0;
}
