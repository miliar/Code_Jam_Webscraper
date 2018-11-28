#include <iostream> 
#include <math.h>
using namespace std;




int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);

	int T;
	cin>>T;
	for(int casei=1;casei<=T;casei++)
	{
		int l,p,c;
		cin>>l>>p>>c;
		int re=p/l;
		if(p>re*l) re++;
		int num=0;
		for(int i=1;;i*=2)
		{
			int a=(int)pow(c,i);
			if(a>=re) break;
			num++;
		}
		cout<<"Case #"<<casei<<": "<<num<<endl;
	}

	return 0;
}