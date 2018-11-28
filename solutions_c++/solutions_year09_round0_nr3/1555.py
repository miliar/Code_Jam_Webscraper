#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <fstream>
using namespace std;

#define  DEBUG

class LastFour
{
public:
int digit[4];

LastFour(){
	for (int i = 0; i < 4; i++)	{
		digit[i] = 0;
	}
}

LastFour(int ini[]){
	for (int i = 0; i < 4; i++)	{
		digit[i] = ini[i];
	}
}

void setDigit(int val[]){
	for (int i = 0; i < 4; i++)	{
		digit[i] = val[i];
	}
}

void setDigit(const LastFour& lf){
	for (int i = 0; i < 4; i++)	{
		digit[i] = lf.digit[i];
	}
}
// friend ostream&
// 	operator<<(ostream& os, const LastFour& lf);
// friend const LastFour
// 	operator+(const LastFour& left, const LastFour& right);
};

void print(ostream& os, const LastFour& lf){
	os << lf.digit[0];
	for (int i = 1; i < 4; i++)	{
		os << lf.digit[i];
	}
	os << endl;
}

LastFour add(const LastFour& left, const LastFour& right){
	int ar[4];
	int i;
	for (i = 0; i < 4; i++)	{
		ar[i] = left.digit[i] + right.digit[i];
	}
	for (i = 3; i > 0; i--) {
		if (ar[i] >= 10) {
			ar[i-1] += ar[i]/10;
			ar[i] = ar[i]%10;
		}
	}
	if (ar[0] >= 10) {
		ar[i] = ar[i]%10;
	}
	return LastFour(ar);
}

int main(){
	filebuf ifb;
	ifb.open ("C-large.in",ios::in);
	istream min(&ifb);
	//istream min(cin);
	
	filebuf ofb;
	ofb.open ("C-large.out.txt",ios::out);
	ostream mout(&ofb);
	
	int n;
	min >> n;
	string temp("welcome to code jam");
	string line;
	getline(min,line);
	int i, j, k;
	int a1[] = {0,0,0,1};
	LastFour lf1(a1);
	for (i = 0; i < n; i++){
		getline(min,line);
#ifdef DEBUG
		//mout << "line:" << line << endl;
#endif
		int len = line.size();
		vector<LastFour> keep(len,LastFour());
		for (j = 0; j < len; j++){
	
			if (line[j] == 'w') {
				keep[j].setDigit(a1);
			}//if
		}//for
		for (j = 1; j < temp.size(); j++) {
			LastFour acc;
			for (k = 0; k < len; k++) {
				if (line[k] == temp[j-1]) {
					acc = add(acc, keep[k]);
				}
				else if (line[k] == temp[j]) {
					keep[k].setDigit(acc);
				}
			}
		}
		LastFour res;
		for (j = 0; j < len; j++){
			if (line[j] == temp[temp.size()-1]) {
				res.setDigit(add(res,keep[j]));
			}//if
		}//for
		mout << "Case #" << i+1 << ": ";
		print(mout, res);
	}//for
// 	int a1[] = {0,6,7,1};
// 	int a2[] = {2,3,8,3};
// 	LastFour lf1(a1);
// 	LastFour lf2(a2);
// 	LastFour lf3 = add(lf1,lf2);
// 	print(cout,lf3);
	ifb.close();
	ofb.close();
	return 0;
}

