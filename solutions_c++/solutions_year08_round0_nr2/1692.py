#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <sstream>
#include <map>

using namespace std;

struct t
{
	int h,m;

	t(int a,int b){h=a,m=b;}
	t(){h=300,m=300;}
	void add(int z)
	{
		m+=z;
		h+=m/60;
		m%=60;
	}
};

struct trip
{
	bool done;
	t st,et;
	trip(){done=false;}
	trip(t a,t b){st=a,et=b;}
};

bool operator < (t a,t b)
{
	if (a.h!=b.h) return a.h < b.h;
	return a.m <= b.m;
}

bool operator < (trip a,trip b)
{
	if (a.st.h!=b.st.h) return a.st.h < b.st.h;
	return a.st.m <= b.st.m;
}

int getFirst(vector<trip>& A,t tmp)
{
	int ret = -1;
	
	t min;
	min.h = 300;
	for (int i=0;i<A.size();i++)
	{
		if (!A[i].done && tmp < A[i].st && A[i].st < min)
		{
			min = A[i].st;
			ret = i;
		}
	}

	return ret;
}

void sim(vector<trip>& A,vector<trip>& B,int tat,int fA,int fB)
{
	if (fA!=-1)
	{
		t cur;

		A[fA].done = true;
		cur = A[fA].et;
		cur.add(tat);

		fB = getFirst(B,cur);
		sim(A,B,tat,-1,fB);
	}
	else if (fB!=-1)
	{
		t cur;

		B[fB].done = true;
		cur = B[fB].et;
		cur.add(tat);

		fA = getFirst(A,cur);
		sim(A,B,tat,fA,-1);
	}
}

pair<int,int> f(vector<trip>& A,vector<trip>& B,int tat)
{
	pair<int,int> ret;
	vector<bool> bA(A.size(),false),bB(A.size(),false);

	int lim = A.size() + B.size();

	while (true)
	{
		if (lim==0) return ret;

		t cur;
		cur.h = cur.m = 0;
		
		int fA,fB;

		fA = getFirst(A,cur);
		fB = getFirst(B,cur);

		if (fA==-1 && fB==-1) return ret;
		if (fA!=-1 && (fB==-1 || A[fA]<B[fB]))
		{
			sim(A,B,tat,fA,-1);
			ret.first++;
		}
		else 
		{
			sim(A,B,tat,-1,fB);
			ret.second++;
		}
	}
}



int main()
{
	int t=0,n;
	stringstream ss;

	cin>>n;
	ofstream outs;

	while (n--)
	{
		int tat = 0,na,nb;
		vector<trip> A,B;

		cin>>tat;

		cin>>na>>nb;
		while (na--)
		{
			char ch;
			trip tmp;

			cin>>tmp.st.h>>ch>>tmp.st.m;
			cin>>tmp.et.h>>ch>>tmp.et.m;
			A.push_back(tmp);
		}

		while (nb--)
		{
			char ch;
			trip tmp;

			cin>>tmp.st.h>>ch>>tmp.st.m;
			cin>>tmp.et.h>>ch>>tmp.et.m;
			B.push_back(tmp);
		}

		pair<int,int> p = f(A,B,tat);
		ss<<"Case #" <<++t<<": ";
		ss<<p.first<<" "<<p.second<<endl;
	}

	cout<<ss.str()<<endl;
	outs.open("a.txt");
	outs<<ss.str()<<endl;
}