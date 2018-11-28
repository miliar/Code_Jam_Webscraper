#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int t,na,nb;
int flaga[100],flagb[100],resulta,resultb;
int ad[100],ar[100],bd[100],br[100];


int main(){
	int n;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin>>n;
	for(int i=0; i<n; i++){
		resulta = 0;resultb =0;
		fin>>t;
		memset(flaga,0,sizeof(flaga));
		memset(flagb,0,sizeof(flagb));
		memset(ad,0,sizeof(ad));
		memset(bd,0,sizeof(bd));
		memset(ar,0,sizeof(ar));
		memset(br,0,sizeof(br));
		fin>>na>>nb;
		string temp;
		for(int j=0;j<na;j++)
		{
			fin>>temp;
			ad[j]=1000*(temp[0]-48)+100*(temp[1]-48)+10*(temp[3]-48)+(temp[4]-48);
			fin>>temp;
			ar[j]=1000*(temp[0]-48)+100*(temp[1]-48)+10*(temp[3]-48)+(temp[4]-48);
			ar[j] = (ar[j] + t) % 100 %60 + (ar[j] + t) % 100 /60 * 100 + ar[j] / 100 * 100;				

		}
		for(int j=0;j<nb;j++)
		{
			fin>>temp;
			bd[j]=1000*(temp[0]-48)+100*(temp[1]-48)+10*(temp[3]-48)+(temp[4]-48);
			fin>>temp;
			br[j]=1000*(temp[0]-48)+100*(temp[1]-48)+10*(temp[3]-48)+(temp[4]-48);
			br[j] = (br[j] + t) % 100 %60 + (br[j] + t) % 100 /60 * 100 + br[j] / 100 * 100;
		}
		int numa = na, numb = nb;
		for(; numa > 0 && numb > 0;)
		{
			int flag = 1, side =0,//0 for A, 1 for B
				arr = - 1 - t;
			int mina = 2500, minb=2500;
			for (int j = 0; j< na; j++)
				if (flaga[j]==0)
					mina=(ad[j] < mina) ? ad[j]:mina;
			for (int j = 0; j< nb; j++)
				if (flagb[j]==0)
					minb=(bd[j] < minb) ? bd[j]:minb;
			side = (mina < minb)?0:1;
			if (side ==0)
				resulta++;
			else 
				resultb++;
			while (flag == 1)
			{
				flag =0;
				int num = -1, late = 2500;
				if (side==0)
				{
					for(int j = 0; j < na; j++)
					{
						if (flaga[j] == 0 && ad[j] >= arr && ad[j] < late)
						{
							late = ad[j];num = j;
						}
					}
					if (num > -1)
					{
						flaga[num] = 1; arr = ar[num];numa--;flag = 1;side = 1;
					}
				}
				else
				{
					for(int j = 0; j < nb; j++)
					{
						if (flagb[j] == 0 && bd[j] >= arr && bd[j] < late)
						{
							late = bd[j];num = j;
						}
					}
					if (num > -1)
					{
						flagb[num] = 1; arr = br[num];numb--;flag = 1; side = 0;
					}
				}
			}
		}
		resulta += numa;
		resultb += numb;
		cout<<"Case #"<<i+1<<": "<<resulta<<"\t"<<resultb<<"\n";//answer;
		fout<<"Case #"<<i+1<<": "<<resulta<<" "<<resultb<<"\n";//answer;

	}
	fin.close();
	fout.close();
}