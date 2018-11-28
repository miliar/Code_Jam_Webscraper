#include <iostream>
#include <fstream>
using namespace std;
int calcSmallerPerm(int i, int l, int h, int i1, int x);
bool exists(int j,int* a, int asize);
int recPairs(int l, int h);

int main(){
	int l=0;
	int h=0;
	int r=0;
	
	ifstream fi;
	fi.open("C-large.in");
	
	ofstream fo;
	fo.open("outfile_large.out");
	
	int caseNo = 1;
	
	while(fi.good()){
		int t = 0;
		fi>>t;
		if(t<=0)return 1;
		for(int i=0; i<t; i++){
		fi>>l>>h;
		
		if(l>h)continue;
		
		r = recPairs(l, h);
		fo<<"Case #"<<caseNo<<": "<<r<<endl;
		caseNo++;
		//cout<<"\nl="<<l<<"  h="<<h;
		}
	}
	
	fi.close();
	fo.close();
	
	//r = recPairs(l, h);
	//cout<<"\n r="<<r<<endl;
	
	return 0;
}


int recPairs(int l, int h){
	if(l>h){cout<<"\nInvalid range\n";return 1;}
	
	int t = 0;
	int x = 1;
	int i1=0;			//No of digits
	for(; i1<50; i1++){
		t = l%x;
		if(t == l)break;
		x = x*10;
	}
	
	int smallerPerm=0;
	int tot = 0;
	for(int i=l; i<=h; i++){
		smallerPerm = calcSmallerPerm(i, l, h, i1, x);
		tot = tot + smallerPerm;
	}
	
	return tot;
}

int calcSmallerPerm(int i, int l, int h, int i1, int x) {
	int* a;
	int ir, il;
	
	a = new int[i1];
	for(int k=0; k<i1; k++)a[k] = 0;
	
	int cnt=0;
	int j = i;
	
	x = x/10;
	
	for(int i2=0; i2<i1; i2++){
		
		ir = j%10;
		j = j/10;
		j = ir*x + j;
		//cout<<"\nj="<<j;
		if(j<l || j>h)continue;
		if(exists(j,a, i1))continue;
		
		if(j>i){
			//cout<<"\ni="<<i<<"  j="<<j;
			cnt++;
			a[i2] = j;
		}
		
	}
	//if(cnt!=0)cout<<"  cnt="<<cnt;
	return cnt;
	
}

bool exists(int j,int* a, int asize){
	if(a==NULL)return false;
	for(int k=0; k<asize; k++){
		if(a[k]==j){
		return true;
		}
	}
	return false;
}

