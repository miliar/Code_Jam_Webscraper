#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stdlib.h>
using namespace std;
int check(string pat,string word){
	
		return 1;

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
  ofstream outfile("wahomeA.out");
  string filename;
  filename = "A-large.in";
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
		string::iterator it = tcs.begin();
		int o[100];
		int b[100];
		int op=1;
		int bp=1;
		int oi=0;
		int bi=0;
		string rbts;
		int sec=0;
		char activer=tca[1][0];
		int but=GetIntVal(tca[0]);
		int tl=tca.size();
		string tbm="";
		int vb = (tl-1);
		cout <<"VB is :"<<vb<<endl;
		for(int c=0;c<vb;c++){
			
			if(c%2==0){
				activer=tca[c+1][0];
				rbts+=tca[c+1];
				//cout<<"--C: "<<c<<"\'"<<activer<<"\'--";
			}
			else{
				
				if(activer=='O'){
					o[oi]=GetIntVal(tca[c+1]);
					//cout<<o[oi];
					oi++;
					
				}
				else if(activer=='B'){
					b[bi]=GetIntVal(tca[c+1]);
					//cout<<b[bi];
					bi++;
				}
				
			}
		}
		int cn=rbts.length();
		int pos=0;
		//cout <<endl<<"==========================="<<endl<< "TCA length: "<<tcs<<endl;
		//cout <<endl<<"==========================="<<endl<< "RBTS length: "<<cn<<" "<<rbts<<endl;
		//cout <<endl<<"==========================="<<endl<< "RBTS length: "<<cn<<" "<<rbts<<endl;
	//	cout <<endl<<"==========================="<<endl<< "RBTS length: "<<cn<<" "<<rbts<<endl;
		//do the pressing
		for(int h=0;h<100;h++){
			//cout<<b[h];
		}
		cout<<endl;
		for(int h=0;h<100;h++){
			//cout<<o[h];
		}
		cout<<endl;
		int oia = 0;
		int bia = 0;
		while(pos<cn){
			if(rbts[pos]=='O'){
				if(bp==b[bia]&&b[bia]){
					//sec++;
					//pos++;
					//continue;
					//cout<<"Blue Wait"<<endl;
				}
				else{
					if(b[bia]>bp&&b[bia]){
						//sec++;
						bp++;
						//continue;
					}
					else if(b[bia]<bp&&b[bia]){
						//sec++;
						bp--;
						//continue;
					}
				}
				if(op==o[oia]){
					sec++;
					pos++;
					oia++;
					//cout<<"Orange Press"<<endl;
					continue;
					
				}
				else{
					if(o[oia]>op&&o[oia]){
						sec++;
						op++;
						//cout<<"Orange Move Up"<<endl;
						//pos++;
						continue;
					}
					else if(o[oia]<op&&o[oia]){
						sec++;
						//pos++;
						op--;
						//cout<<"Orange Move Down"<<endl;
						continue;
					}
				}
				
			}
			else if(rbts[pos]=='B'){
				if(op==o[oia]&&o[oia]){
					//sec++;
					//pos++;
					//cout<<"Orange Wait"<<endl;
					//continue;
				}
				else{
					if(o[oia]>op&&o[oia]){
						//sec++;
						op++;
						//continue;
					}
					else if(o[oia]<op&&o[oia]){
						//sec++;
						op--;
						//continue;
					}
				}
				if(bp==b[bia]){
					sec++;
					pos++;
					bia++;
					//cout<<"Blue Press"<<endl;
					continue;
					
				}
				else{
					if(b[bia]>bp&&b[bia]){
						sec++;
						//pos++;
						bp++;
						//cout<<"Blue Move Up"<<endl;
						continue;
					}
					else if(b[bia]<bp&&b[bia]){
						sec++;
						//pos++;
						//cout<<"Blue Move Down"<<endl;
						bp--;
						continue;
					}
				}
			}

			cout <<endl<<endl<<"Position :"<<pos<<endl<<endl;
		
		}

		
		outfile << "Case #"<< lp <<": "<<sec <<endl;
		lp = lp +1;
	}
	cout <<"  Success!!"<<endl;

  }
  int x;
  cin >> x;
  return 0;
}