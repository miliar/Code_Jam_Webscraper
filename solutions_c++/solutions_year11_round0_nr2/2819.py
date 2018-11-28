#include<fstream>
#include<cmath>
#include<cstring>
using namespace std;
char q[100],s[100];
char op[26][27];
char co[26][26];
int hash[26];
int n,h,l;
int c2i(char c){
	return c-'A';
}
char i2c(int i){
	return 'A'+i;
}
void clear() {
	h=l;
	int j,k;
	for (j=0;j<26;j++) 
		hash[j]=0;
	return;
}
bool chkh(int is) {
	int i,j;
	for (i=0;i<strlen(op[is]);i++) {
		if (hash[c2i(op[is][i])]) 
			return true;
	}
	return false;
}
void cas(char* s,char c) {
	int i=strlen(s);
	s[i]=c;
	s[i+1]='\0';
	return;
}
	
int main() {
	ifstream fin("B.in");
	ofstream fout("B.out");
	int t,c,d,i,j,k,iq,is;
	char cr[4];
	fin>>t;
	for(i=0;i<t;i++) {
		l=0;  //[)
		clear();
		for (j=0;j<26;j++) {
			for (k=0;k<26;k++) 
				 co[j][k]='\0';
			op[j][0]='\0';
			}
		fin>>c;
		for(j=0;j<c;j++){
			fin>>cr;
			co[c2i(cr[0])][c2i(cr[1])]=cr[2];
			co[c2i(cr[1])][c2i(cr[0])]=cr[2];
		}
		fin>>d;
		for(j=0;j<d;j++){
			fin>>cr;
			cas(op[c2i(cr[0])],cr[1]);
			cas(op[c2i(cr[1])],cr[0]);
		}
		fin>>n;
		fin>>s;
		for(j=0;j<n;j++) {
			iq=(l>h?c2i(q[l-1]):-1);
			is=c2i(s[j]);
			if (iq>=0&&co[iq][is]) {
				hash[iq]--;
				q[l-1]=co[iq][is];
				continue;
			}
			if (chkh(is)) {
				clear();
				continue;
			}
			q[l++]=s[j];
			hash[is]++;
		}
		fout<<"Case #"<<i+1<<": [";
		for (j=h;j<l;j++) {
			if (j!=h)
				fout<<", ";
			fout<<q[j];
		}
		fout<<"]"<<endl;
	}
	fin.close();
	fout.close();
	return 0;
	}
			
		
