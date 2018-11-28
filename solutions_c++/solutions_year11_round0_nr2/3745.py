
#include <iostream>
#include <string>
#include <cstring>
//#include <stack>
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("myret.out","w",stdout);
	int T,c,n,d,flag;
	char a[20],t;
	int k,op,cases=1;
//	queue<char> q;
	string com,del,inv;
	cin >>T;
	while (T--)
	{
		k=0;
		cin >>c;
		if(c) cin >>com;
		cin >>d;
		if(d) cin >>del;
		cin >>n;
		if(n) cin >>inv;
		a[k++]=inv[0];
	//	q.push(inv[0]);
		for (int i=1;i<inv.size();i++)
		{
			flag=1;
			t=inv[i];
			if(c && k>0 && ((a[k-1]==com[0] && t==com[1]) || (a[k-1]==com[1] && t==com[0])))
				flag=0,a[k-1]=com[2];
			else if(d){
				for(op=0;op<k;op++)
					if((a[op]==del[0] && t==del[1]) ||( a[op]==del[1] && t==del[0])){
						flag=0;
						k=0;
						break;
					}
			}
			if(flag)
				a[k++]=t;			
		}
		cout <<"Case #"<<cases++<<": "<<"[";
		if(k)
			cout <<a[0];
		for (int i=1;i<k;i++)
			cout <<", "<<a[i];
		
		cout <<"]"<<endl;
	}
	return 0;
}
