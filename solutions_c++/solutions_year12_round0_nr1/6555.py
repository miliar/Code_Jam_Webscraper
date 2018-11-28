#include <fstream>
#include <iostream>
#include <string>
#include <bitset>

using namespace std;

void build_map( char* );

int main( void ){
	fstream input, output;
		
	input.open("googlerese-small.in", fstream::in);
	output.open("googlerese-small.out", fstream::out | fstream::app );
	
	char map[26];
	build_map( map );
	
	/*for( int i=0; i<26; i++ ){
		cout << (char)(97+i) << " ==> " << map[i] << endl;
	}*/
	
	int num_cases;
	string str_in, str_out;
	
	input >> num_cases;
	
	for( int i=0; i<num_cases; i++){
		char c;
		c = input.peek();
		
		if( c < 97 | c > 97+26 )
			input.ignore();
	
		getline(input, str_in);
		
		int kStrSize = str_in.length();
		char tmp[kStrSize+1];
		
		for( int j=0; j<kStrSize; j++ ){
			int num = (int) str_in[j]%97;
			
			if( num < 26 )
				tmp[j] = map[num];
			else
				tmp[j] = ' ';
		}
		
		tmp[kStrSize] = '\0';
		
		output << "Case #" << i+1 << ": " << tmp << endl;
	}

	return 0;
}

void build_map( char* map){
	bitset<26> e, g;
	e.set();
	g.set();
	
	string str_g="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv", str_e="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	
	// english->googlerese: a->y o->e z->q
	string tmp_g="yeq", tmp_e="aoz";
	for(int i=0; i<3; i++){
		int num= (int)tmp_g[i] % 97;
		map[num]=tmp_e[i];
		
		int idx = (int)tmp_e[i]%97;
		g.reset(num);
		e.reset(idx);
		
	}
	
	for( int i=0; i<str_g.length(); i++ ){
		int num = (int)str_g[i] % 97;
		//cout << str_g[i] << " " << num << endl;
		if( num < 26 ){
			map[num] = str_e[i];
			
			int idx = (int)str_e[i]%97;
			g.reset(num);
			e.reset(idx);
		}		
	}
		
	while( g.any() ){
		int i = 0, j=0;
		
		while(i<26 & ~g[i])
			i++;
		while(j<26 & ~e[j])
			j++;
		
		map[i] = (char)(97 + j);
		
		g.reset(i);
	}

}
