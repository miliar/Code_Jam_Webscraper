// a.cpp : Defines the entry point for the console application.
//


#include <vector>
#include <string>
#include <sstream>
#include <iostream>
using namespace std;

vector<string> vecs;
vector<string> vecq;

int marks[101];
void show(vector<string> vec)
{
	vector<string>::iterator theIter;
	
	for (theIter = vec.begin(); theIter != vec.end(); theIter ++)
	{
		cout << *theIter << endl;
	}
	cout << endl;
}
int solve(int s,int q)
{
	int res = 0;
	memset(marks,0,sizeof(marks));
	int i,j,k;
	for (i = 0; i < q; i ++)
	{
		for (j = 0; j < s; j++)
		{
			if (vecs[j] == vecq[i] && marks[j] == 0)
				marks[j] = 1;
			int sum = 0;
			for(k = 0; k < s ; k++)
				sum += marks[k];
			if(sum == s)
			{
				vecq.erase(vecq.begin(),vecq.begin()+i);
			//	vecs.erase(vecs.begin()+j);
		//		show(vecs);
		//		show(vecq);
				return solve(s,q-i) + 1;
				
			}
			
		}
	}
	return 0;
}
int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("a_large_output.txt","w",stdout);
	char S[1000];
	
	int n;
	cin.getline(S, 1000);
	istringstream sin(S);
	
	sin >> n;

	int s,q,k;

	for (k = 1; k <= n; k++)
	{
		
		int i;
		cin.getline(S, 1000);
		istringstream sin1(S);
		sin1 >> s;
		vecs.clear();

		
		for(i = 0; i < s; i++)
		{
			string strtemp;	
			cin.getline(S, 1000);
			strtemp = S;
//			istringstream sinStr1(S);
//			sinStr1 >> strtemp;
			vecs.push_back(strtemp);
		}

		cin.getline(S, 1000);
		istringstream sin2(S);
		sin2 >> q;
		vecq.clear();

		
		for (i = 0; i < q; i++)
		{
			string strtemp;
			cin.getline(S, 1000);
			strtemp = S;
			vecq.push_back(strtemp);
		}
	//	show(vecs);
	//	show(vecq);

		cout << "Case #" << k << ": " << solve(s,q) << endl;
	}
	return 0;
}
