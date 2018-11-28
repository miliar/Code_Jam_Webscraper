#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int l,n,d;
	fin>>l>>d>>n;
	fin.ignore(255,'\n');
	char temp[1024];
	char dict[5001][30];
	bool can_not_be[5001];
	for (int i=0;i<d;i++)
		fin.getline(dict[i],30);
	
	for (int i=0;i<n;i++) {
		memset(can_not_be,0,sizeof(can_not_be));
		fin.getline(temp,1024);
		int p=0;
		char *c=temp,*c2,*c3,c4;
		while (*c!='\0') {
			if (*c=='(') {
				c2=++c;
				while (*c2!=')') c2++;
				for (int j=0;j<d;j++) {
					c4=dict[j][p];
					for (c3=c;c3<c2;c3++)
						if (*c3==c4) break;
					if (c3==c2) can_not_be[j]=true;
				}
				c=c2;
			} else {
				for (int j=0;j<d;j++) 
					if (dict[j][p]!=*c) 
						can_not_be[j]=true;
			}
			c++;
			p++;
		}
		int res=0;
		for (int j=0;j<d;j++) if (!can_not_be[j]) res++;
		fout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	fout.close();
	fin.close();
}
