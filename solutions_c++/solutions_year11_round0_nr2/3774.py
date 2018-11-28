//Compiled using Visual Studio C++ 2010 Express - Version 10.0.30319.1 RTMRel
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <map>
#include <bitset>

using namespace std;

typedef pair<char,char> CPAIR;
typedef pair<int,int> IPAIR;
typedef pair<string,string> SPAIR;

typedef vector<int> IVECTOR;
typedef vector<int>::iterator IVECTOR_ITR;
typedef vector<char> CVECTOR;
typedef vector<float> FVECTOR;
typedef vector<string> SVECTOR;

typedef map<int,int> IIMAP;
typedef map<char,char> CCMAP;
typedef map<int,string> ISMAP;
typedef map<string,string> SSMAP;
typedef map<string,int> SIMAP;


#define FOR(i,a,n) for (int i=a;i<n;i++)
#define FORN(i,a,n) for (int i=n-1;i>=a;i--)


#define FOR1(i,a,n) for (int i=a;i<=n;i++)
#define FOR1N(i,a,n) for (int i=n;i>a;i--)

void printcase (int n, string& mystring)
{
	printf("Case #%d: [",n);
	FOR(i,0,mystring.size())
	{
		printf("%c",mystring[i]);

		if (i < mystring.size()-1)
		{
			printf(", ");
		}
	}
	printf("]\n");

}



int main (int argv, char* argc[])
{
	freopen("in.txt","r+",stdin);
	freopen("out.txt","w+",stdout);

	char discard;

	int t = 0;
	scanf("%d",&t);

	FOR(i,0,t)
	{
		SVECTOR CArray, DArray;
		
		int c = 0;
		scanf("%d",&c);
		scanf("%c",&discard);
		map<CPAIR,char> Combination;
		map<CPAIR,char>::iterator CombinationItr;
		FOR(j,0,c)
		{
			char key1,key2,value;
			scanf("%c",&key1);
			scanf("%c",&key2);
			scanf("%c",&value);
			
			CPAIR temp(key1,key2);
			CPAIR temp1(key2,key1);
			
			Combination[temp]=value;
			Combination[temp1]=value;

		}

		CVECTOR DemolitionKey;
		CVECTOR DemolitionValue;
		int d = 0;
		cin >> d;
		scanf("%c",&discard);
		FOR(j,0,d)
		{
			char first,second;
			scanf("%c",&first);
			scanf("%c",&second);
			
			//CPAIR temp(ch[0],ch[1]);
			//CPAIR temp1(ch[1],ch[0]);

			DemolitionKey.push_back(first);
			DemolitionKey.push_back(second);
			DemolitionValue.push_back(second);
			DemolitionValue.push_back(first);
		}


		int n = 0;
		cin >> n;
		scanf("%c",&discard);
		string mystring;
		char prev('\0');
		FOR(j,0,n)
		{
			char curr;
			scanf("%c",&curr);

			bool ProcessingDone = false;
			
			
			if ((CombinationItr = Combination.find(make_pair(prev,curr))) != Combination.end())
			{
				mystring.pop_back();
				mystring.push_back(CombinationItr->second);
				prev = CombinationItr->second;
				ProcessingDone = true;
			}
			else
			{
				FOR(k,0,DemolitionKey.size())
				{
					if (DemolitionKey[k] == curr)
					{
						if (string::npos != mystring.find(DemolitionValue[k]))
						{
							mystring.clear();
							prev = '\0';
							ProcessingDone = true;
							break;
						}
					}
				}
			}

			if (!ProcessingDone)
			{
				mystring.push_back(curr);
				prev = curr;
			}

		}

		printcase(i+1,mystring);
	}


	fclose(stdin);
	fclose(stdout);
}