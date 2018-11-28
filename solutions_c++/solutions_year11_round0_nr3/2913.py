#include<set>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;

int candy[1010];
int n;
int maxc;

int add(int a, int b)
{
	int c = 0;
	int a1,b1;
	int i = 0;
	int temp = 1;
	while(a||b)
	{
		a1=a%2;b1=b%2;
		a/=2;b/=2;
		if((a1==0)&&(b1==0)||(a1&&b1))
		{
			//c+=0;
		}
		else
		{
			c+=temp;
		}
		temp*=2;
	}
	return c;
}

int pc,p1,p2;

void def(int i, int psum, int ssum)
{
	if(i==n){
		if (add(psum,ssum)==0)
		{
			if(pc>maxc&&p1&&p2) maxc=pc;
		}
		return ;
	}
	int pct,sct;
	pct = add(psum,candy[i]);
	sct = add(ssum,candy[i]);
	pc+=candy[i];
	p1++;
	def(i+1,pct,ssum);
	p1--;
	p2++;
	pc-=candy[i];
	def(i+1,psum,sct);
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("outl.txt","w",stdout);
	int t;
	cin >> t;
	for(int i = 0; i!= t; i++){
		cin >> n;
		memset(candy, 0, 1010*sizeof(int));
		for(int j =0;j!=n;j++) cin >> candy[j] ;

		maxc = -1;
		pc = 0;
		p1=0;p2=0;
		def(0,0,0);

		if(maxc!=-1){
			cout << "Case #" << i+1 << ": " <<  maxc << endl;	
		}
		else cout << "Case #" << i+1 << ": NO"  << endl;	
	}
}