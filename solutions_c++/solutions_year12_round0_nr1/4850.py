#include <iostream>

using namespace std;

int main(){
	int number;
	cin >> number;
		string buf;
		getline(cin, buf);
	for(int i=1; i<=number; i++){
		getline(cin, buf);
		for(int j=0; j<buf.size();j++){
			switch(buf[j]){
				case 'a':buf[j]='y';break;
				case 'b':buf[j]='h';break;
				case 'c':buf[j]='e';break;
				case 'd':buf[j]='s';break;
				case 'e':buf[j]='o';break;
				case 'f':buf[j]='c';break;
				case 'g':buf[j]='v';break;
				case 'h':buf[j]='x';break;
				case 'i':buf[j]='d';break;
				case 'j':buf[j]='u';break;
				case 'k':buf[j]='i';break;
				case 'l':buf[j]='g';break;
				case 'm':buf[j]='l';break;
				case 'n':buf[j]='b';break;
				case 'o':buf[j]='k';break;
				case 'p':buf[j]='r';break;
				case 'q':buf[j]='z';break;
				case 'r':buf[j]='t';break;
				case 's':buf[j]='n';break;
				case 't':buf[j]='w';break;
				case 'u':buf[j]='j';break;
				case 'v':buf[j]='p';break;
				case 'w':buf[j]='f';break;
				case 'x':buf[j]='m';break;
				case 'y':buf[j]='a';break;
				case 'z':buf[j]='q';break;
			}
		}
		cout << "Case #" << i << ": " << buf << endl;
	}
}