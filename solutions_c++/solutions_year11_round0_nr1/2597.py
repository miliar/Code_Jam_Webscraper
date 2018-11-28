// main.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;

struct wer
{
	int num;
	int rob_num;
};

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	vector <wer> mas;
	vector <wer> masr[3];
	int res[101];
	
	for(int q=1;q<=t;q++)
	{
		int z;
		int count_hid;
		wer s;
		char c;
		int num;
		mas.clear();
		masr[1].clear();
		masr[2].clear();
		//зчитування одиночної ситуації
		cin>>z;
		for(int j=1;j<=z;j++)
			{
			cin>>c;
			if (c=='O')
				{
					cin>>num;
					s.num=num;
					s.rob_num=1;
					mas.push_back(s);
					masr[1].push_back(s);
					
				}
			if (c=='B')
				{
					cin>>num;
					s.num=num;
					s.rob_num=2;
					mas.push_back(s);
					masr[2].push_back(s);
				}

			}

		//обробка даних
		count_hid=0;
		int coor[3];
		coor[1]=1;
		coor[2]=1;
		int cill[3];
		cill[1]=0;
		cill[2]=0;
		masr[1].push_back(s);
		masr[2].push_back(s);
		for(int i=0;i<mas.size();i++)
		{
			int potoch=mas[i].rob_num;
			int ne_potoch=1;
			if(potoch==1) ne_potoch=2;


			int dx=abs(coor[potoch]-mas[i].num)+1;
			count_hid+=dx;

			if(dx<abs(coor[ne_potoch]-masr[ne_potoch][cill [ne_potoch]].num))
			{
				if (coor[ne_potoch]>masr[ne_potoch][cill [ne_potoch] ].num ) coor[ne_potoch]-=dx;
				else coor[ne_potoch]+=dx;
			}else coor[ne_potoch]=masr[ne_potoch][cill [ne_potoch] ].num;

			coor[potoch]=mas[i].num;
			cill[potoch]+=1;
			/*cout<<"O="<<coor[1]<<" B="<<coor[2]<<endl;
			system("pause");*/
		}
		cout<<"Case #"<<q<<": "<<count_hid;
		cout<<endl;
	}
	//system("pause");
	return 0;
}

