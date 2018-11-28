#include <map>
#include <iostream>
#include <string>

using namespace std;

static int solve_case(void);

int main(void){
	int N;	
	cin >> N;

	for(int i=0; i<N; i++){
		cout << "Case #" << i+1 << ": " << solve_case() << endl;
	}

}

typedef map<string,char*> engine_map_t;


static int solve_case(void)
{
	int S;
	engine_map_t engine_map;
	string help_str;

	cin >> S;
	getline(cin, help_str);
	
	char* help_arr = new char[S];

	for(int i=0; i<S; i++){
		getline(cin, help_str);
		engine_map[help_str] = help_arr+i;
	}
   
	memset(help_arr,0,S);

	int Q = -1;
	cin >> Q;
	getline(cin,help_str);

	int switch_count = 0;
	int free_engines = S;
	for(int i = 0; i<Q; i++){
		getline(cin,help_str);
		char * t = engine_map[help_str];
		if(*t==0){
			*t = 1;
			free_engines--;
			if(free_engines==0){
				switch_count++;
				memset(help_arr,0,S);
				*t = 1;
				free_engines = S-1;
			}
		}
	}

	return switch_count;
}
