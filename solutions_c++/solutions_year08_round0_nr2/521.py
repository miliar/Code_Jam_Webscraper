#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;
/*
class SavingTheUniverse
{
public:
	SavingTheUniverse()
	{
		cin>>test;
		for (int testcase=0;testcase<test;testcase++){
			cin>>n;
			getchar();
			m.clear();
			for (int i=0;i<n;i++){
				string name;
				getline(cin,name);
				m[name]=i+1;
			}
			cin>>q;
			getchar();
			memset(d,0,sizeof(d));
			int cnt=0,res=0;
			for (int i=0;i<q;i++){
				string strq;
				getline(cin,strq);
				if (d[m[strq]]==0){
					cnt++;
				}
				if (cnt==n){
					res++;
					memset(d,0,sizeof(d));
					cnt=1;
				}
				d[m[strq]]=1;
			}
			cout<<"Case #"<<testcase+1<<": "<<res<<endl;
		}
	}
private:
	int n,q,test;
	map<string,int> m;
	int d[101];
};
*/

struct Event{
	int hh,mm,type,a2b;
	void set(int hh,int mm,int type,int T,int a2b){
		if (type==0) mm+=T;
		while (mm>60){
			hh++;
			mm-=60;
		}
		this->hh=hh;
		this->mm=mm;
		this->type=type;
		this->a2b=a2b;
	}
	bool operator<(const Event &x)const{
		return hh<x.hh||hh==x.hh&&mm<x.mm||hh==x.hh&&mm==x.mm&&type<x.type;
	}
};

class TrainTimetable
{
public:
	TrainTimetable()
	{
		int test,T,NA,NB,nowA,nowB,resA,resB;
		cin>>test;
		for (int testcase=0;testcase<test;testcase++){
			cin>>T;
			cin>>NA>>NB;
			d.clear();nowA=nowB=resA=resB=0;
			for (int i=0;i<NA;i++){
				int hh,mm;
				scanf("%d:%d",&hh,&mm);
				Event a2b,b2a;
				a2b.set(hh,mm,1,T,1);
				d.push_back(a2b);
				scanf("%d:%d",&hh,&mm);
				b2a.set(hh,mm,0,T,0);
				d.push_back(b2a);
			}
			for (int i=0;i<NB;i++){
				int hh,mm;
				scanf("%d:%d",&hh,&mm);
				Event b2a,a2b;
				b2a.set(hh,mm,1,T,0);
				d.push_back(b2a);
				scanf("%d:%d",&hh,&mm);
				a2b.set(hh,mm,0,T,1);
				d.push_back(a2b);
			}
			sort(d.begin(),d.end());
			for (int i=0;i<d.size();i++){
				if (d[i].type==1){
					if (d[i].a2b){
						nowA--;
						if (nowA<0) {resA++;nowA=0;}
					}else{
						nowB--;
						if (nowB<0) {resB++;nowB=0;}
					}
				}else{
					if (d[i].a2b){
						nowA++;
					}else{
						nowB++;
					}
				}
			}
			printf("Case #%d: %d %d\n",testcase+1,resA,resB);
		}
	}
private:
	vector<Event> d;
};

int main()
{
//	SavingTheUniverse a;
	TrainTimetable();
	return 0;
}