#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <afx.h>
#include <vector>

using namespace std;
typedef vector<CString> STRVECTOR;

void CompareVectors(CString str, STRVECTOR& vec)
{
	STRVECTOR::iterator theIterator;
	bool fin = false;
	int i=0;
	for (theIterator = vec.begin(); theIterator != vec.end(); theIterator++)
	{
		CString tmp = vec.at(i);
		if (0 == strcmp(tmp, str))
		{
			fin = true;
			break;
		}
		i++;
	}
	if (!fin)
		vec.push_back(str);
}

int main()
{
	//GenTable(100,100);
	CStdioFile fp, fw;
	if (!fp.Open("A-large.in.txt", CFile::modeRead))
		return -1;
	if (!fw.Open("A-large.out.txt", CFile::modeCreate|CFile::modeWrite|CFile::typeText))
		return -1;

	CString str;
	fp.ReadString(str);
	int casenum = atoi(str);
	int caseindex = 1;
	while (casenum > 0)
	{
		int switchtime = 0;
		fp.ReadString(str);
		int enginenum = atoi(str);
		for (int i=0; i<enginenum; i++)
			fp.ReadString(str);
		//
		fp.ReadString(str);
		int queriesnum = atoi(str);
		if (0 != queriesnum)
		{
			fp.ReadString(str);
			STRVECTOR vec;
			vec.push_back(str);
			for (int i=1; i<queriesnum; i++)
			{
				fp.ReadString(str);
				CompareVectors(str, vec);
				int i_size = vec.size();
				if (i_size == enginenum)
				{
					switchtime++;
					vec.erase(vec.begin(), vec.end());
					vec.push_back(str);
				}
			}
			//
			
		}

		//output to file
		CString strrlt;
		strrlt.Format("Case #%d: %d\n", caseindex, switchtime);
		fw.WriteString(strrlt);
		casenum--;
		caseindex++;
	}
	fp.Close();
	fw.Close();
	
	return 0;

}