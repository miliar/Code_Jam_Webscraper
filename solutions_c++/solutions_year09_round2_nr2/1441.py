#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector <int> inttovec(int n){
	vector <int> r;
	while (n>0){
		r.push_back(n%10);
		n/=10;
	}
	reverse(r.begin(),r.end());
	return r;
}

void writerez(vector <int> r){
	int a=0;
	for (int i=0;i<r.size();i++){
		a*=10;
		a+=r[i];
	}
	printf("%d\n",a);
}

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	int n;
	bool b=true;
	vector <int> v;
	for (int y=0;y<t;y++){
		printf("Case #%d: ",y+1);
		scanf("%d\n",&n);
		v=inttovec(n);
		for (int i=0;i<v.size()-1;i++){
			if (v[i]>v[i+1] && v[i+1]!=0) b=false;
		}
		if (next_permutation(v.begin(),v.end())) ; else v.insert(v.begin()+1,0);
		if (v[0]==0){
			int j=1;
			while (v[j]==0 && j<n){
				j++;
			}
			swap(v[0],v[j]);
		}
		writerez(v);
		b=true;
	}
	return 0;
}