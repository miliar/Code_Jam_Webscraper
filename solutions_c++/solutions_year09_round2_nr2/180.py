#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int T,te=1;
	cin >> T;
	while(T--)
	{
		string A,res;
		cin >> A;
		int p=A.size()-1;
		while(p) if(A[p-1]<A[p]) break; else p--;
		p--;
		if(p==-1)
		{
			reverse(A.begin(),A.end());
			int pos = 0;
			while(A[pos] == '0') pos++;
			swap(A[pos],A[0]);
			res = A.substr(0,1) + "0" + A.substr(1);
		}
		else
		{
			int pos = p+1;
			for(int i=p+1;i<A.size();i++) if(A[i]>A[p])
			{
				if(A[pos] > A[i]) pos = i;
			}
			swap(A[p],A[pos]);
			string po = "";
			for(int i=p+1;i<A.size();i++) po+=A[i];
			sort(po.begin(),po.end());
			res = A.substr(0,p+1) + po;
		}
		cout << "Case #" << te << ": " << res << endl;
		te++;
	}
	return 0;
}
