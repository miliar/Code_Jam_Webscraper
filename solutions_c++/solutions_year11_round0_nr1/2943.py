#include<fstream>
#include<cmath>
#include<cstring>
#include "general.h"
using namespace std;
struct tsk{
	int type,time,prior;
};
int main(){
	ifstream fin("A.in");
	ofstream fout("A.out");
	int t,n,i,j,k;
	char rc;
	int rp,mintime;
	tsk nt,n1,n2;
	fin>>t;
	for (k=0;k<t;k++){
		fout<<"Case #"<<k+1<<": ";
		fin>>n;
		List<tsk> s1,s2;
		Queue<tsk> ro(s1),rb(s2);
		int curPr=0,curT=0;
		int po=1,pb=1;
		for (i=0;i<n;i++){
			fin>>rc>>rp;
			nt.type=0;
			nt.prior=0;
			if (rc=='O') {
				nt.time=abs(po-rp);
				ro.pushTail(nt);
				po=rp;
			}
			else {
				nt.time=abs(pb-rp);
				rb.pushTail(nt);
				pb=rp;
			}
			nt.type=1;
			nt.prior=i;
			nt.time=1;
			if (rc=='O') 
				ro.pushTail(nt);
			else 
				rb.pushTail(nt);
			}
		while (ro.getLength()||rb.getLength()) {
			if (ro.getLength())
				n1=ro.getFirst();
			if (rb.getLength())
				n2=rb.getFirst();
			mintime=100000;
			if (ro.getLength()&&n1.prior<=curPr) 
				mintime=n1.time;
			if (rb.getLength()&&n2.prior<=curPr) 
				mintime=min(mintime,n2.time);
			curT+=mintime; //一定会有 
			j=curPr;
			if (ro.getLength()&&n1.prior<=j)
				if (!(ro.getFirst().time-=mintime)) {
					if (n1.type) 
						curPr++;
					ro.popFirst();
				}
			if (rb.getLength()&&n2.prior<=j)
				if (!(rb.getFirst().time-=mintime)) {
					if (n2.type) 
						curPr++;
					rb.popFirst();
				}
		}
		fout<<curT<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
			
