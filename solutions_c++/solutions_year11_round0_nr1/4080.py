#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;

int main(){
	int t;
	int n;
	int blu,orang,time;
	char c;
	int q;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d",&t);
	queue<int> orange,blue;
	queue<char> ch;
	//cin>>t;
	for(int j=0;j<t;j++)
	{
		scanf("%d",&n);
		//cin>>q;
		blu=1;	orang=1;	time=0;
		for(int i=0;i<n;i++)
		{
			cin>>c;
			ch.push(c);
			cin>>q;
			if(c =='O')
			{
				orange.push(q);
			}
			else blue.push(q);
		}
		bool b,o;
		while(n>0)
		{
			b=false;	o=false;
			if(orange.size()!=0)
			{
				if(orange.front() >orang)
				{
					orang++;
					o=true;
				}
				else if(orange.front() <orang)
				{
					orang--;
					o=true;
				}
			}
			
			if(blue.size()!=0)
			{
				if(blue.front() >blu)
				{
					blu++;
					b=true;
				}
				else if(blue.front() <blu)
				{
					blu--;
					b=true;
				}
			}

			if(ch.size()!=0 && orange.size()!=0 && !o && orang==orange.front() && ch.front()=='O')
			{
				n--;
				ch.pop();
				orange.pop();
			}
			else if(ch.size()!=0 && blue.size()!=0 && !b && blu==blue.front() && ch.front()=='B')
			{
				n--;
				ch.pop();
				blue.pop();
			}
			time++;
		}

		printf("Case #%d: %d\n",j+1,time);
		//cout<<"Case #"<<j+1<<": "<<time<<endl;
	}

	return 0;
}