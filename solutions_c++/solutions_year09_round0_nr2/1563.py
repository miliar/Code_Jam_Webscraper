#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <fstream>
using namespace std;
vector<vector<int> > *palti;
vector<vector<int> > *pconn;
vector<vector<int> > *pdb;
int h, w, index;
//#define  DEBUG

int direction[] = {1, 2, 4, 3};

void flow(int r, int c, int cdb){
	if((*pdb)[r][c] == -1){
		if (cdb == -1){
#ifdef DEBUG
			mout << "set (" << r << "," << c << ") = " << index << endl;; 
#endif
			(*pdb)[r][c] = index;
			index++;
		}
		else{
#ifdef DEBUG
			mout << "set (" << r << "," << c << ") = " << cdb << endl;; 
#endif
			(*pdb)[r][c] = cdb;
		}
		if ((*pconn)[r][c] != -1) {//flow to a point
			switch ((*pconn)[r][c])
			{
			case 1:
				flow(r-1, c, (*pdb)[r][c]);
				break;
			case 2:
				flow(r, c-1, (*pdb)[r][c]);
				break;
			case 3:
				flow(r, c+1, (*pdb)[r][c]);
				break;
			case 4:
				flow(r+1, c, (*pdb)[r][c]);
				break;
			}
		}
		for(int i = 1; i <= 4; i ++){
			int xm = r;
			int ym = c;
			if(i%2 == 1){
				xm += i - 2;
			}
			else{
				ym += i - 3;
			}
			if((xm >= 0) && (xm < h) && (ym >= 0) && (ym < w)){//in boundary
				switch (i)
				{
				case 1:
					if((*pconn)[xm][ym] == 4){//a point flow to it
						flow(r-1, c, (*pdb)[r][c]);
					}
					break;
				case 2:
					if((*pconn)[xm][ym] == 3){//a point flow to it
						flow(r, c-1, (*pdb)[r][c]);
					}
					break;
				case 3:
					if((*pconn)[xm][ym] == 1){//a point flow to it
						flow(r+1, c, (*pdb)[r][c]);
					}
					break;
				case 4:
					if((*pconn)[xm][ym] == 2){//a point flow to it
						flow(r, c+1, (*pdb)[r][c]);
					}
					break;
				}
				
			}
		}
	}
}


void connect(){
	int j, k;
	for (j = 0; j < h; j++){
		for (k = 0; k < w; k++){
			int r = j;
			int c = k;
			int mx = r;
			int my = c;
			for(int i = 0; i < 4; i ++){
				int t = direction[i];
				int xm = r;
				int ym = c;
				if(t%2 == 1){
					xm += t - 2;
				}
				else{
					ym += t - 3;
				}
#ifdef DEBUG
				mout << "i=" << i << " (" << xm << "," << ym << ")" << endl;
				mout << " t=" << t << endl;
#endif
				if((xm >= 0) && (xm < h) && (ym >= 0) && (ym < w)){//in boundary
#ifdef DEBUG
					mout << " (" << xm << "," << ym << ")=" << (*palti)[xm][ym] << " (" << mx << "," << my << ")=" << (*palti)[mx][my] << endl;
#endif
					
					if((*palti)[xm][ym] < (*palti)[mx][my]){//neighbor should be lowest and follow direction
#ifdef DEBUG
						mout << " (" << xm << "," << ym << ") is lower than (" << mx << "," << my << ")" << endl;
						mout << " set (" << r << "," << c << ") = " << i+1 << endl;; 
#endif
						mx = xm;
						my = ym;
						(*pconn)[r][c] = i+1;
					}
				}
			}
		}//column
	}//row
	
}



int main(){
	filebuf ifb;
	//ifb.open ("A-large.in",ios::in);
	ifb.open ("B-large.in",ios::in);
	istream min(&ifb);
	//istream min(cin);
	
	filebuf ofb;
	ofb.open ("B-large.out.txt",ios::out);
	ostream mout(&ofb);
	
	int t;
	min >> t;
	
	int i, j, k;
	for(i = 0; i < t; i++){
		index = 0;
		min >> h >> w;
		vector<vector<int> > alti(h, vector<int>(w,0));
		vector<vector<int> > conn(h, vector<int>(w,-1));
		vector<vector<int> > db(h, vector<int>(w,-1));
		palti = &alti;
		pconn = &conn;
		pdb = &db;
		for (j = 0; j < h; j++){
			for (k = 0; k < w; k++){
				min >> alti[j][k];
			}//column
		}//row
		
 		connect();
	
		mout << "Case #" << i+1 << ":\n";
#ifdef DEBUG
		for (j = 0; j < h; j++){
			mout << conn[j][0];
			for (k = 1; k < w; k++){
				mout << " " << conn[j][k];
			}//column
			mout << endl;
		}//row
#endif
		
		for (j = 0; j < h; j++){
			for (k = 0; k < w; k++){
				flow(j,k,-1);
			}//column
		}//row
		for (j = 0; j < h; j++){
 			char t = 'a' + db[j][0];
 			mout << t;
//			mout << db[j][0];
			for (k = 1; k < w; k++){
 				t = 'a' + db[j][k];
 				mout << " " << t;
//				mout << db[j][k];
			}//column
			mout << endl;
		}//row
		
	}
	ifb.close();
	ofb.close();
	return 0;
}

