#include <iostream>
#include <string>
using namespace std;
int D[100][1000];
int T,N,M;
int A[100];
string Search[100];
string Query[1000];
string temp;
int main()
{
	int q,t,w,e;
	cin >> T;
	for (t=1;t<=T;t++)
	{
		cin >> N;
		getline(cin,temp);
		for(q=0;q<N;q++)
		       	getline(cin,Search[q]);
		cin >> M;
		getline(cin,temp);
		if (M==0) 
		{
			int ans=0;
			cout << "Case #" << t <<": " << ans << endl;
			continue;
		}
		for (q=0;q<M;q++) getline(cin,Query[q]);
		int n,c=0,ret=0,f;
		for (n=-1;n<M;n++)
		{
			if (n>=0 && Search[c]!=Query[n]) continue;
			if (n>=0) ret++;
			for (q=0;q<N;q++) A[q]=M;
			for (q=M-1;q>=n && q>=0;q--)
			{
				f=1;
				for (w=0;w<N;w++)
				{
					if (Search[w]==Query[q])
					{
						A[w]=q;
						f=0;
					}
				}
				if (t==20 && f) cout  << "no match for <" << Query [q] << "><" << Search[7] << ">" << endl;
			}
			for (q=0;q<N;q++)
				if (A[q]>A[c]) 
					c=q;
		}
		cout << "Case #" << t <<": " << ret << endl;	
	}
}
