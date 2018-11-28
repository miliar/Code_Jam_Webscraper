#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
	int tetCas;
	cin >> tetCas;
	for(int cnt = 1 ; cnt <= tetCas ; cnt++)
	{
		long long strRes;
		int frtCnt = 0;
		vector<long long> canVec;
		long long canNum;
		cin >> canNum;
		for(int canNumcnt = 0; canNumcnt < canNum; canNumcnt++)
		{
			long long curCan;
			cin >> curCan;
			canVec.push_back(curCan);
			if(frtCnt == 0)
			{
				frtCnt++;
				strRes = curCan;
			}
			else
			{
				strRes = strRes ^ curCan;
			}
		}
		if(strRes != 0)
		{	
			cout << "Case #" << cnt << ": " << "NO" << endl;	
		}
		else 
		{
			long long res = 0;
			sort(canVec.begin() , canVec.end());
			for(int canNumcnt = 1; canNumcnt < canNum; canNumcnt++)
			{
				res += canVec[canNumcnt];
			}
			cout << "Case #" << cnt << ": " << res << endl;
		}

		
		
	}
	return 0;
}
