#include <iostream>
#include <list>
using namespace std;


list<int> liczba;
list<int>::iterator it;
int n,i,a,b,j,pom,k,wynik,l,size;
int bylo[10];
bool czy;

int main()
{
	ios_base::sync_with_stdio(0);
	cin>>n;
	for(i=0;i<n;++i)
	{
		wynik=0;
		cin>>a;
		cin>>b;
		for(j=a;j<=b;++j)
		{
			pom=j;
			k=0;
			size=0;
			liczba.clear();
			while(pom>0)
			{
				liczba.push_back(pom%10);
				pom=int(pom/10);
				++k;
			}
			while(k>1)
			{
				liczba.push_back(*(liczba.begin()));
				liczba.pop_front();
				it=liczba.end();
				pom=0;
				while(it!=liczba.begin())
				{
					--it;
					pom=pom*10;
					pom+=*it;
				}
				if((j<pom)&&(pom<=b))
				{
					czy=1;
					for(l=0;l<size;++l)
					{
						if(bylo[l]==pom) {czy=0;}
					}
					if(czy) {++wynik;}
				}
				bylo[size]=pom;
				++size;
				--k;
			}
			
		}
		cout<<"Case #"<<i+1<<": "<<wynik<<endl;
	}
	return 0;
}
