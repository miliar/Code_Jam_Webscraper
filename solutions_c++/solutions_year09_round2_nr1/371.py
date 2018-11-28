#include <iostream>
using namespace std;
struct dtree
{
	double weight;
	string feature;
	int t1,t2;
} T[111000];
int nT=0;
string S[110];
int K;
void init(dtree &t)
{
	t.t1=t.t2=-1;
}
void myread(int k)
{
//	cout<<"read "<<k<<endl;
	char c;
	init(T[k]);
	scanf(" ( %lf ",&T[k].weight); 
//	cout<<"done "<<T[k].weight<<endl;
	if (cin.peek()==')') scanf(" ) "); else
	{
		cin>>T[k].feature;
//		cout<<endl<<"done "<<" "<<T[k].feature<<endl;
		T[k].t1=nT++;
		T[k].t2=nT++;
//		cout<<"read t1="<<T[k].t1<<endl;
		myread(T[k].t1);
//		cout<<"done t1"<<endl;
//		cout<<"read t2="<<T[k].t2<<endl;
		myread(T[k].t2);
//		cout<<"done t2"<<endl;
		scanf(" ) ");
	}
}
double go(int k,double p)
{
	p*=T[k].weight;
	if (T[k].t1==-1) return p;
	int t=lower_bound(S,S+K,T[k].feature)-S;
	if (t<K&&S[t]==T[k].feature) return go(T[k].t1,p); else
	return go(T[k].t2,p);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tt,ttt,N,i;
	string s;
    scanf("%d",&tt);
    for(ttt=1;ttt<=tt;ttt++)
    {
		cout<<"Case #"<<ttt<<":"<<endl;
		scanf(" %d ",&i);
		nT=1;
		myread(0);
		scanf("%d",&N);
		while(N--)
		{
			cin>>s>>K;
			for(i=0;i<K;i++) cin>>S[i];
			sort(S,S+K);
			printf("%.7lf\n",go(0,1));
		}
	}
//    system("pause");
    return 0;
}
