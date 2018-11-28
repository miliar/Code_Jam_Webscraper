
#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(__typeof((b).begin()) a = (b).begin();a!=(b).end();++a)
#define vv vector
#define pb push_back
#define ll long long
#define ld long double
#define ss(a) (int)(a).size()
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi vv<int>
#define vs vv<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))
#define ABS(a) ((a)>(0))?(a):(a)
/*
class CBotTrust
{

public:
int Solve()
{
 
	int numOfButtons;
 scanf("%d", &numOfButtons);
 
 int nextButton; 
 char Who='N';
 char LastWho='N';
 int pos[2]={1,1};
 int Steps[100][2];
 rep(k,100)
	 {
		 Steps[k][0]=0;
		 Steps[k][1]=0;
	}

 char First='N';
 int IsFirst;
 char tab;
 int stepIndex=0;
 int maxSteps;
 int lastBigger=-1;
 int TotalSteps=0;
 bool biggerChanged;
 int numOfCouples=0;
 rep (i, numOfButtons)
 {
	 scanf("%c", &tab );	   
	 scanf("%c", &Who );

	 scanf("%c", &tab );
	 scanf("%d", &nextButton);
	 
	 
	 if(First=='N')
		 First=Who;
	 IsFirst=(Who==First);

	 if (Who!=LastWho)
	 {
		 if(IsFirst)
			stepIndex++;
	 }
		
	 	 
	 Steps[stepIndex][IsFirst]+=abs(nextButton-pos[IsFirst])+1;
	 
	 pos[IsFirst]=nextButton;
	
	

	 

	 LastWho=Who;
  }

 
	return  TotalSteps;
}


   




};
*/

class NewBotStruct
{
	public:
	void ReadData()
	{
		char tab,Who;
		int nextButton;
		 scanf("%d", &numOfButtons);
		m_numOfObuttons=0;
		m_numofBbuttons=0;
		 rep (i, numOfButtons)
		{
			 scanf("%c", &tab );	   
			 scanf("%c", &Who );

			 scanf("%c", &tab );
			 scanf("%d", &nextButton);
			 if (Who=='O')
			 {
				 m_Obuttons[m_numOfObuttons][0]=nextButton;
				 m_Obuttons[m_numOfObuttons][1]=i;
					 m_numOfObuttons++;
			 }
			 if (Who=='B')
			 {
				 m_Bbuttons[m_numofBbuttons][0]=nextButton;
				 m_Bbuttons[m_numofBbuttons][1]=i;
					 m_numofBbuttons++;
			 }
		 }
		};

		 int Solve()
		 {
			 ReadData();
			 int TotBtnIdx=0;
			 int bpos=1;
			 int opos=1;
			 int nexBIdx=0;
			 int nextOIdx=0;
			 int Time=0;
			 while ((nexBIdx<m_numofBbuttons) || (nextOIdx<m_numOfObuttons))
			 {
				 int pressed=0;
				 if (nexBIdx<m_numofBbuttons)
				 {
					 if (bpos==m_Bbuttons[nexBIdx][0])
					{
						if (m_Bbuttons[nexBIdx][1]==TotBtnIdx)
						{//press btn
							nexBIdx++;
							TotBtnIdx++;
							pressed=1;
						}
					 }
					else
					{
						 if (bpos>=m_Bbuttons[nexBIdx][0])
							 bpos--;
						 else
							 bpos++;
					 }
				 }
				 
				 if (nextOIdx<m_numOfObuttons)
				 {
					 if (opos==m_Obuttons[nextOIdx][0])
					{
						if (m_Obuttons[nextOIdx][1]==TotBtnIdx)
						{//press btn
							if(pressed==0)
							{
								nextOIdx++;
								TotBtnIdx++;
							}
						}
					 }
					 else
					 {
						 if (opos>=m_Obuttons[nextOIdx][0])
							 opos--;
						 else
							 opos++;
					 }
				 }
				 Time++;
				 
			 }
			 return Time;
		 };
		 int numOfButtons;
		 int m_Obuttons[100][2]; 
		 int m_Bbuttons[100][2];
		 int m_numOfObuttons;
		 int m_numofBbuttons;


};

int main(int argc, char ** argv) {
   int t;
   NewBotStruct botTrust;
   char c;
   char endofline;
   scanf("%d", &t);
   scanf("%c", &endofline);
   rep (i, t) {
       printf("Case #%d: ", i+1);
	 //  storecredit1.GetData();
	   
	    printf("%d",botTrust.Solve());

       printf("\n");
   }
   return 0;
}