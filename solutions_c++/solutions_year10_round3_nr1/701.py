#include <iostream> 
using namespace std;

struct c
{
	int a;
	int b;
};
c cab[1001];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

	int T;
	cin>>T;
	for(int casei=1;casei<=T;casei++)
	{
		int N,num=0;
		cin>>N;
		for(int i=0;i<N;i++)
		{
			cin>>cab[i].a>>cab[i].b;
		}
		for(i=0;i<N;i++)
			for(int j=i+1;j<N;j++)
			{
				if(cab[i].a>cab[j].a && cab[i].b<cab[j].b)
					num++;
				if(cab[i].a<cab[j].a && cab[i].b>cab[j].b)
					num++;
			}
		cout<<"Case #"<<casei<<": "<<num<<endl; 
	}

	return 0;
}