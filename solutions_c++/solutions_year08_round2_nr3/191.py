#include <iostream>
#include <fstream>
using namespace std;

struct carta {
	carta *next,*prev;
	int num;
	carta(carta *aprev, int anum, carta* anext):next(anext),prev(aprev),num(anum){}
};


int main(int argc, char *argv[]) {
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	int cant_cases;
	fin>>cant_cases;
	int idx[120];
	int nums[5010];
	carta *top,*punt, *nueva,*au1,*au2;
	for (int case_number=0;case_number<cant_cases;case_number++) {
		int k;
		fin>>k;
		int ni;
		fin>>ni;
		for (int i=0;i<ni;i++) {
			fin>>idx[i];
		}
		top = punt = new carta(NULL,k,NULL);
		top->next=top;
		top->prev=top;	
		for (int i=k-1;i>0;i--) {
			nueva = new carta(punt->prev,i,punt);
			au1=punt->prev;
			au2=punt;
			au1->next=nueva;
			au2->prev=nueva;
			punt=nueva;
			
			for (int j=1;j<i;j++) {
				punt=punt->prev;
			}
	
		}
		
		for (int i=1;i<=k;i++) {
			nums[i]=punt->num;
			punt=punt->next;
		}
		
		fout<<"Case #"<<case_number+1<<":";
		for (int i=0;i<ni;i++) {
			fout<<" "<<nums[idx[i]];
		}
		fout<<endl;
	}
	fout.close();
	fin.close();
	return 0;
}

