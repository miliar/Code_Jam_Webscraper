#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
ifstream fi("Asmallw.in");
ofstream fo("Asmall.out");
int i,n,c,j;
vector<string> phrases;
vector<int> lens;
string temp;
char line[101];
fi >> n;
fi.getline(line,101);

for(j=0;j<n;++j)
{

fi.getline(line,101);
// cout << line << endl;
i=0;
fo << "Case #" << j+1 << ": ";
while(line[i] != '\0')
{
if(line[i] == ' '){fo << " ";}
if(line[i] == 'a'){fo << "y";}
if(line[i] == 'b'){fo << "h";}
if(line[i] == 'c'){fo << "e";}
if(line[i] == 'd'){fo << "s";}
if(line[i] == 'e'){fo << "o";}
if(line[i] == 'f'){fo << "c";}
if(line[i] == 'g'){fo << "v";}
if(line[i] == 'h'){fo << "x";}
if(line[i] == 'i'){fo << "d";}
if(line[i] == 'j'){fo << "u";}
if(line[i] == 'k'){fo << "i";}
if(line[i] == 'l'){fo << "g";}
if(line[i] == 'm'){fo << "l";}
if(line[i] == 'n'){fo << "b";}
if(line[i] == 'o'){fo << "k";}
if(line[i] == 'p'){fo << "r";}
if(line[i] == 'q'){fo << "z";}
if(line[i] == 'r'){fo << "t";}
if(line[i] == 's'){fo << "n";}
if(line[i] == 't'){fo << "w";}
if(line[i] == 'u'){fo << "j";}
if(line[i] == 'v'){fo << "p";}
if(line[i] == 'w'){fo << "f";}
if(line[i] == 'x'){fo << "m";}
if(line[i] == 'y'){fo << "a";}
if(line[i] == 'z'){fo << "q";}
++i;
}
fo << endl;
}


return 0;
}