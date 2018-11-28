#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int l,d,n;
vector<string> s(5001);
vector<string> t(16);

inline int saiki(int m,string a,string z){
	int ret=0;
	for(int i=0;i<t[m].size();i++){
		a[m]=t[m][i];
		z[m]=t[m][i];
//	cout << a << endl << z << endl;
		int d=(int)distance(lower_bound(s.begin(),s.end(),a),upper_bound(s.begin(),s.end(),z));
//		cout << *lower_bound(s.begin(),s.end(),a) << "   " << *upper_bound(s.begin(),s.end(),z) << endl;
		if(m==l-1) ret += d;
		else if(d!=0) ret += saiki(m+1,a,z);
	}
	return ret;

}
int main()
{
	cin >> l >> d >> n;
	
	int i,j,k;
	for(i=0;i<d;i++) cin >> s[i];
	sort(s.begin(),s.end());
	
	string c;
	for(i=0;i<n;i++){
		cin >> c;
		int p=0;
		int b=0;
		k=0;
		for(j=0;j<15;j++) t[j].clear();
		while(p!=c.size()){
			if(c[p]=='(') b=1;
			else if(c[p]==')'){
				b=0;
				k++;
			}
			else{
				t[k]+=c[p];
				if(b==0) k++;
			}
			
			p++;
		}
		string a,z;
		for(j=0;j<l;j++){
			a+='a';
			z+='z';
		}
		cout << "Case #" << i+1 << ": " << saiki(0,a,z) << endl;
		
	}
		
	
	
	return 0;
}

