#include <iostream>
#include <cmath>
#include <string>

#define NAME "file"
using namespace std;
int test;
string ss;
char s[100];
int c[100];
int num[100];

int find(char cc){
	for (int i=1;i<=s[0];i++){
		if (s[i]==cc) return c[i];
	}
	return -1;
}

int main(void){
	freopen(NAME".in","r",stdin);
	freopen(NAME".out","w",stdout);
	scanf("%i\n",&test);
	for (int z=0;z<test;z++){
		getline(cin,ss);
		int cur=0;
		s[0]=0;
		for (int i=0;i<ss.size();i++){
			if (i==0){
				s[0]=1;
				s[s[0]]=ss[0];
				c[s[0]]=1;
				num[0]=1;
			}else{
				int fin=find(ss[i]);
				if (fin==-1){
					s[0]++;
					s[s[0]]=ss[i];
					c[s[0]]=cur;
					num[i]=cur;
					if (cur==0) cur+=2;
					else cur++;
					
				}else num[i]=fin;
			}
		}
		int base=cur;
		if (base<2) base=2;
		long long res=0;
		
		for (int i=0;i<ss.size();i++){
			res=res*base+num[i];
		}
		
		printf("Case #%i: ",z+1);
		cout<<res<<endl;
	}

	return 0;
}