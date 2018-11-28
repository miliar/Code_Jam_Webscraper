#include<iostream>
#include<limits.h>
#include<queue>
using namespace std;
struct type
{
	int time;
	int but;
};
int main()
{
	int note;
	cin>>note;
	for(int caseno=1;caseno<=note;caseno++)
	{
		int n;
		cin>>n;
		type temp;
		char where;
		queue<type> orange,blue;
		for(int i=1;i<=n;i++)
		{
			cin>>where;
			cin>>temp.but;
			temp.time=i;
			if(where=='O')
				orange.push(temp);
			else
				blue.push(temp);
		}
//		cout<<orange.size()<<" "<<blue.size()<<endl;
		int time=0;
		int bloc=1,oloc=1;
		while(!(orange.empty()&&blue.empty()))
		{
			time++;
//			cout<<"TIME "<<time<<" : ";
			type ortop,bluetop;
			ortop.time=INT_MAX;
			bluetop.time=INT_MAX;
			if(!orange.empty())
				ortop=orange.front();
			if(!blue.empty())
				bluetop=blue.front();
			if(ortop.time<bluetop.time||blue.empty())
			{
				if(bluetop.but!=bloc&&!blue.empty())
				{
//					cout<<" Changed blue pos ";
					if(bluetop.but>bloc)
						bloc++;
					else
						bloc--;
				}
				if(ortop.but==oloc&&orange.size()!=0)
				{
//					cout<< " pressed Orange ";
					orange.pop();
				}
				else
				{
//					cout<<" Changed orpos ";
					if(ortop.but<oloc)
						oloc--;
					else
						oloc++;
				}
			}
			else
				if(ortop.time>bluetop.time||orange.empty())
				{
					if(ortop.but!=oloc&&!orange.empty())
					{
//						cout<<" Changed Orpos ";
						if(ortop.but<oloc)
							oloc--;
						else
							oloc++;
					}
					if(bluetop.but==bloc&&blue.size()!=0)
					{
//						cout<<" pre blue ";
						blue.pop();    
					}
					else
					{
//						cout<<" Changed bluepos ";
						if(bluetop.but>bloc)
							bloc++;
						else
							bloc--;
					}

				}
//			cout<<bloc<<" "<<oloc<<endl;
		}
		cout<<"Case #"<<caseno<<": "<<time<<endl;
	}
}
