#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

using namespace std;

int main() {



    string filename= "set1.txt";
     ifstream fin(filename.c_str());
     ofstream fout("set2.txt");
     
vector <int> O(0);
vector <int> B(0);
vector <char> OB(0);
int counter=0;
int numberbutton=0;
char a;
int b;
int bufferposO=1;
int bufferposB=1; 
int bufferO=0;
int bufferB=0;
int time=0;
int testcase=0;
fin>>testcase;

int timestayO=0;
int timestayB=0;
int counterB=0;
int counterO=0;
int moveO=0;
int moveB=0;

for(int j=0; j<testcase;j++) {

bufferposO=1;
bufferposB=1; 
bufferO=0;
bufferB=0;
time=0;
O.clear();
B.clear();
OB.clear();
fin>>numberbutton; // sum number button need to be pressed

for(int i=0; i<numberbutton;i++) {
       
       fin>>a; // awal O or B
       fin>>b;
       OB.push_back(a);
       if(a=='O') {
                  
                    O.push_back(b);
                    }
       else 
         B.push_back(b);     
       
       
       }
       
// move , for O
for(int i=0; i<O.size();i++) {
        if(O[i]>=bufferposO)
        time+=O[i]-bufferposO;
        else
        time+=bufferposO-O[i];
        bufferposO=O[i];
        }
time+=O.size(); // move + press, for O

// stay;
bufferposO=1;
bufferposB=1;
timestayO=0;
timestayB=0;
counterB=0;
counterO=0;
moveO=0;
moveB=0;

if(O.size()==0) 
O[0]=1;
if(B.size()==0)
B[0]=1;

for(int i=0; i<OB.size();i++) {
 // O 5 O 8 B 3
        if(OB[i]=='O')
        {
        moveO= fabs(O[counterO]-bufferposO)+1;
       
        if(moveO>=fabs(B[counterB]-bufferposB)) 
        {
        timestayB+=moveO-fabs(B[counterB]+bufferposB);
       
        bufferposB=B[counterB];
        }
        if(moveO<fabs(B[counterB]-bufferposB)) 
        {
        if(bufferposB<B[counterB]) 
        bufferposB=bufferposB+moveO;
        if(bufferposB>B[counterB])
        bufferposB=bufferposB-moveO;
        }
                 
        bufferposO=O[counterO];
        if(counterO!=O.size()-1)
        counterO++;
          
        }
            if(OB[i]=='B')
        {
        moveB= fabs(B[counterB]-bufferposB)+1;
    
        if(moveB>=fabs(O[counterO]-bufferposO)) 
        {
       
        timestayO+=moveB-fabs(O[counterO]-bufferposO);
        bufferposO=O[counterO];
        }
        if(moveB<fabs(O[counterO]-bufferposO)) 
        {
        if(O[counterO]>bufferposO)
        bufferposO=bufferposO+moveB;
        if(O[counterO]<bufferposO)
        bufferposO=bufferposO-moveB;
        }
                 
        bufferposB=B[counterB];
        if(counterB!=B.size()-1)
        counterB++;
        }
}

time+=timestayO;
fout<<"Case #"<<j+1<<": "<<time<<endl;

}
system("PAUSE");

}
