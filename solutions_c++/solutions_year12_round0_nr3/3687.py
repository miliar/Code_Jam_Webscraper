#include<iostream>
#include<fstream>
#include<cassert>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;++i)
#define MAX 2000010

int position[MAX];

int main(int argc, char *argv[])
{

//cout<<"??\n";

	if(argc!=3) return -1;
	
//cout<<"QQ\n";	
	
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

//cout<<"AA\n";

	//preprocessing
	cout<<"preprocessing\n";
	int ten[9]={1,10,100,1000,10000,100000,1000000,10000000,100000000};
	int combine[10]={0,0,1,3,6,10,15,21,28,36};

	REP(i,0,MAX)
		position[i]=-1;
	
	int num=-1,temp;
	REP(i,0,9-1)
	{
cout<<"start "<<i<<endl;
		for(int j=ten[i];j<ten[i+1];++j) {

//cout<<j<<endl;
	
			if(j<MAX && position[j]==-1)
			{
				++num;
				temp=j;
				do {
					if (temp<MAX && temp>= ten[i] && temp<ten[i+1]) {
//cout<<"  "<<temp<<endl;
						assert(position[temp]==-1);
						position[temp]=num;
					}
					temp=temp/10+(temp%10)*ten[i];
				} while (temp!=j);
			
			}
		}
	}
	
	//do
	cout<<"start running\n";
	int record[MAX],T,A,B;
	long long ans;
	fin>>T;
	REP(i,0,T)
	{
		fin>>A>>B;
		memset(record,0,sizeof(int)*MAX);
		ans=0;
		
		for(int j=A;j<=B;++j)
			++record[ position[j] ];
		REP(j,0,MAX)
			ans+=combine[ record[j] ];
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}

	return 0;
}
