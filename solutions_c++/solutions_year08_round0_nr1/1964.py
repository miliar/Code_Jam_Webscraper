#include <iostream>
#include <string>

using namespace std;

const int inf=10000000;

string S[100];
string Q[1000];
int M[1000][100];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	cin>>n;
	for (int t=0; t<n; ++t){
		int s;
		string ss;
		cin>>s;
		getline(cin,ss);
		for (int i=0; i<s; ++i)
			getline(cin, S[i]);
		int q;
		cin>>q;
		getline(cin,ss);
		for (int i=0; i<q; ++i)
			getline(cin, Q[i]);

		for (int j=0; j<s; ++j)
			if (Q[q-1]==S[j])
				M[q-1][j]=1;
			else
				M[q-1][j]=0;

		for (int i=q-2; i>=0; --i)
			for (int j=0; j<s; ++j){
				M[i][j]=inf;
				if (Q[i]!=S[j])
					M[i][j]=M[i+1][j];
				for (int k=0; k<s; ++k)
					if (k!=j){
						M[i][j]=min(M[i][j], M[i+1][k]+1);
					}
			}

		/*for (int i=0; i<q; ++i){
			for (int j=0; j<s; ++j)
				cout<<M[i][j]<<" ";
			cout<<endl;
		}*/

		int res=inf;
		for (int j=0; j<s; ++j)
			res = min(res, M[0][j]);

		cout<<"Case #"<<t+1<<": "<<res;
		if (t<n-1)
			cout<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}