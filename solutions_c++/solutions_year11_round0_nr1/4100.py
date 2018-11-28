#define DEBUG 0
#include<iostream>
#include<vector>
using namespace std;
vector<pair<bool, int> > v;
int O;
int B;
int O_to;
int B_to;
int O_order;
int B_order;
int next(bool t)
{
	int pos;
	int k=v.size();
	if(t)
		pos=O_order+1;
	else
		pos=B_order+1;
	for(;pos<k;pos++)
		if(v[pos].first==t)
			return pos;
	return -1;
}
int main()
{
	ios::sync_with_stdio(0);
	int n;
	cin >> n;
	for(int x=1;x<=n;x++)
	{
		v.clear();
		int k;
		cin >> k;
		v.resize(k);
		O_to=-1;
		B_to=-1;
		O_order=-1;
		B_order=-1;
		for(int i=0;i<k;i++)
		{
			char c;
			int t;
			cin >> c;
			cin >> t;
			v[i]=make_pair((c=='O'),t);
			if(O_to==-1&&c == 'O')
			{
				O_to=t;
				O_order=i;
			}
			if(B_to==-1&&c == 'B')
			{
				B_to=t;
				B_order=i;
			}
		}
		if(DEBUG) cout <<O_to << "X " << B_to<<endl;
		int c=0;
		int fin=-1;
		O=1;
		B=1;
		bool clc=false;
		while(true)
		{
			clc=false;
			if(DEBUG) cout << "fin:" << fin <<" O:"<< O << "-> " <<O_to;
			if(DEBUG) cout << " B:" << B << "->" << B_to <<endl;
			if(DEBUG) cout << "c:" << c;
			if(v[fin+1].first && O==O_to)
			{ 	//O
				O_order=next(true);
				O_to=v[O_order].second;
				fin++;
				clc=true;
				if(DEBUG) cout << " click O";
			}
			else if(O_to>O)
			{
					if(DEBUG) cout << " O++";
					O++;
			}
			else if(O_to<O)
			{
					if(DEBUG) cout << " O--";
					O--;
			
			}
			if(v[fin+1].first==false && B==B_to&&clc==false)
			{	//B
				B_order=next(false);
				B_to=v[B_order].second;
				fin++;
				clc=true;
				if(DEBUG) cout << " click B, new order id:" << B_order;
			}
			else if(B_to>B)
			{
				if(DEBUG) cout << " B++";
				B++;
			}
			else if(B_to<B)
			{
				if(DEBUG) cout << " B--";
				B--;
			}
			c++;

			if(DEBUG) cout << endl;
			if(fin==k-1)
				break;
		}
		cout << "Case #"<<x << ": "  <<c<< endl;

	}
}
