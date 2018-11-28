#include<fstream>
#define dmax 102
using namespace std;
ifstream in("bot.in");
ofstream out("bot.out");

int n,m,tst,poz,crt,nr1,pz1[dmax],t1[dmax],nr2,pz2[dmax],t2[dmax];
char c;

int ab(int k)
{	
	if( k < 0)
		return -k;
	return k;
}	

int mx(int a, int b)
{	
	if( a > b)
		return a;
	return b;
}	


int main()
{	
	int i,j;
	
	in>>tst;
	
	
	for(j=1; j<=tst; j++)
	{	

		in>>n;
		
		pz1[0]=1;
		pz2[0]=1;
		
		for(i=1; i<=n; i++)
		{	
			in>>c>>poz;

			if(c == 'O')
			{	nr1++;
				pz1[nr1] = poz;
				
				t1[nr1] = t1[nr1-1] + abs(pz1[nr1]-pz1[nr1-1])+1;
				
				if(t1[nr1] <= t2[nr2])
					t1[nr1] = t2[nr2]+1;	
				
				//out<<"1: "<<pz1[nr1]<<" "<<t1[nr1]<<'\n';
			}
			
			if(c == 'B')
			{	nr2++;
				pz2[nr2] = poz;
				
				t2[nr2] = t2[nr2-1] + abs(pz2[nr2]-pz2[nr2-1])+1;
				
				if(t2[nr2] <= t1[nr1])
					t2[nr2] = t1[nr1]+1;
				
				//out<<"2: "<<pz2[nr2]<<" "<<t2[nr2]<<'\n';
			}
		}
		out<<"Case #"<<j<<": "<<mx(t1[nr1],t2[nr2])<<'\n';
		
		for(i=1; i<=nr1; i++)
			pz1[i] = t1[i] = 0;
		for(i=1; i<=nr2; i++)
			pz2[i] = t2[i] = 0;
		nr1 = nr2 = 0;
	}	
	in.close();
	out.close();
	return 0;
}	