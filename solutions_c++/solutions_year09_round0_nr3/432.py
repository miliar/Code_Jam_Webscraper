#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	int n;
	fin>>n;
	fin.ignore(255,'\n');
	char temp[1024];
	unsigned long long l[19];
	for (int i=0;i<n;i++) {
		fin.getline(temp,1024);
		for (int k=0;k<19;k++) l[k]=0;
		char *r=temp;
		int p=0;
		while (*r!='\0') {
			p++;
			if (*r=='w') l[0]++;
			if (*r=='e') l[1]+=l[0];
			if (*r=='l') l[2]+=l[1];
			if (*r=='c') l[3]+=l[2];
			if (*r=='o') l[4]+=l[3];
			if (*r=='m') l[5]+=l[4];
			if (*r=='e') l[6]+=l[5];
			if (*r==' ') l[7]+=l[6];
			if (*r=='t') l[8]+=l[7];
			if (*r=='o') l[9]+=l[8];
			if (*r==' ') l[10]+=l[9];
			if (*r=='c') l[11]+=l[10];
			if (*r=='o') l[12]+=l[11];
			if (*r=='d') l[13]+=l[12];
			if (*r=='e') l[14]+=l[13];
			if (*r==' ') l[15]+=l[14];
			if (*r=='j') l[16]+=l[15];
			if (*r=='a') l[17]+=l[16];
			if (*r=='m') l[18]+=l[17];
			for (int k=0;k<19;k++) l[k]=l[k]%10000;
			r++;
		}
		
		fout<<"Case #"<<i+1<<": "<<setw(4)<<setfill('0')<<right<<(l[18]%10000)<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}

