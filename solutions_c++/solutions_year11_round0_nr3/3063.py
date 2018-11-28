#include <iostream>
#include <vector>
using namespace std;

void zamiana(int liczba,vector<int> &tab)
{
	for(int i = 0 ; i< tab.size() ; i++)
	{
		tab[i]=0;
	}

	int ktory = tab.size() -1;
	do
	{
		tab[ktory] = liczba%2;
		liczba/=2;
		ktory--;
	}while( liczba !=0 );
}

int potega(int wykladnik)
{
	int potega = 1;

	for(int i = 0 ;i< wykladnik; i++)
	{
		potega*=2;
	}
return potega;
}

int exec(vector<int> cyfry)
{
	vector<int> jak(cyfry.size(),0);

		int anormSum = 0;
		int bnormSum = 0;
		int axorSum = 0;
		int bxorSum = 0;

		int best = -1;
		int poteg = potega(cyfry.size());
		for(int j = 1 ; j<poteg-1 ; j++)
		{
			zamiana(j,jak);
			 anormSum = 0;
			 bnormSum = 0;
			 axorSum = 0;
			 bxorSum = 0;


			 for(int i = 0 ; i< jak.size() ; i++)
			 {
				 if(jak[i])
				 {
					anormSum+=cyfry[i];
					axorSum^=cyfry[i];
				 }
				 else
				 {
					bnormSum+=cyfry[i];
					bxorSum^=cyfry[i];				
				 }		
			 }

			 int wieksze = anormSum;
			 if(bnormSum > wieksze) wieksze = bnormSum;

			 int megaxorsum = axorSum^bxorSum;
			 if(megaxorsum == 0)
			 {
				if(best < wieksze) best = wieksze;
			 }		

		}
return best;		
}

#define SMALL
int main(int argc, char* argv[])
{

#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif


	int T = 0;
	int tmp = 0;
	int ileCyfr = 0;
	
	cin>>T;
	
	for(int i = 0 ; i< T ; i++)
	{
		cin >> ileCyfr ;
	
		vector<int> cyfry;

		for(int j = 0 ; j< ileCyfr ; j++)
		{
			cin >> tmp;
			cyfry.push_back(tmp);

		}
		int odp = exec(cyfry);
		
		cout<<"Case #"<<i+1<<": ";

		if(odp==-1)
			cout<<"NO";
		else 
			cout<<odp;

		cout<<endl;
	}
	

	

	return 0;
}

