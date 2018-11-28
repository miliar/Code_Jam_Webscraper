#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

bool corectForPair(map<char,string>& cmbFind , string& str , char lastChar , map<string , char>& repGt)
{
	if(str.size() >= 2)
	{
		map<char,string>::iterator it;
		it = cmbFind.find(lastChar);
		if(it != cmbFind.end())
		{
			string findresStr = it->second;
			char lastbutOneChar = str.at(str.length() - 2);
			size_t found;
			found = findresStr.find(lastbutOneChar);
			if(found!=string::npos)
			{
				string cnStr;
				cnStr.push_back(lastbutOneChar);
				cnStr.push_back(lastChar);
				map<string , char>::iterator itGt;
				itGt = repGt.find(cnStr);
				char replChar = itGt->second;

				string newStr = str.substr(0 , str.length() - 2);
				newStr.push_back(replChar);
				str = newStr;
				return true;
			}
		}
	}
	return false;
}


bool corectForOpp(map<char,string>& oppFind , string& str , char lastChar , vector<char>& opStr)
{
	if(str.size() >= 2)
	{
		map<char,string>::iterator it;
		it = oppFind.find(lastChar);
		if(it != oppFind.end())
		{
			string findresStr = it->second;
			char lastbutOneChar = str.at(str.length() - 2);
			size_t found;
			found = findresStr.find(lastbutOneChar);
			if(found!=string::npos)
			{
				str = "";
				opStr.clear();
				return true;
			}
			for(int cn = 0 ; cn < opStr.size(); cn++)
			{
				char prevopStr = opStr[cn];
				found = findresStr.find(prevopStr);
				if(found!=string::npos)
				{
					str = "";
					opStr.clear();
					return true;
				}

			}
		}
	}
	return false;
}

int main()
{
	int tetCas;
	cin >> tetCas;
	for(int cnt = 1 ; cnt <= tetCas ; cnt++)
	{
		int cmb;
		cin >> cmb;
		map<char , string> cmbFind;
		map<string , char> repGet;
		for(int cmbCnt = 0 ; cmbCnt < cmb; cmbCnt++)
		{
			char cmbPr5 , cmbPr7;
			char repChar;
			cin >> cmbPr5;
			cin >> cmbPr7;
			cin >> repChar;
			cmbFind[cmbPr5].push_back(cmbPr7);
			cmbFind[cmbPr7].push_back(cmbPr5);
			string cmb5_cmb7;
			cmb5_cmb7.push_back(cmbPr5);
			cmb5_cmb7.push_back(cmbPr7);
			repGet[cmb5_cmb7] = repChar;

			string cmb7_cmb5;
			cmb7_cmb5.push_back(cmbPr7);
			cmb7_cmb5.push_back(cmbPr5);
			repGet[cmb7_cmb5] = repChar;

		}

		int opp;
		cin >> opp;
		map<char , string> oppFind;
		for(int oppCnt = 0 ; oppCnt < opp; oppCnt++)
		{
			char oppPr5 , oppPr7;
			cin >> oppPr5;
			cin >> oppPr7;

			oppFind[oppPr5].push_back(oppPr7);
			oppFind[oppPr7].push_back(oppPr5);
		}

		int ent;
		cin >> ent;
		string res;
		vector<char> opStrtedVec; 
		for(int entCnt = 0 ; entCnt < ent; entCnt++)
		{
			char curChar;
			cin >> curChar;
			res.push_back(curChar);
			if( corectForPair(cmbFind , res , curChar , repGet) )
				continue;

				
			if(corectForOpp(oppFind , res , curChar , opStrtedVec) )
				continue;	
					
			if(res.size() > 1)
			{
				char lastbutOneChar = res.at(res.length() - 2);
				map<char,string>::iterator it;
				it = oppFind.find(lastbutOneChar);
				if(it != oppFind.end())
					opStrtedVec.push_back(lastbutOneChar);
			}
		}

		cout << "Case #" << cnt << ": [";
		if(res.size() > 0)
		{
			cout << res.at(0);
			for(int strCnt = 1 ; strCnt < res.length(); strCnt++)
			{
				cout << ", ";
				cout << res.at(strCnt);
			}
		}
		cout << "]" << endl;


	}
	return 0;
}