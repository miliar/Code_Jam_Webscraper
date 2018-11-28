#include<iostream>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

int a[40][40];
vector<vector<int> > d;
vector<int> ans;
vector<int> pred;
vector<int> last;

void add(int k){
	if(ans.size()==0){
		ans.push_back(k);
		last[k]=0;
		pred.push_back(-1);
		return;
	}
	int n=ans.size();
	int p=ans[n-1];
	if(a[p][k]!=-1){
		last[p]=pred[n-1];
		ans.pop_back();
		pred.pop_back();
		add(a[k][p]);
	}
	else{
		int f=0;
		for(int i=0;i<d[k].size();i++){
			if(last[d[k][i]]!=-1){
				f=1;
				break;
			}
		}
		if(f==1){
			last.assign(40,-1);
			ans.clear();
			pred.clear();
			return;
		}
		ans.push_back(k);
		pred.push_back(last[k]);
		last[k]=n;
	}
}

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	cin >> T;
	for(int q=0;q<T;q++){
		memset(a,-1,sizeof a);
		int n;
		cin >> n;
		for(int i=0;i<n;i++){
			string s;
			cin >> s;
			a[s[0]-'A'][s[1]-'A']=a[s[1]-'A'][s[0]-'A']=s[2]-'A';
		}
		cin >> n;
		d.clear();
		d.resize(40);
		for(int i=0;i<n;i++){
			string s;
			cin >> s;
			d[s[0]-'A'].push_back(s[1]-'A');
			d[s[1]-'A'].push_back(s[0]-'A');
		}
		cin >> n;
		string s;
		cin >> s;
		last.assign(40,-1);
		ans.clear();
		pred.clear();
		for(int i=0;i<n;i++){
			int k=s[i]-'A';
			add(k);
		}
		cout << "Case #" << q+1 << ": [";
		for(int i=0;i<ans.size();i++){
			if(i!=0){
				cout << ", ";
			}
			cout << char(ans[i]+'A');
		}
		cout << "]\n";
	}
	return 0;
}
