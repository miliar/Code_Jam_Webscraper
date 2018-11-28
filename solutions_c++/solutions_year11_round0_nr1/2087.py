#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " ")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}

int getSec(int button, int& npos, int& nstat){
	int secs = 0;
	if (npos!=button){
		secs+= abs(button-npos);
		npos = button;
	}
	secs++;
	nstat++;
	
	return secs;
}

int main(){
	int T;
	scanf("%d",&T);
	cin.ignore();
	for (int cs=1; cs<=T; cs++){
		string str;
		getline(cin,str);
		
		vector<string> dat;
		Tokenize(str,dat);
		
		vector<char> col;
		vector<int> button;
		
		vector<int> blue;
		vector<int> orange;
		
		int pos=0;
		int N = atoi(dat[pos].c_str());
		pos++;
		while(pos<dat.size()){
			char c = dat[pos][0];
			col.push_back(c);
			pos++;
			int b = atoi(dat[pos].c_str());
			button.push_back(b);
			pos++;
			if (c=='O')	orange.push_back(b);
			else blue.push_back(b);
		}
		/*for (int k=0; k<N; k++){
			cout<<col[k]<<button[k]<<" ";
		}
		cout<<endl;*/
		
		int minim = 0;
		int so = 0; int po = 1;
		int sb = 0; int pb = 1;
		
		for (int k=0; k<N; k++){
			int secs = 0;
			
			if (col[k]=='O'){
				secs = getSec(orange[so], po, so);
				if (sb<blue.size()){
					int mov = min(abs(pb-blue[sb]), secs);
					if (pb<blue[sb])
						pb += mov;
					else	pb -= mov;
				}
			}
			else{
				secs = getSec(blue[sb], pb, sb);
				if (so<orange.size()){
					int mov = min(abs(po-orange[so]), secs);
					if (po<orange[so])
						po += mov;
					else	po -= mov;
				}
			}
				
			minim += secs;
			/*cerr<<minim<<endl;
			cerr<<"\tOrange: "<<po<<"/"<<so<<" "<<orange[so]<<endl;
			cerr<<"\tBlue: "<<pb<<"/"<<sb<<" "<<blue[sb]<<endl;*/
		}
		
		
		cout<<"Case #"<<cs<<": "<<minim<<endl;
		
	}
	return 0;
}
