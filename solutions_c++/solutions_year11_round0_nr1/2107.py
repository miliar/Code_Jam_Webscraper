#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct ButnInfo
{
	char roboClor;
	int butnLab;
	ButnInfo(char rbCol , int bunNum)
	{
		roboClor = rbCol;
		butnLab = bunNum;
	}

};


int main(){
	int tetCas;
	cin >> tetCas;
	for(int cnt = 1 ; cnt <= tetCas ; cnt++)
	{
		vector<ButnInfo> ordVec;
		vector<int> orgButn;
		vector<int> bluButn;
		long res;
		int odrNum;
		cin >> odrNum;
		int curPosOrg = 1, curPosBlu = 1;
		int tarPosOrgInx = 0, tarPosBluInx = 0;
		int tarPosOrgBut = 0, tarPosBluBut = 0;

		for(int ordcnt = 0 ; ordcnt < odrNum ; ordcnt++)
		{
			char rbCol;
			int butnNum;
			cin >> rbCol;
			cin >> butnNum;
			ButnInfo butnInfo(rbCol , butnNum);
			ordVec.push_back(butnInfo);
			if(rbCol == 'O')
			{
				orgButn.push_back(butnNum);
			}
			else if(rbCol == 'B')
			{
				bluButn.push_back(butnNum);
			}
		}
		
		long long tolTimElas = 0;
		int maxOrgInx = orgButn.size();
		int maxBluInx = bluButn.size();
		for(int ordcnt = 0; ordcnt < odrNum; ordcnt++)
		{
			int timElas = 0;
			if(tarPosOrgInx < maxOrgInx)
				tarPosOrgBut = orgButn[tarPosOrgInx];
			if(tarPosBluInx < maxBluInx)
				tarPosBluBut = bluButn[tarPosBluInx];
			ButnInfo curButnInfo = ordVec[ordcnt];
			char curRobo = curButnInfo.roboClor;
			int curTarLab = curButnInfo.butnLab;

			if(curRobo == 'O')
			{
				timElas = (curTarLab - curPosOrg);
				timElas = (timElas > 0 ? timElas : -timElas);
				timElas += 1;
				tolTimElas += timElas;
				curPosOrg = curTarLab;
				tarPosOrgInx++;
				
				if(tarPosBluInx < maxBluInx)
				{
					int disForBlu = tarPosBluBut - curPosBlu;
					int timReqForBlu = disForBlu > 0 ? disForBlu : -disForBlu;
					if(timReqForBlu <= timElas)
					{
						curPosBlu = tarPosBluBut;
					}
					else 
					{
						curPosBlu += (disForBlu > 0 ? timElas : -timElas);
					}
				}
				
			}
			else
			{
				timElas = (curTarLab - curPosBlu);
				timElas = (timElas > 0 ? timElas : -timElas);
				timElas += 1;
				tolTimElas += timElas;
				curPosBlu = curTarLab;
				tarPosBluInx++;
			
				if(tarPosOrgInx < maxOrgInx)
				{
					int disForOrg = tarPosOrgBut - curPosOrg;
					int timReqForOrg = disForOrg > 0 ? disForOrg : -disForOrg;
					if(timReqForOrg <= timElas)
					{
						curPosOrg = tarPosOrgBut;
					}
					else 
					{
						curPosOrg += (disForOrg > 0 ? timElas : -timElas);
					}
				}
				
			}
		}

		cout << "Case #" << cnt << ": " << tolTimElas << endl;
	}
	return 0;
}
