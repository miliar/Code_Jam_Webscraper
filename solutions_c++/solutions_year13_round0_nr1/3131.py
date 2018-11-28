#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>


using namespace std;

int main(int argc, char *argv []) {
  if(argc<3) return 1;
  ifstream input;
  input.open(argv[1]);
  ofstream output;
  output.open(argv[2]);
  int tcc;
  string nummern;
  getline(input,nummern);
  stringstream(nummern)>>tcc;
  for(int testnr=1;testnr<=tcc;testnr++) {
    string feld[4];
    for(int i=0;i<4;i++)
      getline(input,feld[i]);
    input.ignore();
    bool ow=false;
    bool tw=false;
    bool free=false;
    for(int i=0;i<4;i++) {
      bool owmomhor=true;
      bool twmomhor=true;
      bool owmomver=true;
      bool twmomver=true;
      for(int j=0;j<4;j++) {
        owmomhor&=(feld[i][j]=='T'||feld[i][j]=='O');
        twmomhor&=(feld[i][j]=='T'||feld[i][j]=='X');
        owmomver&=(feld[j][i]=='T'||feld[j][i]=='O');
        twmomver&=(feld[j][i]=='T'||feld[j][i]=='X');
        free|=(feld[i][j]=='.');
      }
      ow|=(owmomhor||owmomver);
      tw|=(twmomhor||twmomver);
    }
    bool owdigl=true;
    bool owdigr=true;
    bool twdigl=true;
    bool twdigr=true;
    for(int i=0;i<4;i++) {
      owdigl&=(feld[i][i]=='T'||feld[i][i]=='O');
      owdigr&=(feld[i][3-i]=='T'||feld[i][3-i]=='O');
      twdigl&=(feld[i][i]=='T'||feld[i][i]=='X');
      twdigr&=(feld[i][3-i]=='T'||feld[i][3-i]=='X');
    }
    ow|=(owdigr||owdigl);
    tw|=(twdigr||twdigl);
    output<<"Case #"<<testnr<<": ";
    if(tw&&!ow)
      output<<"X won"<<endl;
    if(!tw&&ow)
      output<<"O won"<<endl;
    if(tw&&ow)
      output<<"Draw"<<endl;
    if(!tw&&!ow)
      if(free) {
        output<<"Game has not completed"<<endl;
      } else {
        output<<"Draw"<<endl;
      }
  }
  input.close();
  output.close();
  cout<<"\nFinished\n";
  return 0;
}
