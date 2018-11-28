#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdlib.h>
using namespace std;
string check(string pat){
	int ln=pat.length();
	string rf="";
	for(int j=0;j<ln;j++){
		if(j<=(ln-1)){
			rf.insert(rf.end(),pat[j]);
			rf.insert(rf.end(),',');
			rf.insert(rf.end(),' ');
		}
	}
	return rf.substr(0,rf.length()-2);

}
vector<string> splitval(string src,char sep){
	vector<string> vec2;
	int slen=src.length();
	int lst = 0;
	string buff;
	for(int d=0;d<slen;d++){
		if(src[d]==sep){
			if(buff.length()){
				vec2.push_back(buff);
			}
				buff = "";
				
		}else{
			buff+=src[d];
		
		}
		if(d==src.size()-1){
			if(buff.length()){
			vec2.push_back(buff);
			}
		}
		
	
	}
	return vec2;
}

int GetIntVal(string strConvert) { 
  int intReturn; 
  intReturn = atoi(strConvert.c_str()); 
  return(intReturn); 
}
int main ()
{
  ifstream infile;
  ofstream outfile("MagicB.out");
  string filename;
  filename = "B-small-attempt2.in";
  cout << "\n" << filename << "\n";
  infile.open(filename);
  string df;
  vector<string> vec;
  if (infile.is_open())
  {
    while ( infile.good() )
    {
      getline (infile,df);
	  vec.push_back(df);
    }
    infile.close();
	string nn = vec[0];
	vector<string> nna;
	//nna =splitval(nn,' ');
	int tc = GetIntVal(nn);
	int xc = vec.size()-2;
	int lp=1;
	for(int v=0;v<xc;v++){
		cout<<"test Case"<<lp<<endl;
		string tcs =vec[v+1];
		vector<string> tca;
		tca  =splitval(tcs,' ');

		int com=GetIntVal(tca[0]);
		char comb[100][3];
		for(int m=0;m<com;m++){
			comb[m][0]=tca[1+(m*3)][0];
			comb[m][1]=tca[1+(m*3)][1];
			comb[m][2]=tca[1+(m*3)][2];
		}
		int opp=GetIntVal(tca[com+1]);
		char oppb[100][2];
		for(int m=0;m<opp;m++){
			oppb[m][0]=tca[com+2+(m*2)][0];
			oppb[m][1]=tca[com+2+(m*2)][1];
		}
		int basn=GetIntVal(tca[opp+1+com+1]);
		string tryme=tca[opp+1+com+2];
		
		//cout <<"C is : "<<com<<endl;
		//cout <<"D is : "<<opp<<endl;
		//cout <<"N is : "<<basn<<endl;
		for(int z=0;z<opp;z++){
			cout<<oppb[z][0]<<oppb[z][1]<<endl;
		}
		cout<<endl;
		cout <<tryme<<endl<<endl;
		string final;
		for(int g=0;g<basn;g++){
			char cl=tryme[g];
			int fl=final.length();
			int flp=fl-2;
			int fla=fl-1;
			int cat=0;
			int dat=0;
			if(g==0||fl<1){
				final+=cl;
			}
			else{
				//check combine
				for(int z=0;z<com;z++){
					if(cl==comb[z][0]&&final[fla]==comb[z][1]||cl==comb[z][1]&&final[fla]==comb[z][0]){
						//combine
						final[fla]=comb[z][2];
							cat=1;
							break;
					}
				}
				//check oppose
				
				
				if(!cat){	
						int fg=final.length();
						for(int v=0;v<fg;v++){
							for(int z=0;z<opp;z++){
									if(cl==oppb[z][0]&&final[v]==oppb[z][1]||cl==oppb[z][1]&&final[v]==oppb[z][0]){
										//clear
										final="";
										dat=1;
										break;
									}
								}
							if(dat){
								break;
							}
						}
				
						if(!dat){
							final+=cl;
						}
				}

			}
			//cout <<"Final is :"<<final<<endl;

		}
		final="["+check(final)+"]";
		//cout <<final<<endl;
		outfile << "Case #"<< lp <<": "<<final<<endl;
		lp = lp +1;
	}
	cout <<"  Success!!"<<endl;

  }
  int x;
  cin >> x;
  return 0;
}