#include <iostream>
#include <string>
#include <map>
#include <fstream>
using namespace std;

const bool TEST = false;

int main(int argc, char* argv[]){

	ifstream fp;
	fp.open(argv[1]);
	
	if(fp.is_open()){
		ofstream ofp("A-small-attempt43.out");
		map<char,char> rdic,dic;
		rdic['a'] = 'y';
		rdic['b'] = 'n';
		rdic['c'] = 'f';
		rdic['d'] = 'i';
		rdic['e'] = 'c';
		rdic['f'] = 'w';
		rdic['g'] = 'l';
		rdic['h'] = 'b';
		rdic['i'] = 'k';
		rdic['j'] = 'u';
		rdic['k'] = 'o';
		rdic['l'] = 'm';
		rdic['m'] = 'x';
		rdic['n'] = 's';
		rdic['o'] = 'e';
		rdic['p'] = 'v';
		rdic['q'] = 'z';
		rdic['r'] = 'p';
		rdic['s'] = 'd';
		rdic['t'] = 'r';
		rdic['u'] = 'j';
		rdic['v'] = 'g';
		rdic['w'] = 't';
		rdic['x'] = 'h';
		rdic['y'] = 'a';
		rdic['z'] = 'q';
		rdic[' '] = ' ';
		for(map<char,char>::iterator it = rdic.begin();it != rdic.end();it++){
			dic[(*it).second] = (*it).first;
		}
		
		string sen;
		size_t num,cnum=0;
		fp>>num;
		getline(fp,sen);	// flash the newline
		while(cnum<num){
			getline(fp,sen);
			for(size_t i = 0 ; i < sen.size();i++){
				sen[i]=dic[sen[i]];
			}
			if(!TEST){
				ofp<<"Case #"<<cnum+1<<": "<<sen<<endl;
			}
			else{
			
				cout<<"Case #"<<cnum+1<<": "<<sen<<endl;
				getchar();
			}
			cout<<"Case #"<<cnum+1<<": "<<sen<<endl;
			sen.clear();
			
			cnum++;
		}
		ofp.close();
		fp.close();
	}else{
		cerr<<"Can't open file!"<<endl;
	}


	return 0;
}

