#include<iostream>
#include<vector>

using namespace std;

const int BRAK=0;

struct node
{
	int p,rank;
	char znak;
	int wys;
};

int _find(int v,vector<node>& A)
{
	if(A[v].p==v)
		return v;
	return A[v].p=_find(A[v].p,A);
}

void _union(int a,int b,vector<node>& A)
{
	a=_find(a,A);
	b=_find(b,A);
	if(A[a].rank<A[b].rank)
		A[a].p=b;
	else if(A[a].rank>A[b].rank)
		A[b].p=a;
	else
	{
		A[a].p=b;
		A[b].rank++;
	}
}



int main()
{
	ios_base::sync_with_stdio(false);
	
	int t;
	cin>>t;
	
	for(int i=0;i<t;i++)
	{
		
		int h,w;
		cin>>h>>w;
		
		vector<node> A(h*w);
		
		for(int j=0;j<h*w;j++)
		{
			cin>>A[j].wys;
			A[j].znak=BRAK;
			A[j].p=j;
		}
		
		//grupowanie wody	
		for(int j=0;j<h*w;j++)
		{
			int min=A[j].wys;
			if(j>=w && A[j-w].wys<min)
				min=A[j-w].wys;
			if(j%w!=0 && A[j-1].wys<min)
				min=A[j-1].wys;
			if(j%w!=w-1 && A[j+1].wys<min)
				min=A[j+1].wys;
			if(j<w*(h-1) && A[j+w].wys<min)
				min=A[j+w].wys;
			
			
			if(min!=A[j].wys)
			{
				int drugi;
				if(j>=w && A[j-w].wys==min)
					drugi=j-w;
				else if(j%w!=0 && A[j-1].wys==min)
					drugi=j-1;
				else if(j%w!=w-1 && A[j+1].wys==min)
					drugi=j+1;
				else
					drugi=j+w;
				
				
				int u = _find(j,A);
				int v = _find(drugi,A);
				if(u!=v)
					_union(u,v,A);
				
			}
		}
		
		//przypisaywanie oznaczen
		
		cout<<"Case #"<<i+1<<":"<<endl;
		
		int kolejny=0;
		for(int j=0;j<h*w;j++)
		{
			int p=_find(j,A);
			if(A[p].znak!=BRAK)
				A[j].znak=A[p].znak;
			else
			{
				A[p].znak='a'+kolejny;
				kolejny++;
				A[j].znak=A[p].znak;
			}
			cout<<A[j].znak;
			if(j%w==w-1)
				cout<<endl;
			else
				cout<<" ";
		}
		
	}
	return 0;
}
