#include<windows.h>
#include<math.h>
#include<string>
#include<strstream>
#include<iomanip>
#include<iostream>
#include<fstream>

int max_line;
const int MAXBUF=1000;
char buf[MAXBUF];
const int PATLINE=19;
char* A="welcome to code jam";

long inside(int x, int y, int z){ long count=0;
	for(; x<z+y; x++)
		A[y] == buf[x] ? (y<PATLINE-1 ? count+=inside(x+1, y+1, z) : count++) :0;
	return count;
	}

int WINAPI WinMain(
    HANDLE hinst,      HANDLE hPrevInstance,
    LPSTR  lpCmdLine,  int    nCmdShow){/*+++*/MSG msg;
using namespace std;
fstream in("C-small.in");//C-large.in");//
fstream out("C-small.out");//C-large.out");//
int N=0; in >> N; in.getline(buf, MAXBUF, '\n');
for(short i=0;i<N;i++){
	in.getline(buf, MAXBUF, '\n'); max_line=strlen(buf);
	sprintf(buf, "%04ld", max_line<PATLINE ? 0: inside(0,0,max_line-PATLINE+1) );
	out << "Case #" << i << ": " << buf+strlen(buf)-4 << endl;
	}

return 0;
}