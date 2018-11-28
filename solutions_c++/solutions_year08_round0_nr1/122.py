#include <string>
#include <map>
#include <vector>
#include <iostream>
using namespace std;

vector<string> eng;
vector<string> q;

int S;
int Q;

map<int,int> mm;

int sol(int qx, int se)
{
	if(qx==Q)
		return 0;
	int K=10000*qx+se;
	if(mm.find(K)!=mm.end())
		return mm[K];
	
	string query=q[qx];
	
	int ans=10*Q;
	if(query!=eng[se]){
		ans=sol(qx+1,se);
	}else{
		for(int i=0;i<S;i++)
		if(query!=eng[i])
			ans=min(ans, 1+sol(qx+1,i));
	}
	mm[K]=ans;
	//fprintf(stderr,"sol '%s'(%d)/%d -> %d\n",query.c_str(), qx, se, ans);
	return ans;
}

int main()
{
	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){
		eng.clear();
		q.clear();

		string tmp;
		
		cin >> S;
		getline(cin,tmp);

		eng.resize(S);
		for(int i=0;i<S;i++)
			getline(cin,eng[i]);

		cin >> Q;
		getline(cin,tmp);

		q.resize(Q);
		for(int i=0;i<Q;i++)
			getline(cin,q[i]);
		
		mm.clear();
		
		int mia=10*Q;
		for(int i=0;i<S;i++)
			mia=min(mia, sol(0,i));
			
		fprintf(stderr,"\nDONE S%d Q%d == %d\n",S,Q,mia);
		printf("Case #%d: %d\n", cutest, mia);
	}

	return 0;
}
