#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int t1,u,min,c,i,j,k,p[20];
	char last;
	string s,t;
	cin>>t1;
	for (u=0; u<t1; u++){
		cin>>k>>s;
		for (i=0; i<k; i++)
			p[i]=i;
		min=100000000;
		do{
			t="";
			for (i=0; i<s.length(); i+=k){
				for (j=0; j<k; j++)
					t+=s[i+p[j]];
			}
			last=t[0];
			c=1;
			for (i=1; i<t.length(); i++){
				if (last!=t[i]){
					last=t[i];
					c++;
				}
			}
			if (c<min)
				min=c;
		} while(next_permutation(p,p+k));
		cout<<"Case #"<<(u+1)<<": "<<min<<endl;
	}
	return 0;
}
