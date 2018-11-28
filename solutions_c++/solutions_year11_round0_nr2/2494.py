#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main(){
    
    ifstream sisf("B.in");
    ofstream valf("B.out");
    
    int T;
    sisf >> T;
    for(int t=1; t<=T; t++){
            
       int C, D, N;
       char comb[257][257][2];
       char a,b,c;
       string spell;
       
       for(int i = 0; i<=256; i++)
          for(int j = 0; j<=256; j++){
             comb[i][j][0]='0';
             comb[i][j][1]='0';
          }
       
       sisf >> C;
       for(int i = 1; i<=C; i++){
          sisf.get(a);
          sisf.get(a);
          sisf.get(b);
          sisf.get(c);
          comb[a][b][0]=c;
          comb[b][a][0]=c;
       }
       
       sisf >> D;
       for(int i = 1; i<=D; i++){
          sisf.get(a);
          sisf.get(a);
          sisf.get(b);
          comb[a][b][1]='1';
          comb[b][a][1]='1';
       }
       //valf << comb['Q']['F'][0] << endl;
       
       sisf >> N;
       sisf.get(a);
       for(int i = 1; i<=N; i++){
          sisf.get(a);
          //valf <<spell[spell.size()-1]<< " "<< a << " " << comb[spell[spell.size()-1]][a][0] << " " << spell.size() << endl;
          if(comb[spell[spell.size()-1]][a][0]!='0'&&spell.size()!=0){
                                                
             b=comb[*(spell.end()-1)][a][0];
             
             spell.erase(spell.end()-1);
             
             spell.push_back(b);
          }
          else{
             spell.push_back(a);
          }
          string::iterator it = spell.end()-1;
          string::iterator ut;
          for(ut = spell.begin(); ut<spell.end(); ut++)
             if(comb[*it][*ut][1]=='1')spell.clear();
       }
       valf << "Case #" << t << ": [";
       for(string::iterator ot = spell.begin(); ot<spell.end(); ot++){
          if(ot==spell.end()-1)valf << *ot;
          else valf << *ot << ", ";
       }
       valf << "]\n";
       
    }
    
    /*int a[257];
    for(int i = 0; i<=256; i++)a[i]=i;
    
    //cout << a['1'] << endl;
    
    string spell;
    spell.push_back('a');
    
    
    
    spell.erase(spell.end()-3);
    
    
    system("PAUSE");*/
    
    
    
    return 0;
}
