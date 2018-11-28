#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;

int T,k,last,x,i,j,n;
char a[100];
vector<char> aux;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>T;
	for(k=1;k<=T;++k)
	{
		cin>>a;
		n = strlen(a);
		aux.clear();
		last = '0';
		for(i=n-1;i>=0;--i)
		{
			if(a[i]<last){ last = a[i]; break;}
			else
				aux.push_back(a[i]);
			last = a[i];
		}
		if(i==-1) last = '0', ++i;
		sort(aux.begin(),aux.end());
		for(j=0;j<aux.size();++j)
			if(aux[j]>last)
			{
				x = last;
				last = aux[j];
				aux[j] = x;
				break;
			}			
		sort(aux.begin(),aux.end());
		a[i] = last;
		++i;
		for(j=0;j<aux.size();++j,++i)
			a[i] = aux[j];
		a[i] = 0;
		cout<<"Case #"<<k<<": "<<a<<endl;
	}
	fclose(stdout);
	return 0;
}
