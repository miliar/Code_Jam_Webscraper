#include<iostream>
#include <cstdlib>
using namespace std;
#include <fstream>




int main(int argc, char** argv) {

    int k, n;
    char *buffer;
    buffer = new char[102];
    ifstream in;
    ofstream out;
    in.open("A-small-attempt0.in", ios_base::in);
    out.open("output.txt", ios_base::out);
    
    
    if (in && out) {
        int **array;

        in.getline(buffer,101,'\n');
        cout<<buffer<<endl;
        //# cases
        k = atoi(buffer);
        for (int j = 0; j < k; j++) {
            in.getline(buffer,101,'\n');
            cout<<buffer<<endl;
            char a=buffer[0];
            for(int i=0;a!='\0';i++){
				switch (a){
					case 'a': 
						buffer[i]='y';
						break;
					case 'b': 
						buffer[i]='h';
						break;
					case 'c': 
						buffer[i]='e';
						break;
					case 'd': 
						buffer[i]='s';
						break;
					case 'e': 
						buffer[i]='o';
						break;
					case 'f': 
						buffer[i]='c';
						break;
					case 'g': 
						buffer[i]='v';
						break;
					case 'h': 
						buffer[i]='x';
						break;
					case 'i': 
						buffer[i]='d';
						break;
					case 'j': 
						buffer[i]='u';
						break;
					case 'k': 
						buffer[i]='i';
						break;
					case 'l': 
						buffer[i]='g';
						break;
					case 'm': 
						buffer[i]='l';
						break;
					case 'n': 
						buffer[i]='b';
						break;
					case 'o': 
						buffer[i]='k';
						break;
					case 'p': 
						buffer[i]='r';
						break;
					case 'q': 
						buffer[i]='z';
						break;
					case 'r': 
						buffer[i]='t';
						break;
					case 's': 
						buffer[i]='n';
						break;
					case 't': 
						buffer[i]='w';
						break;
					case 'u': 
						buffer[i]='j';
						break;
					case 'v': 
						buffer[i]='p';
						break;
					case 'w': 
						buffer[i]='f';
						break;
					case 'x': 
						buffer[i]='m';
						break;
					case 'y': 
						buffer[i]='a';
						break;
					case 'z': 
						buffer[i]='q';
						break;
				}
				a=buffer[i+1];
            }
            out<<"Case #"<<j+1<<": "<<buffer<<endl;            
        }
		
    }
    in.close();
    out.close();
    system("Pause");
}
