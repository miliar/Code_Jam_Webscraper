#include<iostream>
#include<fstream>
using namespace std;

const int MAXN=10;
const int MAXT=20;

int opl,opot,bpot,bpl,mpl,N,ans;
int mi[MAXN];
bool mc[MAXN]; // 0 is b---1 is o

int abs(int x)
{
	if(x<0)
		return -x;
	return x;	
}

int main()
{
	ifstream in ("A.in");
	ofstream out ("A.out");
	int T;
	in>>T;
	for(int t=0;t<T;t++)
	{
		in>>N;
		char a;
		for(int i=0;i<N;i++)
		{
			in>>a;
			in>>mi[i];
			mi[i]--;
			if(a=='B')
				mc[i]=false;
			else
				mc[i]=true;
		}
		ans=0;
		mpl=0;
		opl=0;
		opot=0;
		bpot=0;
		bpl=0;
		ans+=mi[mpl]+1;
		if(mc[mpl])
		{
			opl=mi[mpl];
			bpot=mi[mpl]+1;
		}
		else
		{
			bpl=mi[mpl];
			opot=mi[mpl]+1;
		}
		mpl++;
//		cout<<mpl<<" "<<ans<<"-"<<opl<<" "<<opot<<"-"<<bpl<<" "<<bpot<<" "<<endl;	
		int dis;
		while(mpl<N)
		{
			if(mc[mpl])
			{
				dis=abs(opl-mi[mpl]);
				opl=mi[mpl];
				if(opot>dis)
				{
					bpot++;
					ans++;
					opot=0;	
//					cout<<"1"<<endl;
				}
				else
				{
//					cout<<"2"<<endl;
					bpot+=dis-opot+1;
					ans+=dis-opot+1;
					opot=0;
				}
			}
			else
			{
				dis=abs(bpl-mi[mpl]);
				bpl=mi[mpl];
				if(bpot>dis)
				{
//					cout<<"3"<<endl;
					bpot=0;
					opot++;
					ans++;	
				}
				else
				{
///					cout<<"4"<<endl;
					opot+=dis-bpot+1;
					ans+=dis-bpot+1;
					bpot=0;
				}
			}
			mpl++;	
//			cout<<mpl<<" "<<ans<<"-"<<opl<<" "<<opot<<"-"<<bpl<<" "<<bpot<<"-"<<dis<<endl;	
		}
		out<<"Case #"<<t+1<<": "<<ans<<endl;	
	}
//	cin>>T;
	return 0;
}
