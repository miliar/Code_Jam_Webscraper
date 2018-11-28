#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

fstream fin("B-large.in.txt",ios::in);
fstream fout("B-large.out.txt",ios::out);
struct TRIP{
	int start, end;
};
bool MyCMP(TRIP a, TRIP b) {
	return (a.start < b.start || a.start == b.start && a.end < b.end);
}


int main() {
	TRIP a[200], b[200];
	int tra[200], trb[200];
	int t;
	int lena, lenb;
	int ta, tb;	
	int n, na, nb;
	fin>>n;
	int i,j,hour,min;
	char ch;
	for (int k=1; k<=n; k++) {
		fin>>t>>na>>nb;
		ta = tb = lena = lenb = 0;
		fout<<"Case #"<<k<<": ";
		
		for (i=0; i<na; i++) {
			fin>>hour>>ch>>min;
	//		cout<<hour<<' '<<ch<<' '<<min<<endl;
			a[ta].start = hour*60+min;
			fin>>hour>>ch>>min;
			a[ta].end = hour*60+min;
			ta++;
		}
		for (i=0; i<nb; i++) {
			fin>>hour>>ch>>min;
		//	cout<<hour<<' '<<ch<<' '<<min<<endl;
			b[tb].start = hour*60+min;
			fin>>hour>>ch>>min;
			b[tb].end = hour*60+min;
			tb++;
		}
		sort(a, a+ta,MyCMP);
		sort(b, b+tb,MyCMP);
		int cura(0), curb(0), resa(0), resb(0);
		for (i=0; i<na+nb; i++) {
			if ( cura <na && (curb >=nb || a[cura].start < b[curb].start) ) {
				if ( lena>0  && tra[0] <= a[cura].start ) {
					trb[lenb] = a[cura].end+t;
					lenb++;
					sort(trb,trb+lenb);
					tra[0] = tra[lena-1];
					lena--;
					sort(tra,tra+lena);
				}
				else {
					resa++;
					trb[lenb] = a[cura].end+t;
					lenb++;
					sort(trb,trb+lenb);
				}
				cura++;
			}
			else {
				if ( lenb>0 && trb[0]<=b[curb].start){
					tra[lena] = b[curb].end+t;
					lena++;
					sort(tra,tra+lena);
					trb[0] = trb[lenb-1];
					lenb--;
					sort(trb,trb+lenb);
				}
				else {
					resb++;
					tra[lena] = b[curb].end+t;
					lena++;
					sort(tra,tra+lena);
				}
				curb++;
			}
		}
		fout<<resa<<' '<<resb<<endl;
	}
	return 0;
}