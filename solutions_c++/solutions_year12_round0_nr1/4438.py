#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	
	int map[26];
	int no = 1;
	string in = "ejp mysljylc kd kxveddknmc re jsicpdrysi " 
				 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd "
				 "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string out = "our language is impossible to understand "
				  "there are twenty six factorial possibilities "
			 	 "so it is okay if you want to just give up";
	for (int i = 0; i < in.length(); i++ ) {
		if (in[i] == ' ' )continue;
		map[ in[i] - 97] = out[i] - 97;	
	}
	map[25] = 16;
	map[16] = 25;

	ifstream fin("small");
	ofstream fout("answersmall");
	int T;
	fin>>T;
	//cout<<T<<endl;
	getline(fin,in);
	while (T--) {

	/*	
		for (int i = 0; i < 26;i++ )
			cout<<i<<" "<<map[i]+97<<endl;	
	 */	
	
		getline (fin,in);
		out = "";	
		for (int i = 0; i < in.length(); i++ ) {
			if (in[i] == ' ') { 
				out += ' ';
				continue;
		 	}
			out += map [in[i] - 97] + 97;
		}
		fout<<"Case #"<<no++<<": "<<out<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
