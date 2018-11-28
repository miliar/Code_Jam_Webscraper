#include <iostream>
#include <queue>
#include <string>
using namespace std;

int PatSum(int num1, int num2);
int MaxValue(int num1, int num2);
void main ()
{
	int testCases=0;
	int i = 1;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out2.txt","w",stdout);

	for (cin >> testCases; i <= testCases; i++)
    {
		int C,D,N;
		string Cstr, Dstr, Nstr;
		
		cin >> C;
		if (C>0) cin >> Cstr;
		
		cin	>> D;
		if (D>0) cin >> Dstr;
		
		cin	>> N;
		if (N>0) cin >> Nstr;

		for (int k=1; k <= Nstr.size(); k++)
		{
			string NstrTmp = Nstr.substr(0,k);

			for (int j=0; j<C; j++)
			{
				string combine = Cstr.substr(j*3,2);
				string toForm = Cstr.substr((j*3)+2,1);

				string rcombine = combine;
				reverse (rcombine.begin(), rcombine.end());
				
				if (NstrTmp.find(combine)!=string::npos)
				{
					Nstr.replace(NstrTmp.find(combine),combine.length(),toForm);
					k--;
				}
				else if (NstrTmp.find(rcombine)!=string::npos)
				{
					Nstr.replace(NstrTmp.find(rcombine),rcombine.length(),toForm);
					k--;
				}
			}
			NstrTmp = Nstr.substr(0,k);
			for (int j=0; j<D; j++)
			{
				string opposed1 = Dstr.substr(j*2,1);
				string opposed2 = Dstr.substr((j*2)+1,1);
				if (NstrTmp.find_first_of(opposed1)!=string::npos && NstrTmp.find_last_of(opposed2)!=string::npos)
				{
					if (NstrTmp.find_first_of(opposed1) < NstrTmp.find_last_of(opposed2))
					{
						Nstr.replace(0, NstrTmp.find_last_of(opposed2)+1,"");
						k-= NstrTmp.find_last_of(opposed2)+1;
					}
					else if (NstrTmp.find_first_of(opposed1) > NstrTmp.find_last_of(opposed2))
					{
						Nstr.replace(0, NstrTmp.find_first_of(opposed1)+1,"");
						k-= NstrTmp.find_first_of(opposed1)+1;
					}				
				}
			}
		}
		cout << "Case #" << i << ": [";
		for(int j=0; j<Nstr.size(); j++)
		{
			if (j>0)
				cout << ", ";
			cout << Nstr[j];
		}
		cout << "]" << endl ;
	}

}