#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int T;
	ifstream in = ifstream("A-large.in");
	ofstream out = ofstream("out.txt");
	in>>T;
	int testn = 0;
	for(int ii=0;ii<T;ii++){
		testn++;
		vector<string> m;
		bool found = false;
		bool dotexist = false;
		for(int i=0 ; i<4 ; i++){
			string rstr;
			in>>rstr;

			m.push_back(rstr);
			

			int xcount = 0, ocount = 0 , tcount = 0;
			for(int j=0 ; j<4 ; j++){
				if(rstr[j] == 'X') xcount += 1;
				else if(rstr[j] == 'O') ocount += 1;
				else if(rstr[j] == 'T') tcount += 1;
				else if(rstr[j] == '.') dotexist = true;
			}

			if((xcount==4) || (xcount==3&&tcount==1)){
				out<<"Case #"<<testn<<": X won"<<endl;
				found = true;				
			}
			else if((ocount==4) || (ocount==3&&tcount==1)){
				out<<"Case #"<<testn<<": O won"<<endl;
				found = true;				
			}

			if(found){
				for(i=i+1;i<4 ; i++) in>>rstr;
			}
		}

		if(found) continue;

		for(int i=0 ; i<4 ; i++){
			int xcount = 0, ocount = 0 , tcount = 0;
			for(int j=0 ; j<4 ; j++){
				if(m[j][i] == 'X') xcount += 1;
				else if(m[j][i] == 'O') ocount += 1;
				else if(m[j][i] == 'T') tcount += 1;
			}

			if((xcount==4) || (xcount==3&&tcount==1)){
				out<<"Case #"<<testn<<": X won"<<endl;
				found = true;
				break;
			}
			else if((ocount==4) || (ocount==3&&tcount==1)){
				out<<"Case #"<<testn<<": O won"<<endl;
				found = true;
				break;
			}
		}

		if(found) continue;

		int xcount = 0, ocount = 0 , tcount = 0;
		for(int i=0 ; i<4 ; i++){
			if(m[i][i] == 'X') xcount += 1;
			else if(m[i][i] == 'O') ocount += 1;
			else if(m[i][i] == 'T') tcount += 1;
		}

		if((xcount==4) || (xcount==3&&tcount==1)){
			out<<"Case #"<<testn<<": X won"<<endl;
			found = true;
			
		}
		else if((ocount==4) || (ocount==3&&tcount==1)){
			out<<"Case #"<<testn<<": O won"<<endl;
			found = true;
			
		}

		if(found) continue;

		xcount = 0, ocount = 0 , tcount = 0;
		for(int i=0 ; i<4 ; i++){
			if(m[i][3-i] == 'X') xcount += 1;
			else if(m[i][3-i] == 'O') ocount += 1;
			else if(m[i][3-i] == 'T') tcount += 1;
		}

		if((xcount==4) || (xcount==3&&tcount==1)){
			out<<"Case #"<<testn<<": X won"<<endl;
			found = true;
			
		}
		else if((ocount==4) || (ocount==3&&tcount==1)){
			out<<"Case #"<<testn<<": O won"<<endl;
			found = true;
			
		}

		if(found) continue;

		if(dotexist) out<<"Case #"<<testn<<": Game has not completed"<<endl;
		else out<<"Case #"<<testn<<": Draw"<<endl;
	}
}