#include<iostream>
using namespace std;

int n;
int qq , ss;
string q[1001];
string s[101];

long long mat[1001][101];

long long get(int qi , int si){
	if(qi >= qq) return 0;
	if(mat[qi][si]!=-1)
		return mat[qi][si]; 
	long long m = (long long)1e18;
	bool is = (s[si] == q[qi]);
	if(!is) m = min(m , get(qi+1 , si));
	for(int i = 0 ; i<ss ; i++){
		if(i == si) continue;
		long long ll ;
		if(is)
			ll=1+get(qi , i);
		else
			ll=1+get(qi+1 , i);
		m = min(m , ll);
	}
	return mat[qi][si] = m;
}

int main(){
	freopen("A-large.in" , "rt" , stdin);
	freopen("1.out" , "wt" , stdout);
	cin>>n;
	string str;
	for(int i = 1 ; i<= n ; i++){
		cin>>ss;getline(cin , str);
		for(int j = 0 ; j< ss; j++){
			getline(cin , s[j]);
		}
		cin>>qq;getline(cin , str);
		for(int j = 0 ; j< qq; j++){
			getline(cin , q[j]);
		}
		long long m = (long long)1e18;
		memset(mat , -1 , sizeof mat);
		for(int j = 0 ; j< ss ; j++){
			m = min(m , get(0  , j));
		}
		cout<<"Case #"<<i<<": "<<m<<endl;
	}
	return 0;
}
