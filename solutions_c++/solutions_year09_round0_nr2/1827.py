#include <iostream>
#include <string>
#include <list>

using namespace std;

struct point {
	int x,y;
};
const char* convert(int i) {
	if(i==0) return "a";
	if(i==1) return "b";
	if(i==2) return "c";
	if(i==3) return "d";
	if(i==4) return "e";
	if(i==5) return "f";
	if(i==6) return "g";
	if(i==7) return "h";
	if(i==8) return "i";
	if(i==9) return "j";
	if(i==10) return "k";
	if(i==11) return "l";
	if(i==12) return "m";
	if(i==13) return "n";
	if(i==14) return "o";
	if(i==15) return "p";
	if(i==16) return "q";
	if(i==17) return "r";
	if(i==18) return "s";
	if(i==19) return "t";
	if(i==20) return "u";
	if(i==21) return "v";
	if(i==22) return "w";
	if(i==23) return "x";
	if(i==24) return "y";	
	return "z";
}

int main()
{   int cases_no,height,width; cin >> cases_no;
for(int cases=0; cases<cases_no; cases++) {
	cin >> height; cin >> width;
  	// dynamically allocate twodimensional array of dimensions 
  	// (n+2) x (m+2) to hold the floor plus extra walls around 
  	int** map = new int*[height];
  	for (int r=0; r<height; ++r) map[r] = new int[width]; 

	for(int r=0; r<height; ++r) 
		for(int c=0; c < width; c++) cin >> map[r][c];


	//for(int r=0; r<height; ++r) {
	//	for(int c=0; c < width; c++) cout << map[r][c] << " ";
	//	cout << endl;	
	//} // just to see if everything is still cool.

  	int** sheds = new int*[height];
  	for (int r=0; r<height; ++r) sheds[r] = new int[width]; 

	for(int r=0; r<height; ++r) 
		for(int c=0; c < width; c++) sheds[r][c]=-1;

	list<point> way2sink; int basin=0;
	for(int r=0; r<height; ++r) 
		for(int c=0; c < width; c++) {
		   way2sink.clear();
		   int rr=r, cc=c; point sink; sink.x=rr; sink.y=cc;
		   while(sheds[sink.x][sink.y]==-1) {
		        way2sink.push_back(sink);
			if(rr>0 && map[rr-1][cc]<map[sink.x][sink.y]) {sink.x=rr-1; sink.y=cc;}
			if(cc>0 && map[rr][cc-1] < map[sink.x][sink.y]) {sink.x=rr; sink.y=cc-1;}
			if(cc+1<width && map[rr][cc+1]<map[sink.x][sink.y]) {sink.x=rr; sink.y=cc+1;}
			if(rr+1<height && map[rr+1][cc]<map[sink.x][sink.y]) {sink.x=rr+1; sink.y=cc;} 
			if(sink.x==rr && sink.y==cc) break; else {rr=sink.x; cc=sink.y;}
		   }
		   int mark;
		   if(sheds[sink.x][sink.y]!=-1) mark=sheds[sink.x][sink.y]; else mark=basin++;
		   for(list<point>::iterator it=way2sink.begin(); it!=way2sink.end(); it++) { 
			//cout << (*it).x << "," << (*it).y << "; ";
			sheds[(*it).x][(*it).y]=mark; }
		   //cout << endl << "Sheds:"<<endl;

		//for(int r=0; r<height; ++r) {
		//for(int c=0; c < width; c++) cout << sheds[r][c] << " ";
		//cout << endl;	
		//} // just to see if everything is still cool.
		    
		}
	cout << "Case #" << cases+1 << ":\n";
	for(int r=0; r<height; ++r) {
	   for(int c=0; c < width; c++) cout << convert(sheds[r][c]) << " ";
		cout << endl;	
	} 

  	// delete dynamically allocated arrays
  	for (int r=0; r<height; ++r) delete[] map[r];
	delete[] map;

  	for (int r=0; r<height; ++r) delete[] sheds[r];
	delete[] sheds;
}

return 0;
}
