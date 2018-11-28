#include <fstream>
#include <string>

using namespace std;
ifstream fin("C-small.in");
ofstream fout("C-small.out");
const int MNAX=500;
const char s2[19]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
char s1[MNAX+2];	
int ans,l1,l2=19;

string Res(int k){
	string s="";
	char ch[10];
	itoa(k%10000,ch,10);
	int i=0;
	while (i<10 && ch[i]!='\0'){
		s+=ch[i];
		++i;
	}
	while (s.length()<4){s='0'+s;}
	return s;
}

int main(){
	int a[MNAX+2][21];
	int t,test,i,j;
	fin>>test;
	fin.getline(s1,255);

	for (t=1;t<=test;++t){
		memset(a,0,sizeof(int)*(MNAX+2)*21);
		ans=0; l1=0;
		fin.getline(s1,255);
		while (s1[l1]!='\0'){++l1;}

		for (i=0;i<l1;++i){
			if (i>0) a[i][0]=a[i-1][0];
			if (s1[i]==s2[0]){
				++a[i][0];
			}
			a[i][0]%=10000;
		}

		int last=0;
		for (j=1;j<l2;++j){
			for (i=0;i<l1;++i){
				if (i>0) a[i][j]=a[i-1][j];
				if (s1[i]==s2[j]){
					a[i][j]+=a[i][j-1];
					a[i][j]%=10000;
				}
			}
		}


		fout<<"Case #"<<t<<": "<<Res(a[l1-1][l2-1])<<"\n";
	}
	return 0;
}