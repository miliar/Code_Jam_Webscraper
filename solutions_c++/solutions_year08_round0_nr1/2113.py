#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

const int MAXC = 999999;

int N, S, Q;
vector<string> A;
vector<string> B;

int F[1100][110];

int solve(){
	if (Q==0) return 0;
	
	
	for (int j=0;j<S;j++)
		if (B[0] == A[j])
			F[0][j] = MAXC;
		else
			F[0][j] = 0;
			
	for (int i=1;i<Q;i++)
		for (int j=0;j<S;j++)
			if (B[i] == A[j])
				F[i][j] = MAXC;
			else{
				int ret = F[i-1][j];
				for (int k=0;k<S;k++)
					ret = min(ret, F[i-1][k]+1);
				F[i][j] = ret;
			}
	
	int ans = MAXC;
	for (int j=0;j<S;j++)
		ans = min(ans, F[Q-1][j]);

	return ans;
}

int main(){
	ifstream cin("input.in");
	ofstream cout("output.out");
	
	string lin;
	cin>>N;
	getline(cin, lin);

	int cnt = 0;
	while (N--){
		cin>>S; 
		getline(cin, lin);
		
		for (int i=0;i<S;++i){
			getline(cin, lin);
			A.push_back(lin);
//			cout<<lin<<endl;
		}
		
		cin>>Q;
		getline(cin, lin);
		for (int i=0;i<Q;++i){
			getline(cin, lin);
			B.push_back(lin);
		}
		
		cout<<"Case #"<<++cnt<<": "<<solve()<<endl;
		A.clear();
		B.clear();
	}

//	system("pause");	
	return 0;
}
