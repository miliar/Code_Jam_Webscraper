#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int reads[100];
int nr=0;
void readint(string s)
{
	nr=-1;
	istringstream is(s);
	
	while(is>>reads[++nr]);
}

bool visited[11][50000000];
bool succeed[11][50000000];

bool ish(int a, int base, int ind)
{
	//cout<<succeed[0][2]<<endl;
	//cout<<"RE:"<<a<<" "<<base<<" "<<ind<<" "<<visited[ind][a]<<" "<<succeed[ind][a]<<endl;
	if(visited[base][a]==true) {return succeed[base][a];}
	visited[base][a]=true;
	int result = 0;
	int aa=a;
	while(aa>0)
	{
		result+=(aa%base)*(aa%base);
		aa/=base;
	}
	
	if(result==1) {succeed[base][a]=true; return true;}
	succeed[base][a]=ish(result,base,ind); return succeed[base][a];
}



bool ishappy(int a, int base, int ind)
{
	
	return ish(a,base,ind);
}



int main()
{
	int cases;
	cin>>cases;
	char buffff[1000];
	cin.getline(buffff,1000);
	for(int i=1;i<=cases;i++)
	{
		//memset(visited,0,sizeof(visited));
		//memset(succeed,0,sizeof(succeed));
		char buf[1000];
		cin.getline(buf,1000);
		readint(string(buf));
		int ans = 2;
		while(true)
		{
			for(int a=0;a<nr;a++)
			{
				if(!ishappy(ans,reads[a], a)) goto continuethis;
			}
			
			break;
			continuethis:ans++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
}
