#include<iostream>
#include<set>
using namespace std;
typedef multiset<int> mi;

int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		mi a;
		int n;
		cin>>n;
		for(int i=0;i<n;i++){
			int x,y;
			cin>>x>>y;
			for(int j=0;j<y;j++)
				a.insert(x);
		}
		int count=0;bool up=0;
		do{
//			for(multiset<int>::iterator it=a.begin();it!=a.end();cout<<(*it)<<" ",it++);cout<<endl;
			up=0;
			int last=-100000000;
			for(multiset<int>::iterator it=a.begin();it!=a.end();it++){
				int num=*it;
				if(num==last){
					int c=a.count(num);
//					cout<<num<<" "<<c<<endl;
					a.erase(num);
					for(int j=0;j<c-2;j++)
						a.insert(num);
					a.insert(num-1);
					a.insert(num+1);
					up=1;
					count++;
					break;
				}
				last=num;
			}
		}while(up);
		cout<<"Case #"<<tt<<": "<<count<<endl;
	}
}