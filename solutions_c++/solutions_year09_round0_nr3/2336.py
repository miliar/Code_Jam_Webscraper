#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;


int main(int argc, char** argv) {
  if(argc!=2) {
    cout << "Usage: " << argv[0] << " DATAFILE" << endl;
    exit(1);
  }
  
  ifstream infile(argv[1]);
  if(!infile.good()) {
    cout << "Error: could not open " << argv[1] << endl;
    exit(2);
  }
  
  int N;
  char aLine[512];
  infile.getline(aLine,512);
  string aStr(aLine);
  N=atoi(aStr.c_str());
  vector<string> vLetter;
  vLetter.push_back("a");
  vLetter.push_back("c");
  vLetter.push_back("d");
  vLetter.push_back("e");
  vLetter.push_back("j");
  vLetter.push_back("l");
  vLetter.push_back("m");
  vLetter.push_back("o");
  vLetter.push_back("t");
  vLetter.push_back("w");
  vLetter.push_back(" ");
  //  cout << N << endl;
  for(int iN=0; iN<N; iN++){
    infile.getline(aLine,512);
    aStr=string(aLine);
    //    cout << aStr << " " << aStr.size() <<  endl << endl;
    for(int i=aStr.size()-1; i>=0; i--){
      if(find(vLetter.begin(), vLetter.end(),aStr.substr(i,1))==vLetter.end()) aStr.erase(i,1);
    }
    //    cout << aStr << " " << aStr.size() <<  endl << endl;
    for(int i=aStr.size()-1; i>=0; i--){
     if(aStr.substr(i,1)=="m") break; else aStr.erase(i,1);
    }
    //    cout << aStr << " " << aStr.size() <<  endl << endl;
    int index=0;
    for(int i=0; i<aStr.size(); i++){
      if(aStr.substr(i,1)=="w") break; else index++;
    }
    aStr.erase(0,index);
    //    cout << aStr << " " << aStr.size() <<  endl << endl;
    int counts=0;
    if(aStr.size()>=19){
    for(int i1=aStr.find("w", 0); i1<aStr.size()-18; i1++) { if(aStr.substr(i1,1)!="w") continue;
    for(int i2=aStr.find("e", i1+1); i2<aStr.size()-17; i2++){ if(aStr.substr(i2,1)!="e") continue;
    for(int i3=aStr.find("l", i2+1); i3<aStr.size()-16; i3++){ if(aStr.substr(i3,1)!="l") continue;
    for(int i4=aStr.find("c", i3+1); i4<aStr.size()-15; i4++){ if(aStr.substr(i4,1)!="c") continue;
    for(int i5=aStr.find("o", i4+1); i5<aStr.size()-14; i5++){ if(aStr.substr(i5,1)!="o") continue;
    for(int i6=aStr.find("m", i5+1); i6<aStr.size()-13; i6++){ if(aStr.substr(i6,1)!="m") continue;
    for(int i7=aStr.find("e", i6+1); i7<aStr.size()-12; i7++){ if(aStr.substr(i7,1)!="e") continue;
    for(int i8=aStr.find(" ", i7+1); i8<aStr.size()-11; i8++){ if(aStr.substr(i8,1)!=" ") continue;
    for(int i9=aStr.find("t", i8+1); i9<aStr.size()-10; i9++){ if(aStr.substr(i9,1)!="t") continue;
    for(int i10=aStr.find("o", i9+1); i10<aStr.size()-9; i10++){ if(aStr.substr(i10,1)!="o") continue;
    for(int i11=aStr.find(" ", i10+1); i11<aStr.size()-8; i11++){ if(aStr.substr(i11,1)!=" ") continue;
    for(int i12=aStr.find("c", i11+1); i12<aStr.size()-7; i12++){ if(aStr.substr(i12,1)!="c") continue;
    for(int i13=aStr.find("o", i12+1); i13<aStr.size()-6; i13++){ if(aStr.substr(i13,1)!="o") continue;
    for(int i14=aStr.find("d", i13+1); i14<aStr.size()-5; i14++){ if(aStr.substr(i14,1)!="d") continue;
    for(int i15=aStr.find("e", i14+1); i15<aStr.size()-4; i15++){ if(aStr.substr(i15,1)!="e") continue;
    for(int i16=aStr.find(" ", i15+1); i16<aStr.size()-3; i16++){ if(aStr.substr(i16,1)!=" ") continue;
    for(int i17=aStr.find("j", i16+1); i17<aStr.size()-2; i17++){ if(aStr.substr(i17,1)!="j") continue;
    for(int i18=aStr.find("a", i17+1); i18<aStr.size()-1; i18++){ if(aStr.substr(i18,1)!="a") continue;
    for(int i19=aStr.find("m", i18+1); i19<aStr.size(); i19++){ if(aStr.substr(i19,1)!="m") continue;
      {
	if(i19!=string::npos) {
	  //	  cout << i1<< " " << i2 << " " << i19 << " " << counts << endl;
	  counts++;
	}
      }
    }}}}}}}}}}}}}}}}}}}
   }
    //"welcome to code jam"
 
    cout << "Case #" << iN+1 << ": "; 
    cout.fill ('0');
    cout.width (4);
    cout << counts << endl;
  }
  
  return 0;
}
