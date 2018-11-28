#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
    int newline=0;
    bool first=true;
    ifstream inFile;
    char  line[5];
    inFile.open("A-small-attempt0.in");
    if (!inFile) {
        cerr << "Unable to open file";
        exit(1);   // call system to stop
    }
    int ca=0;

    inFile >> ca;
  
    for (int i=0;i<ca;i++){  
        
 
        cout<<"Case #"<<i+1<<": ";
        while ( inFile.good() )
		{

        inFile.read (line, 1);
			switch (line[0]) {
				case 'a':
					cout<<"y";//
					break;
				case 'b':
					cout<<"h";//
					break;
				case 'c':
					cout<<"e";//
					break;
				case 'd':
					cout<<"s";//
					break;
				case 'e':
					cout<<"o";//
					break;
				case 'f':
					cout<<"c";//
					break;
				case 'g':
					cout<<"v";//
					break;
                case 'h':
					cout<<"x";//
					break;
				case 'i':
					cout<<"d";//
					break;
				case 'j':
					cout<<"u";//
					break;
				case 'k':
					cout<<"i";//
					break;					
				case 'l':
					cout<<"g";//
					break;
				case 'm':
					cout<<"l";//
					break;
				case 'n':
					cout<<"b";//
					break;
				case 'o':
					cout<<"k";//
					break;
				case 'p':
					cout<<"r";//
					break;
				case 'q':
					cout<<"z";//
					break;
				case 'r':
					cout<<"t";//
					break;
				case 's':
					cout<<"n";//
					break;
                case 't':
					cout<<"w";//
					break;
				case 'u':
					cout<<"j";//
					break;
				case 'v':
					cout<<"p";//
					break;
				case 'w':
					cout<<"f";//
					break;
                case 'x':
					cout<<"m";//
					break;
				case 'y':
					cout<<"a";//
					break;
				case 'z':
					cout<<"q";//
					break;
                case ' ':
					cout<<" ";//
					break;
                case '\n':
					newline=1;//
					break;
				
				default:  cout << "\n";
					break;
			}
            if (newline==1) {
                newline=0;
                if (first) {
                    first=false;
                    continue;
                }
                break;
            }
        }
    
    cout<<"\n";
        }
            
			
		inFile.close();
	
	return 0;
}