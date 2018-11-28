#include<iostream>
#include<fstream>
#include<string>
using namespace std;

const int MAXV = 99999999;

int T, K;
string cc;
int F[1000][130];
int p[200][6];
int pt[6];
bool cover[20];
int tot;

void _find(int dep){
	if (dep == K){
		for (int i=0;i<K;++i)
			p[tot][i] = pt[i];
		tot++;
		return;
	}
	
	for (int i=0;i<K;++i)
		if (!cover[i]){
			cover[i] = true;
			pt[dep] = i;
			_find(dep+1);
			cover[i] = false;
		}
}

inline int _calc(int i, int j){
	int ret = 1;
//	cout<<cc[i*K+p[j][0]]<<i*K+p[j][0];
	for (int r=1;r<K;++r){
//		cout<<cc[i*K+p[j][r]]<<i*K+p[j][r];
		if (cc[i*K+p[j][r]]!=cc[i*K+p[j][r-1]])ret++;
	}
//	cout<<endl;
	return ret;
}

int main(){
	ifstream cin("d1.in");
	ofstream cout("d1.out");
	
	cin>>T;
	for (int Case=1; Case<=T; ++Case){
		cin>>K;
		
		tot=0;
		memset(cover, 0, sizeof(cover));
		_find(0);
		
		cin>>cc;
//cout<<cc<<endl;
		
		int sz = int(cc.size()) / K;
		for (int i=0;i<sz;++i)
		for (int j=0;j<tot;++j){
			int ret = _calc(i, j);
//			cout<<ret<<endl;
			
						
			if (i>0){
				int ans = MAXV;
				//for (int r=0;r<tot;++r){
				int r = j;{
					int tmp = F[i-1][r];
					if (cc[i*K+p[j][0]]==cc[(i-1)*K+p[r][K-1]])
						tmp--;
					if (tmp < ans) ans = tmp;
				}
				ret += ans;
			}
			
			F[i][j] = ret;
		}
		
		int cnt = MAXV;
		for (int j=0;j<tot;++j) 
			if (F[sz-1][j] < cnt) cnt = F[sz-1][j];		
		cout<<"Case #"<<Case<<": "<<cnt<<endl;
	}
	
//	system("pause");
	return 0;
}
