#include <iostream>
#include <fstream>

using namespace std;

#define to_time(s) (((s[0]-'0')*10+s[1]-'0')*60 + (s[3]-'0')*10+s[4]-'0')

typedef struct {
	unsigned char sA; unsigned char sB; unsigned char eA; unsigned char eB;
} nums;

void st_trains(nums * tl, int & sa, int & sb) {
	int ca = 0, cb = 0;
	for (int i=0; i<24*60; i++) {
		ca += tl[i].eB - tl[i].sA;
		cb += tl[i].eA - tl[i].sB;
		if (ca < 0) {
			sa -= ca;	ca = 0;
		}
		if (cb < 0) {
			sb -= cb;	cb = 0;
		}
	}
}

int main (int argc, char * argv[]) {
	char fn[100];

	int cases;

	if (argc < 2)
		return 1;

	sprintf(fn,"%s.in",argv[1]);
	ifstream fin(fn);
	sprintf(fn,"%s.out",argv[1]);
	ofstream fout(fn);

	fin >> cases;

	nums * tl = new nums[25*60];
	for (int i=1; i<=cases; i++) {
		int t,na,nb,a=0, b=0;
		int h,m;
		fin >> t >> na >> nb;
		memset(tl, 0, sizeof(nums)*25*60);
		char tmp[10];
		for (int j=0; j<na+nb; j++) {
			fin >> tmp;	j<na ? tl[to_time(tmp)].sA++ 	: tl[to_time(tmp)].sB++;
			fin >> tmp;	j<na ? tl[to_time(tmp)+t].eA++ 	: tl[to_time(tmp)+t].eB++;
		}
		st_trains(tl, a,b);
		fout << "Case #" << i <<": " << a << " " << b << endl;
	}
	delete [] tl;

	fin.close();
	fout.close();
	
	return 0;
}
