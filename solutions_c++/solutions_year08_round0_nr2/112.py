#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int n;
	char saux[101];
	int sa[3000],sb[3000],la[3000],lb[3000];
	fin>>n;
	for (int i=0;i<n;i++) {
		
		int t,na,nb;
		fin>>t>>na>>nb;
		fin.ignore(255,'\n');
		for (int j=0;j<1500;j++) {
			sa[j]=sb[j]=la[j]=lb[j]=0;
		}
		for (int j=0;j<na;j++) {
			fin.getline(saux,100,'\n');
			sa[ ( (saux[0]-'0')*10+(saux[1]-'0') )*60 + (saux[3]-'0')*10+(saux[4]-'0') ]++;
			lb[ ( (saux[6]-'0')*10+(saux[7]-'0') )*60 + (saux[9]-'0')*10+(saux[10]-'0') +t ]++;
		}
		for (int j=0;j<nb;j++) {
			fin.getline(saux,100,'\n');
			sb[ ( (saux[0]-'0')*10+(saux[1]-'0') )*60 + (saux[3]-'0')*10+(saux[4]-'0') ]++;
			la[ ( (saux[6]-'0')*10+(saux[7]-'0') )*60 + (saux[9]-'0')*10+(saux[10]-'0') +t ]++;
		}
		
		int ta=0,tb=0,ra=0,rb=0;
		
		for (int j=0;j<1440;j++) {
			ta+=la[j];
			tb+=lb[j];
			ta-=sa[j];
			if (ta<0) {
				ra+=-ta;
				ta=0;
			}
			tb-=sb[j];
			if (tb<0) {
				rb+=-tb;
				tb=0;
			}

		}
		
		fout<<"Case #"<<i+1<<": "<<ra<<" "<<rb<<endl;
	
	}
	fout.close();
	fin.close();
	return 0;
}

