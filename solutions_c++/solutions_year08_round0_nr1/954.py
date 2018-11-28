#include <list>
#include <string>
#include <vector>
using namespace std;
typedef vector<string> StringList;

int f(int s[],int i,StringList &EngneerList,StringList &SearchWordList)
{
	if(s[i] == -1)
	{
		int nMin = 100000000;
		for(StringList::iterator iterEngneerList = EngneerList.begin();
			iterEngneerList!=EngneerList.end();iterEngneerList++)
		{
			
			if(iterEngneerList->compare(SearchWordList[i]))
			{
				int nChangeTimes = 0;
				for(StringList::size_type j = i+1;j!=SearchWordList.size();j++)
				{
					if(iterEngneerList->compare(SearchWordList[j])==0)
					{
						nChangeTimes = 1 + f(s,j,EngneerList,SearchWordList);
						break;
					}

				}

				if(nChangeTimes < nMin)
				{
					nMin = nChangeTimes;
				}
			}
		}
		s[i] = nMin;

	}
	
	return s[i];
	
}
int SaveUniverse()
{
	int nSearchEngineer = 0;
	StringList EngneerList;

	scanf("%d\n",&nSearchEngineer);
	for(int i=0;i<nSearchEngineer;i++)
	{
		string strSearchEngineer;
		char buffer[200];
		fgets(buffer,200,stdin);
		strSearchEngineer = buffer;
		EngneerList.push_back(strSearchEngineer);

	}

	int nSearchWord = 0;
	StringList SearchWordList;

	scanf("%d\n",&nSearchWord);
	if(nSearchWord ==0)
	{
		return 0;
	}
	for(int i=0;i<nSearchWord;i++)
	{
		string strSearchWord;
		char buffer[200];
		fgets(buffer,200,stdin);
		strSearchWord = buffer;
		SearchWordList.push_back(strSearchWord);

	}

	int *s = new int[nSearchWord];
	for(int i =0;i<nSearchWord;i++)
	{
		s[i] = -1;
	}

	f(s,0,EngneerList,SearchWordList);

	int r = s[0];
	delete[] s;
	return r;
	
}


int main(int argc, char* argv[])
{
	int nCaseNumber = 0;
		freopen("f:\\A-small-attempt1.in.txt","r",stdin);
	;
	scanf("%d",&nCaseNumber);
	vector<int> r;
	
	for(int i = 0;i<nCaseNumber;i++)
	{
		r.push_back(SaveUniverse());
		//printf("Case #%d: %d\n",i+1,SaveUniverse());
	}

	FILE *file = fopen("f:\\Output01.txt","w+");
	for(int i = 0;i<nCaseNumber;i++)
	{
		
		fprintf(file,"Case #%d: %d\n",i+1,r[i]);
	}
	fclose(file);
	return 0;
}