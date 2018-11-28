#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>

using namespace std;

int main() {
	freopen("number.in","rt",stdin);
	freopen("number.out","wt",stdout);
	int t=0;
	cin >> t;
	int tNum=1;
	while(t-->0){
	string s="";
	cin >> s;
	int n=s.length();
	vector<int> a(n), b(n);
	for(int i=0; i<n; i++) {
		a[i]=s[i]-'0';
		b[i]=a[i];
	}
	next_permutation(a.begin(),a.end());

	int cmp=0;
	for(int i=0; i<n; i++){
		if(a[i]>b[i]){
			cmp=1;
			break;
		}else if(a[i]<b[i]){
			cmp=-1;
			break;
		}
	}
	string s1="";
	if(cmp<=0){
		if(a[0]==0){
			int pos=0;
			int min=10;
			for(int i=0; i<n; i++){
				if(a[i]!=0 && min>a[i]){
					min=a[i];
					pos=i;
				}
			}
			s1+=min+'0';
			s1+='0';
			for(int i=0; i<n; i++){
				if(pos==i) continue;
				s1+=a[i]+'0';
			}
			
		}else{
			s1+=a[0]+'0';
			s1+='0';
			for(int i=1; i<n; i++) s1+=a[i]+'0';
		}
	}else{
		for(int i=0; i<n; i++) s1+=a[i]+'0';
	}
	//cout << s << '\n';
	cout << "Case #";
	cout << tNum;
	cout <<": ";
	tNum++;
	cout << s1 << '\n';
	}
	fclose(stdout);
}