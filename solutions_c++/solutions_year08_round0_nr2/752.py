#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
using namespace std;
vector<int>da;
vector<int>aa;
vector<int>db;
vector<int>ab;
int ta;
int na , nb , noa , nob;

void calc()
{
	noa = nob = 0;
	int nexta=0 , nextd=0 ,  avail = 0;
	
	for(int i=0 ; i <= (23*60 + 59) && nextd<da.size(); i++)
	{

		while(ab[nexta] == i && nexta < ab.size())
		{
			avail++;
			nexta++;
		}
		
		while(da[nextd] == i && nextd<da.size())
		{
		
			if(avail)
				avail--;
		
			else
				noa++;
			nextd++;
		}
	}

  	nexta = nextd = 0;
	avail = 0;
	
	for(int i=0 ; i <= (23*60 + 59) && nextd<db.size(); i++)
	{

		while(aa[nexta] == i && nexta < aa.size())
		{
			avail++;
			nexta++;
		}

		while(db[nextd] == i && nextd<db.size())
		{
	
			if(avail)
				avail--;
	
			else
				nob++;
			nextd++;
		}
	}
	
}

main()
{
	int t,hh,mm;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%d",&ta);
		scanf("%d %d",&na , &nb);
		da.clear();
		aa.clear();
		db.clear();
		ab.clear();
		for(int j=0 ; j<na ; j++)
		{
			scanf("%d:%d" , &hh , &mm);
			da.push_back(hh*60+mm);
			scanf("%d:%d" , &hh , &mm);
			aa.push_back(hh*60+mm+ta);
		}

		for(int j=0 ; j<nb ; j++)
		{
			scanf("%d:%d" , &hh , &mm);
			db.push_back(hh*60+mm);
			scanf("%d:%d" , &hh , &mm);
			ab.push_back(hh*60+mm+ta);
		} 

		sort(da.begin() , da.end());
		sort(aa.begin() , aa.end());
		sort(db.begin() , db.end());
		sort(ab.begin() , ab.end());

		/*cout<<ta<<" "<<na<<"  "<<nb<<endl;
		for(int j=0;j<da.size();j++)
			cout<<da[j]<<"  "<<aa[j]<<endl;
		cout<<"----"<<endl;
		for(int j=0;j<db.size();j++)
			cout<<db[j]<<"  "<<ab[j]<<endl;	
		cout<<"----------------------------------------------"<<endl;*/
		calc();
		cout<<"Case #"<<i+1<<": "<<noa<<" "<<nob<<endl;
		
	}
	return 0;
}
